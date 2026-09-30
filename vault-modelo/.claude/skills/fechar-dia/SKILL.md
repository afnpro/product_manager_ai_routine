---
name: fechar-dia
description: Fecha o dia do PM cruzando a extração do Copilot com palavras-chave e desenhos do Excalidraw, gerando decisões, pendências, follow-ups, necessidades e até 3 itens para revisar. Use às 18h ou quando o PM digitar /fechar-dia.
---

# /fechar-dia

Objetivo: em 20 minutos (contando o Copilot), transformar o dia em registro confiável e deixar o amanhã claro.

## Entrada

- A extração do Copilot colada pelo PM (prompt do dia em `00-Inbox/prompt-extracao-hoje.md`) e a resposta da segunda passada. Se ele colar só a primeira, lembre da segunda passada antes de seguir.
- A nota de hoje em `01-Diario/`.
- Todos os desenhos `.excalidraw.md` incorporados na nota de hoje ou modificados hoje.
- `_contexto.md` dos temas envolvidos; `Principios/` e `Historico/decisoes.md` para checar contradições.

## Passos

1. **Completude:** compare as reuniões da extração com as seções da nota.
   - Reunião na extração sem seção → crie a seção com `#reuniao/surgiu-no-dia`.
   - Seção sem reunião na extração → pergunte ao PM se aconteceu. Se não, marque `#reuniao/cancelada`.
   - Seção criada pelo atalho do Templater (já com `surgiu-no-dia`) → associe pelo horário e título.
   - Reunião sem transcrição → marque para o PM escrever 2 ou 3 linhas no campo "Registro".
2. **Âncoras:** para cada palavra-chave anotada pelo PM, confirme se aparece na extração. Se não aparecer, crie `- [ ] #revisar baixa confiança: "<palavra>" não está na extração da reunião X` e sugira a pergunta ao Copilot.
3. **Desenhos:** leia as caixas de texto de cada desenho (seção `## Text Elements`; descomprima o JSON se preciso para ver as setas). Extraia os marcadores `D:`, `?`, `!`, `→`, `N:`. Se o desenho e a transcrição divergirem, registre `#revisar conflito entre fontes`.
4. **Consolide na nota**, nas subseções do "Fechamento", cada item com link para a fonte:
   - **Decisões do dia** (com quem decidiu). Se contradizer uma decisão anterior ou um princípio validado → `#revisar contradiz decisão anterior`.
   - **Pendências** do PM, como tarefas `- [ ]` com prazo quando houver.
   - **Follow-ups:** rascunhos curtos de mensagem para cada pessoa que precisa de retorno (não envie).
   - **Necessidades de usuários:** crie uma nota em `02-Temas/<Tema>/Evidencias/` para cada necessidade nova (modelo `_modelo-evidencia.md`, `origem: reuniao`) e liste os links aqui.
5. **Decisões nos temas:** acrescente cada decisão em `02-Temas/<Tema>/Historico/decisoes.md` (data · decisão · quem · fonte). Crie o arquivo se não existir.
6. **Reflexão:** se as três perguntas e a nota de energia estiverem vazias, faça as perguntas ao PM no chat, uma de cada vez, e registre as respostas. Não invente.
7. **Contadores:** atualize `reunioes_surgidas` e `reunioes_canceladas` no frontmatter.
8. **Para revisar hoje:** escolha no máximo 3 itens `#revisar`, os de maior impacto (compromissos com outras pessoas primeiro). O resto fica na fila "A revisar".
9. **Amanhã:** sugira a resposta para "O que amanhã precisa de mim?" a partir das pendências com prazo e reuniões de amanhã que exigem preparo.

## Saída no chat

- Resumo em 5 linhas: decisões, pendências, follow-ups, necessidades novas, reuniões surgidas.
- Os até 3 itens para revisar hoje.
- Lembrete gentil de desligar.
