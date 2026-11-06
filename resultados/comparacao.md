# Comparação dos resultados

| Aspecto | Prompt zero-shot | Prompt few-shot orientado por contrato |
|---|---|---|
| Casos gerados | 2 | 13 combinações de teste |
| Caminho feliz | Sim | Sim |
| Fronteira `quantidade == limite` | Não | Sim |
| Corpo JSON completo | Não | Sim |
| Dados inválidos | Apenas negativo | Negativo, zero, decimal, booleano e ausências |
| Falhas de contrato HTTP | Não | Corpo vazio, campo extra e JSON malformado |
| Suposições indevidas | Baixo, mas com cobertura superficial | Menor devido ao contrato explícito |

## Análise

O prompt zero-shot foi útil para uma primeira exploração, mas gerou cobertura limitada e asserções superficiais. O prompt few-shot, apoiado por contrato e exemplos, produziu casos mais precisos e variados, principalmente nas fronteiras e na validação do payload.

A principal melhoria não veio apenas do uso de exemplos, mas da explicitação das regras e dos códigos HTTP. A revisão humana continuou necessária para remover redundâncias e confirmar que cada cenário representava uma regra válida.
