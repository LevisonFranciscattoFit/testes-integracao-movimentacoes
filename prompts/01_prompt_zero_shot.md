# Prompt 1: zero-shot

Você é um QA Engineer especializado em testes de integração de APIs REST.

Crie testes de integração com pytest para uma API FastAPI que recebe eventos fictícios de movimentação industrial pelo endpoint `POST /api/v1/movimentacoes/avaliacoes`.

A requisição possui `zona_id`, `qtd_movimentos` e `limite_permitido`. A resposta informa `zona_id`, `status`, `excesso_movimentos` e `mensagem`.

Gere testes que validem a integração entre a camada HTTP e o módulo de avaliação. Utilize dados fictícios e não invente autenticação, banco de dados ou integrações externas.
