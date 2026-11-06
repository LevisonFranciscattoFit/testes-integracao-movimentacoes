# Prompt 2: few-shot orientado por contrato

Você é um QA Engineer especializado em testes de integração de APIs REST com Python, FastAPI e pytest.

## Contrato

Endpoint: `POST /api/v1/movimentacoes/avaliacoes`

Payload obrigatório:

```json
{
  "zona_id": "ZONA-A",
  "qtd_movimentos": 11,
  "limite_permitido": 10
}
```

Regras:
- `zona_id` é texto não vazio;
- `qtd_movimentos` é inteiro maior ou igual a zero;
- `limite_permitido` é inteiro maior que zero;
- booleanos não são aceitos como inteiros;
- campos adicionais são rejeitados;
- quantidade menor ou igual ao limite retorna `NORMAL` e excesso zero;
- quantidade maior retorna `ALERTA` e informa o excesso;
- payload inválido retorna HTTP 422;
- payload válido retorna HTTP 200;
- não existe autenticação, banco de dados ou persistência.

Exemplo de caso válido:
- entrada: quantidade 10 e limite 10;
- esperado: HTTP 200, status `NORMAL`, excesso 0 e mensagem completa.

Exemplo de erro:
- entrada: quantidade -1;
- esperado: HTTP 422 e corpo com a chave `detail`.

Gere testes de integração independentes usando `TestClient`. Cubra caminho feliz, os dois lados da fronteira, singular e plural da mensagem, campos ausentes, tipos incorretos, booleano, campo adicional, corpo vazio e JSON malformado. Verifique tanto o código HTTP quanto o corpo JSON. Use nomes descritivos e não altere as expectativas apenas para fazer os testes passarem.
