---
name: daily
description: Prepara o PM para conduzir a daily a partir do print ou export do board, do retrato anterior e dos compromissos da daily anterior. Use antes da daily ou quando o PM digitar /daily.
---

# /daily

Objetivo: em 2 minutos, dar ao PM fatos para conduzir a daily de forma curta: o que está parado, o que está bloqueado sem dono e o que foi prometido e não andou.

## Entrada

- **Board de hoje:**
  - `backlog.modo: manual` → o arquivo mais recente `00-Inbox/_entrada/board-AAAA-MM-DD.png` (ou `.csv`). Se não existir, peça ao PM para salvar o print.
  - `backlog.modo: mcp` → leia os itens da sprint atual pelo servidor MCP configurado.
- **Retratos anteriores:** `03-Backlog/Retratos/` (os últimos 10 dias úteis).
- **Compromissos da daily anterior:** na nota do último dia útil, seção da daily: campo "Compromissos" e, se existir, a extração do Copilot da transcrição (prompt `03-daily.md`).

## Passos

1. **Leia o board** e monte uma tabela: ID, título, status, responsável, bloqueado (sim/não). Se a imagem estiver ilegível em algum item, marque `[ilegível]` e não invente.
2. **Salve o retrato** em `03-Backlog/Retratos/AAAA-MM-DD.md` (frontmatter `tipo: retrato-board`, `status: validado`, porque é registro factual). Mova o print para `00-Inbox/_processado/`.
3. **Compare com os retratos anteriores:**
   - **Parados:** mesmo status há 3 dias úteis ou mais. Informe há quantos dias.
   - **Voltaram:** item que regrediu de status.
   - **Novos na sprint:** itens que apareceram depois do início da sprint.
4. **Bloqueios sem dono:** bloqueado e sem responsável, ou bloqueado há mais de 1 dia sem ação registrada.
5. **Compromissos:** para cada compromisso de ontem (`→ Nome: ação`), verifique no board se o item andou. Liste só os que não andaram.
6. **Escreva na seção da daily** da nota de hoje um bloco "Pauta sugerida" com no máximo 5 pontos, em ordem de impacto.

## Saída no chat

A pauta sugerida, direta, com nome das pessoas e IDs. Nada de julgamento sobre as pessoas: fatos do board.

## Regras

- Não use a pauta para expor ninguém. Formule como pergunta: "PROJ-123 está em revisão há 4 dias. Precisa de ajuda?"
- Quando o MCP da ferramenta estiver pronto, basta mudar `backlog.modo` em `config.md`.
