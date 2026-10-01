---
name: refino
description: Prepara a pauta do refino a partir das histórias em rascunho, do board e das perguntas em aberto; depois do refino, registra decisões a partir da transcrição. Use na véspera do refino ou quando o PM digitar /refino.
---

# /refino

Modos:
- `/refino` (antes) → pauta.
- `/refino depois` → registra o resultado a partir da extração do Copilot da transcrição.

## Antes

1. Leia as histórias em `Historias/` que ainda não foram refinadas, o retrato mais recente do board e as perguntas em aberto dos PRDs.
2. **Ordem de discussão:** primeiro o que bloqueia a próxima sprint, depois o que tem mais dúvidas. Estime o tempo de cada item e alerte se passar da duração do refino.
3. **Para cada item:** objetivo em uma frase, link, 1 a 3 perguntas para o time e quem precisa opinar.
4. **Perguntas para o tech lead** que precisam de resposta antes do refino: liste à parte, para o PM mandar antes.
5. Escreva a pauta na seção do refino na nota do dia (ou do dia do refino) e em `Artefatos/refino-AAAA-MM-DD.md`.

## Depois

1. Peça ao PM a extração do Copilot do refino (prompt `02-extracao-diaria.md` restrito a essa reunião).
2. Para cada história: aceita, ajustar (o quê), dividida, descartada, estimativa (se houver na transcrição).
3. Atualize as histórias em `Historias/` com as mudanças, mantendo `status: rascunho` e um `#revisar` para cada ajuste.
4. Novas dúvidas viram perguntas no PRD; decisões vão para `Historico/decisoes.md`.
