# Testes de integração com GenAI

## Contexto

Este repositório registra um experimento acadêmico sobre uso de GenAI como apoio à criação de testes de integração. O cenário é fictício e dá continuidade a uma função de avaliação de movimentações industriais.

## Integração testada

O fluxo integra três partes:

1. um cliente envia um evento por HTTP;
2. a API FastAPI valida o contrato JSON;
3. o módulo `avaliar_movimentacao` classifica o evento como `NORMAL` ou `ALERTA`.

Endpoint: `POST /api/v1/movimentacoes/avaliacoes`.

## Tipos de prompt utilizados

- **Zero-shot:** descrição curta do endpoint, sem exemplos de teste.
- **Few-shot orientado por contrato:** regras completas, códigos HTTP, exemplos e categorias obrigatórias de cobertura.

Os prompts estão na pasta `prompts/` e a comparação está em `resultados/comparacao.md`.

## Resultado do experimento

O zero-shot gerou dois testes básicos. O few-shot produziu uma suíte mais diversa, incluindo fronteiras, tipos inválidos, campos ausentes, campo adicional, corpo vazio e JSON malformado. As asserções passaram a verificar tanto o código HTTP quanto o JSON completo.

## Execução

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -q
```

No Windows PowerShell, a ativação do ambiente é:

```powershell
.venv\Scripts\Activate.ps1
```

## Conclusão

O prompt mais detalhado elevou a precisão e a diversidade dos testes, mas a revisão humana continuou necessária para confirmar as regras, evitar cenários inventados e remover redundâncias. A GenAI funcionou como copiloto, não como autoridade final sobre o contrato.

## Dados

Todos os nomes e dados são fictícios. O projeto não contém credenciais, segredos ou informações confidenciais.
