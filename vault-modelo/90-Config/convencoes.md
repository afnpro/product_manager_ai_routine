---
tipo: config
---

# Convenções

Linguagem comum entre você, a IA e (se compartilhar o kit) outros PMs.

## Marcadores

Use no início de uma caixa de texto do Excalidraw ou de uma linha da nota.

| Marcador | Significa | Exemplo |
| --- | --- | --- |
| `D:` | Decisão | `D: todo server novo passa pelo gateway` |
| `?` | Dúvida, algo a confirmar | `? quem aprova servers externos` |
| `!` | Risco de governança | `! server X acessa dado sensível sem auth` |
| `→` | Ação com responsável | `→ Ana: revisar escopo OAuth` |
| `N:` | Necessidade de usuário | `N: times querem testar server antes de publicar` |

O que não tiver marcador também é lido, com menos confiança.

## Etiquetas

- Tema: `#tema/mcp` (o slug é o nome da pasta em minúsculas, sem acento)
- Tipo de reunião: `#reuniao/gravada`, `#reuniao/ritual`, `#reuniao/nao-gravada`, `#reuniao/entrevista`
- Marcadas pelo fechamento: `#reuniao/surgiu-no-dia`, `#reuniao/cancelada`
- Revisão: `#revisar`

## Status das notas

- `status: rascunho` → gerado pela IA, ainda não revisado (aparece em "A revisar")
- `status: validado` → revisado por você
- `status: arquivado` → não vale mais, mantido como histórico

## Desenhos

- **Rascunho de reunião:** criado dentro da seção da reunião (comando do Excalidraw que cria um desenho novo incorporado na nota ativa). Nome sugerido: `AAAA-MM-DD <reunião>`.
- **Diagrama vivo (caixograma):** um arquivo por sistema em `02-Temas/<Tema>/Diagramas/`. Use frames com data para marcar o que entrou quando. A nota do dia só aponta para ele quando você o altera.
- Links dentro do desenho (`[[nota]]`) criam o caminho de volta.

## Nomes de arquivo

- Nota diária: `01-Diario/AAAA-MM-DD.md`
- Retrato do board: `03-Backlog/Retratos/AAAA-MM-DD.md`
- Status: `02-Temas/<Tema>/Artefatos/status-AAAA-MM-DD.md` (+ `.pptx`)
- Demo: `02-Temas/<Tema>/Entregas/AAAA-MM.md` e `Artefatos/demo-AAAA-MM.pptx`
- Comunicado: `04-Comunicacao/Comunicados/AAAA-MM-DD.md` e `.json`
- Princípio: `02-Temas/<Tema>/Principios/P-NNN <título curto>.md`
- Evidência: `02-Temas/<Tema>/Evidencias/E-AAAA-MM-DD <título curto>.md`
