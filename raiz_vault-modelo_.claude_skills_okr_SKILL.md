---
name: okr
description: Ajuda o PM a escrever e revisar os OKRs do trimestre do tema (qualidade de objetivos e KRs, baseline, fonte, dono) e a fechar o trimestre a partir dos check-ins. Use no início ou fim do trimestre ou quando o PM digitar /okr.
---

# /okr

Modos:
- `/okr` ou `/okr escrever` → rascunho ou revisão dos OKRs do trimestre.
- `/okr fechar` → fechamento do trimestre.

## Escrever

1. Leia `_contexto.md`, `Metricas/_dicionario.md`, o fechamento do trimestre anterior (se houver), evidências e decisões recentes. Se a empresa tiver OKRs de nível superior, peça ao PM que cole os objetivos relevantes.
2. Se o PM já tiver um rascunho, revise-o. Se não, proponha 2 ou 3 objetivos com 2 a 4 KRs cada.
3. **Checagem de qualidade de cada KR:**
   - É resultado, não entrega? ("Lançar X" é entrega. "X% dos times usando Y" é resultado.) Entrega vai para o roadmap.
   - É mensurável com uma fonte que existe hoje? Se não, sinalize: precisa de `/metricas dashboard`.
   - Tem baseline? Sem baseline: `[FALTA: baseline]`. Nunca estime.
   - A meta é ambiciosa mas plausível? Pergunte ao PM, não decida.
   - Tem dono?
4. **Objetivo:** qualitativo, sem número, entendível por quem não é do time.
5. Ligue cada KR às iniciativas do `Roadmap.md` e às métricas do dicionário.
6. Salve em `OKRs/AAAA-QN.md` a partir de `_modelo-trimestre.md` (`status: rascunho`).

## Fechar

1. Leia os check-ins semanais do arquivo do trimestre.
2. Para cada KR: valor final (com fonte, pedido ao PM), atingido ou não, e o que explicou o resultado.
3. Aprendizados e o que levar para o próximo trimestre.
4. Preencha a seção "Fechamento do trimestre".
