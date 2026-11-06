import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)
ENDPOINT = "/api/v1/movimentacoes/avaliacoes"


@pytest.mark.parametrize(
    ("quantidade", "limite", "status", "excesso", "mensagem"),
    [
        (8, 10, "NORMAL", 0, "Movimentação dentro do limite permitido."),
        (10, 10, "NORMAL", 0, "Movimentação dentro do limite permitido."),
        (11, 10, "ALERTA", 1, "Limite excedido em 1 movimentação."),
        (13, 10, "ALERTA", 3, "Limite excedido em 3 movimentações."),
    ],
)
def test_contrato_para_casos_validos(
    quantidade: int,
    limite: int,
    status: str,
    excesso: int,
    mensagem: str,
) -> None:
    resposta = client.post(
        ENDPOINT,
        json={
            "zona_id": "ZONA-A",
            "qtd_movimentos": quantidade,
            "limite_permitido": limite,
        },
    )

    assert resposta.status_code == 200
    assert resposta.json() == {
        "zona_id": "ZONA-A",
        "status": status,
        "excesso_movimentos": excesso,
        "mensagem": mensagem,
    }


@pytest.mark.parametrize(
    "payload",
    [
        {"zona_id": "ZONA-A", "qtd_movimentos": -1, "limite_permitido": 10},
        {"zona_id": "ZONA-A", "qtd_movimentos": 5, "limite_permitido": 0},
        {"zona_id": "ZONA-A", "qtd_movimentos": 5.5, "limite_permitido": 10},
        {"zona_id": "ZONA-A", "qtd_movimentos": True, "limite_permitido": 10},
        {"zona_id": "ZONA-A", "limite_permitido": 10},
        {"qtd_movimentos": 5, "limite_permitido": 10},
        {
            "zona_id": "ZONA-A",
            "qtd_movimentos": 5,
            "limite_permitido": 10,
            "campo_extra": "não permitido",
        },
    ],
)
def test_contrato_rejeita_payload_invalido(payload: dict) -> None:
    resposta = client.post(ENDPOINT, json=payload)

    assert resposta.status_code == 422
    assert "detail" in resposta.json()


def test_corpo_vazio_retorna_erro_de_validacao() -> None:
    resposta = client.post(ENDPOINT, json={})

    assert resposta.status_code == 422
    assert "detail" in resposta.json()


def test_json_malformado_retorna_erro_de_validacao() -> None:
    resposta = client.post(
        ENDPOINT,
        content='{"zona_id": "ZONA-A",',
        headers={"Content-Type": "application/json"},
    )

    assert resposta.status_code == 422
    assert "detail" in resposta.json()
