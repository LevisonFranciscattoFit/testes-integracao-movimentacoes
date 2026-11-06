from typing import Literal

from fastapi import FastAPI
from pydantic import BaseModel, ConfigDict, Field

from app.movimentacoes import avaliar_movimentacao

app = FastAPI(title="API fictícia de avaliação de movimentações", version="1.0.0")


class AvaliacaoEntrada(BaseModel):
    model_config = ConfigDict(extra="forbid")

    zona_id: str = Field(min_length=1)
    qtd_movimentos: int = Field(ge=0, strict=True)
    limite_permitido: int = Field(gt=0, strict=True)


class AvaliacaoSaida(BaseModel):
    zona_id: str
    status: Literal["NORMAL", "ALERTA"]
    excesso_movimentos: int
    mensagem: str


@app.post(
    "/api/v1/movimentacoes/avaliacoes",
    response_model=AvaliacaoSaida,
    status_code=200,
)
def criar_avaliacao(dados: AvaliacaoEntrada) -> AvaliacaoSaida:
    """Valida o contrato HTTP e integra a API ao módulo de avaliação."""
    resultado = avaliar_movimentacao(
        qtd_movimentos=dados.qtd_movimentos,
        limite_permitido=dados.limite_permitido,
    )
    return AvaliacaoSaida(
        zona_id=dados.zona_id,
        status=resultado.status,
        excesso_movimentos=resultado.excesso_movimentos,
        mensagem=resultado.mensagem,
    )
