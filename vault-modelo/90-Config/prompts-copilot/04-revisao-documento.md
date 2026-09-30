# Prompt 04 · Revisão de documento

**Quando:** ao receber um documento, spec do tech lead, proposta ou apresentação para opinar.
**Como:** no Copilot, com o documento aberto ou referenciado (/ nome do arquivo). Para specs do tech lead, a leitura é pela ótica de produto.

```text
Analise o documento "{{nome}}" pela ótica de um Product Manager responsável por {{produto/tema}}.

Traga, nesta ordem:
1. Decisões que o documento pede de mim, cada uma em uma frase
2. Premissas assumidas, explícitas ou implícitas
3. O que muda em relação ao estado atual do produto
4. Riscos de governança e segurança (permissões, dados sensíveis, autenticação, auditoria, prompt injection, conformidade)
5. Pontos que atendem ou não atendem aos requisitos de produto (se for uma spec técnica)
6. Afirmações técnicas ou números que devo verificar, com a página ou seção
7. Classifique cada decisão como: aprovar / ajustar / discutir, com uma linha de justificativa

Não resuma o documento inteiro. Foque no que exige minha decisão ou atenção.
Cite a seção de origem de cada item.
```

Salve a resposta na nota do dia ou no PRD relacionado. Os itens "ajustar" e "discutir" viram pendências.
