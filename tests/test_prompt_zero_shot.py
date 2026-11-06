from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)
ENDPOINT = "/api/v1/movimentacoes/avaliacoes"


def test_avaliacao_valida_retorna_alerta() -> None:
    resposta = client.post(
        ENDPOINT,
        json={
            "zona_id": "ZONA-A",
            "qtd_movimentos": 11,
            "limite_permitido": 10,
        },
    )

    assert resposta.status_code == 200
    assert resposta.json()["status"] == "ALERTA"


def test_quantidade_negativa_retorna_erro() -> None:
    resposta = client.post(
        ENDPOINT,
        json={
            "zona_id": "ZONA-A",
            "qtd_movimentos": -1,
            "limite_permitido": 10,
        },
    )

    assert resposta.status_code == 422
