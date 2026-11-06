from dataclasses import dataclass
from typing import Literal

Status = Literal["NORMAL", "ALERTA"]


@dataclass(frozen=True)
class ResultadoMovimentacao:
    status: Status
    excesso_movimentos: int
    mensagem: str


def avaliar_movimentacao(
    qtd_movimentos: int,
    limite_permitido: int,
) -> ResultadoMovimentacao:
    """Classifica uma quantidade de movimentações em relação a um limite."""
    if isinstance(qtd_movimentos, bool) or not isinstance(qtd_movimentos, int):
        raise TypeError("qtd_movimentos deve ser um número inteiro.")
    if isinstance(limite_permitido, bool) or not isinstance(limite_permitido, int):
        raise TypeError("limite_permitido deve ser um número inteiro.")
    if qtd_movimentos < 0:
        raise ValueError("qtd_movimentos não pode ser negativo.")
    if limite_permitido <= 0:
        raise ValueError("limite_permitido deve ser maior que zero.")

    excesso = max(0, qtd_movimentos - limite_permitido)
    if excesso == 0:
        return ResultadoMovimentacao(
            status="NORMAL",
            excesso_movimentos=0,
            mensagem="Movimentação dentro do limite permitido.",
        )

    unidade = "movimentação" if excesso == 1 else "movimentações"
    return ResultadoMovimentacao(
        status="ALERTA",
        excesso_movimentos=excesso,
        mensagem=f"Limite excedido em {excesso} {unidade}.",
    )
