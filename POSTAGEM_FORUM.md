# Testes de integração de uma API fictícia de movimentações industriais

Para esta atividade, reutilizei o cenário das atividades anteriores e criei uma pequena integração entre uma API REST e um módulo de avaliação de movimentações. O cliente envia `zona_id`, quantidade de movimentações e limite permitido. A API valida o contrato e o módulo retorna `NORMAL` ou `ALERTA`, além da quantidade excedente.

Utilizei dois tipos de prompt. O primeiro foi **zero-shot**, com uma descrição resumida do endpoint e sem exemplos. Ele gerou casos úteis para iniciar a suíte, mas ficou concentrado em um caminho válido e em um erro simples. As asserções verificavam principalmente o status HTTP e um campo da resposta.

O segundo foi um **few-shot orientado por contrato**. Acrescentei regras de domínio, códigos HTTP, exemplos de sucesso e erro, fronteiras e categorias obrigatórias. Esse prompt aumentou a diversidade dos casos, incluindo igualdade com o limite, excesso no singular e plural, valores negativos, limite zero, decimal, booleano, campos ausentes, campo adicional, corpo vazio e JSON malformado. Também passou a verificar o corpo JSON completo.

Os principais ajustes foram explicitar que a igualdade com o limite retorna `NORMAL`, determinar HTTP 200 e 422, rejeitar booleanos e campos adicionais e proibir a criação de autenticação, banco ou persistência não existentes. Também solicitei testes independentes e nomes descritivos.

A experiência mostrou que o prompt detalhado melhora a precisão e reduz suposições, mas não elimina a revisão humana. Foi necessário conferir se os testes representavam regras definidas e se não existiam cenários redundantes. A GenAI foi útil para ampliar a cobertura, especialmente nas fronteiras e falhas do contrato, mas permaneceu como copiloto da atividade de QA.

**Repositório:** inserir aqui o link após publicar os arquivos no GitHub.
