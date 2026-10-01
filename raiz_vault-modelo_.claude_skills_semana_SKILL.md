---
name: semana
description: Revisão semanal do PM a partir das notas diárias - padrões de energia e agenda, decisões, pendências, check-in dos OKRs, fila de revisão e temas de estudo. Use na sexta de manhã ou quando o PM digitar /semana.
---

# /semana

Objetivo: em 30 minutos, olhar a semana com dados e sair com o que fazer na próxima.

## Entrada

- Notas diárias da semana (segunda a sexta) em `01-Diario/`.
- `OKRs/` do trimestre atual e `Roadmap.md` de cada tema ativo.
- A fila "A revisar" (notas com `status: rascunho` e tarefas `#revisar` abertas).
- Semanas anteriores em `01-Diario/Semanas/` para comparar tendências.

## Passos

1. **Energia e agenda:** tabela por dia com energia (1–5), reuniões planejadas, surgidas no dia e canceladas. Aponte correlações simples ("nos dias com 3+ reuniões surgidas, energia média 2"). Com 4+ semanas de dados, compare com as anteriores. Não faça diagnóstico de saúde.
2. **O que drenou e o que avançou:** agrupe as respostas da reflexão diária em padrões (tipos de reunião, pessoas, temas).
3. **Decisões da semana** por tema, com link.
4. **Pendências:** abertas, atrasadas, e as que estão com outras pessoas há mais de uma semana.
5. **Check-in dos OKRs:** para cada KR, pergunte ao PM o valor atual (se houver fonte) e a confiança de 1 a 5. Registre na tabela "Check-ins semanais" do arquivo de OKRs. Nunca preencha valor sem fonte.
6. **Fila de revisão:** quantos itens, os mais antigos, e se está crescendo.
7. **Candidatos a princípio:** decisões que se repetiram ou que outros vão precisar aplicar. Sugira 1 para o `/principio`.
8. **Temas de estudo:** 2 ou 3 assuntos que apareceram como dúvida (`?`) ou lacuna, com uma sugestão de formato (leitura curta, vídeo, conversa com alguém).
9. **Próxima semana:** reuniões críticas, entregas que não podem escorregar, 3 prioridades.

## Saída

- Nota `01-Diario/Semanas/AAAA-Www.md` (`tipo: revisao-semanal`).
- No chat: 5 linhas com o essencial e a sugestão de princípio.
