---
name: demo
description: Monta a demo mensal - registro de entregas do mês a partir do vault, PPT no template da empresa e roteiro da apresentação com plano B. Use na semana da demo ou quando o PM digitar /demo.
---

# /demo

Argumento opcional: mês (`AAAA-MM`). Padrão: mês atual.

## Entrada

- Notas diárias do mês, `Historico/decisoes.md`, retratos do board (`03-Backlog/Retratos/`), PRDs e histórias concluídas.
- `Roadmap.md` (mês atual = o que foi prometido).
- `Metricas/Relatorios/AAAA-MM.md` e check-ins dos OKRs.

## Passos

1. **Registro de entregas** em `Entregas/AAAA-MM.md` (`tipo: demo`, `status: rascunho`):
   - Prometido x entregue: para cada item do mês atual do roadmap, entregue, parcial ou não entregue, com evidência (item do board concluído, decisão, nota).
   - Entregas fora do roadmap (e por quê entraram).
   - Impacto: métricas e KRs que se moveram, com fonte.
   - Quem participou de cada entrega (reconhecimento do time).
   - Aprendizados do mês.
2. **Pergunte ao PM** o que será demonstrado ao vivo e por quem, antes de montar o roteiro.
3. **Roteiro da apresentação** (no mesmo arquivo): ordem, quem apresenta, cenário de cada demonstração, tempo por bloco, e **plano B** (prints ou vídeo) para cada demonstração ao vivo.
4. **PPT** seguindo `90-Config/ppt/como-gerar-ppt.md`:
   1. Capa
   2. Objetivo do mês e resumo em uma frase
   3. Entregas agrupadas por objetivo ou OKR (uma por slide quando for demonstração)
   4. Métricas e KRs (gráficos nativos)
   5. O que não entregamos e por quê
   6. Próximo mês (do roadmap já rolado ou a rolar)
   7. Agradecimentos ao time
   Salve em `Artefatos/demo-AAAA-MM.pptx`.
5. Sugira ao PM rodar `/roadmap rolar` depois da demo e `/comunicado demo` para a edição especial.
