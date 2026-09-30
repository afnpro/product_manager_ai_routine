---
name: entrevista
description: Prepara roteiros de entrevista com usuários e, depois, extrai necessidades e dores atômicas com evidência para o repositório do tema. Também sintetiza padrões entre entrevistas. Use quando o PM digitar /entrevista roteiro, /entrevista ou /entrevista sintese.
---

# /entrevista

## /entrevista roteiro <hipóteses ou objetivo>

1. Leia `_contexto.md` (segmentos), evidências existentes e as hipóteses do PM.
2. Monte um roteiro de 30–45 min: abertura e consentimento para gravar/transcrever, contexto do entrevistado, perguntas abertas sobre comportamento passado ("conte a última vez que…"), aprofundamento, fechamento.
3. Evite perguntas indutivas e hipotéticas ("você usaria X?"). Para cada hipótese, indique quais perguntas a testam.
4. Salve em `Evidencias/roteiros/<assunto>.md`.

## /entrevista (depois)

Entrada: transcrição (ou notas e desenho, se não foi gravada) colocada em `00-Inbox/_entrada/`, e o perfil do entrevistado.

1. **Sensibilidade:** remova dados pessoais. Identifique o entrevistado por segmento e cargo genérico, não por nome, salvo se o PM pedir.
2. **Extraia itens atômicos:** uma necessidade, dor, pedido, elogio ou dúvida por item. Para cada um, crie uma nota em `Evidencias/` com o modelo `_modelo-evidencia.md` (`origem: entrevista`) e uma citação curta como evidência.
3. **Separe fato de interpretação:** o que o usuário disse ou fez x o que você infere. Inferências vão marcadas.
4. **Ligue** a evidências parecidas e a itens do roadmap.
5. **Resumo da entrevista** em `Evidencias/entrevistas/AAAA-MM-DD <segmento>.md`: perfil, principais achados, hipóteses confirmadas ou refutadas, surpresas.
6. Mova a transcrição para `00-Inbox/_processado/`.

## /entrevista sintese

1. Leia todas as evidências do tema (ou do período pedido).
2. Agrupe por tema de necessidade, com contagem de ocorrências e de segmentos distintos.
3. Aponte padrões fortes (várias fontes, vários segmentos) e sinais fracos (uma fonte).
4. Sugira implicações para roadmap e PRDs, marcadas como sugestão.
5. Salve em `Evidencias/sintese-AAAA-MM-DD.md`. Alerta: síntese generaliza; cada padrão mantém os links para as evidências.
