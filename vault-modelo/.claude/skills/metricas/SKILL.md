---
name: metricas
description: Define as métricas do tema a partir dos OKRs, escreve especificações de dashboard para o time de dados e gera o relatório de métricas a partir de prints ou exports, sem nunca estimar números. Use quando o PM digitar /metricas definir, /metricas dashboard ou /metricas relatorio.
---

# /metricas

## /metricas definir

1. Leia `_contexto.md`, `OKRs/` do trimestre e o dicionário atual.
2. Proponha uma **métrica principal** (a que melhor resume o valor que o produto entrega) e as **métricas que a movem**, agrupadas em: adoção, uso, qualidade/governança, experiência. Para cada uma: que pergunta responde, que decisão ela ajuda a tomar e a qual KR se liga.
3. Corte o que não ajuda a decidir nada. Menos é melhor: de 5 a 10 métricas.
4. Para cada métrica, preencha a linha do dicionário (definição, fórmula, fonte provável, granularidade, segmentos). Baseline e meta: `[FALTA]` até ter fonte.
5. Atualize `Metricas/_dicionario.md` e a "Métrica principal" no `_contexto.md` (`status: rascunho`).

## /metricas dashboard <nome>

Gera `Metricas/dashboard-<nome>.md` (`tipo: dashboard-spec`) para orientar o time de dados. O PM define **o quê e por quê**; o time de dados decide **como**.

- **Pergunta de negócio** que o dashboard responde e **decisões** que ele apoia.
- **Público** e frequência de consulta.
- **Métricas** (IDs do dicionário), com definição e fórmula repetidas para não haver ambiguidade.
- **Visualizações sugeridas:** para cada pergunta, o tipo de gráfico e por quê (tendência → linha; comparação entre segmentos → barras; funil → funil).
- **Filtros e segmentos**, granularidade, período padrão.
- **Frequência de atualização** e tolerância de atraso.
- **Critérios de aceite** do dashboard ("o número de servers publicados bate com o registro oficial").
- **Esboço:** prompt para a IA do FigJam desenhar o layout (ou diagrama via conector).
- **Perguntas para o time de dados:** disponibilidade da fonte, qualidade, esforço.

## /metricas relatorio

1. Entrada: prints ou exports em `00-Inbox/_entrada/metricas-AAAA-MM-DD.*`. Leia os números **exatamente** como estão. Ilegível → `[ilegível]`.
2. Para cada métrica: valor atual, variação contra o período anterior, comparação com a meta e com o KR.
3. **Anomalias:** mudanças bruscas. Para cada uma, 1 a 3 hipóteses, marcadas como hipóteses, e o que verificar.
4. Ligue a eventos do período (entregas, incidentes, comunicados) quando houver registro no vault.
5. Salve em `Metricas/Relatorios/AAAA-MM.md` (`tipo: relatorio-metricas`, `status: rascunho`). Se pedido, gere slides pelo `90-Config/ppt/como-gerar-ppt.md` com gráficos nativos.
6. Os valores alimentam o check-in dos OKRs no `/semana` e o `/demo`.

## Regra de ouro

Nenhum número vem da sua cabeça. Todo número tem fonte (arquivo e data). Sem fonte: `[FALTA]` e `#revisar número sem fonte`.
