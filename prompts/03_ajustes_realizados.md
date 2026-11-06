# Ajustes realizados nos prompts

A primeira solicitação era genérica e produziu apenas um caso válido e um caso de quantidade negativa. As asserções verificavam principalmente o código HTTP e o campo `status`.

O segundo prompt foi refinado com:

1. contrato completo do payload e da resposta;
2. regra explícita para a igualdade com o limite;
3. códigos HTTP esperados;
4. rejeição explícita de booleanos e campos adicionais;
5. categorias mínimas de cobertura;
6. obrigação de conferir o JSON completo;
7. proibição de inventar autenticação, persistência ou novas regras;
8. exemplo de caminho feliz e de erro.

Esses ajustes reduziram suposições e aumentaram a diversidade e a precisão dos casos gerados.
