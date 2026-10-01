---
name: status
description: Gera o status report semanal do PM por público (gestor, diretoria, time) a partir das notas, roadmap, OKRs e métricas, em markdown e PPT no template da empresa. Use na sexta ou quando o PM digitar /status.
---

# /status

Argumentos opcionais: tema e público. Ex.: `/status mcp diretoria`. Sem argumentos: todos os temas ativos, versão gestor.

## Entrada

- Revisão semanal mais recente (`01-Diario/Semanas/`) ou, se não houver, as notas diárias da semana.
- `Roadmap.md`, `OKRs/` (check-ins), `Metricas/Relatorios/` e `Historico/decisoes.md` do tema.
- Status anterior em `Artefatos/status-*.md`, para mostrar o que mudou.

## Estrutura fixa (igual toda semana)

1. **Resumo em uma frase** por frente.
2. **Semáforo por frente do roadmap (mês atual):** verde, amarelo ou vermelho, com uma justificativa baseada em fato. **Você sugere; o PM decide.** Na dúvida entre duas cores, sugira a pior e explique.
3. **O que mudou desde o último status.**
4. **Entregas da semana.**
5. **Decisões relevantes** (as que o público precisa saber).
6. **Riscos e bloqueios**, com o que precisa do público (decisão, apoio, recurso).
7. **OKRs:** confiança atual de cada KR (dos check-ins).
8. **Próximas duas semanas.**

## Por público

| Público | Foco | Tamanho |
| --- | --- | --- |
| gestor | Tudo, com detalhes de riscos e pedidos de apoio | 1 página |
| diretoria | Semáforo, OKRs, riscos que pedem decisão | meia página, 3 a 5 slides |
| time | Entregas, decisões, próximas prioridades, reconhecimento | 1 página |

## Saída

- `02-Temas/<Tema>/Artefatos/status-AAAA-MM-DD.md` (`tipo: status`, `status: rascunho`).
- Se o PM pedir PPT (ou público = diretoria): siga `90-Config/ppt/como-gerar-ppt.md`. Um slide de capa, um de semáforo, um de OKRs, um de riscos e pedidos, um de próximos passos.
- No chat: o semáforo sugerido com justificativas, para o PM confirmar ou mudar antes de você finalizar.

## Regras

- Nunca pinte verde sem evidência. "Sem notícia" é amarelo.
- Todo número com fonte. Sem fonte: `[FALTA: …]`.
