# Prompt 01 · Lista de reuniões do dia

**Quando:** 8h40, antes do `/abrir-dia`.
**Como:** cole no Copilot (M365 Chat), copie a resposta e cole depois de `/abrir-dia` no Claude Code.

```text
Liste TODAS as reuniões da minha agenda de hoje, incluindo as que eu ainda não aceitei.

Comece a resposta com a linha: "Encontrei N reuniões."

Depois, uma linha por reunião, em ordem de horário, exatamente neste formato:
HH:MM-HH:MM | Título | Organizador | Participantes principais (até 5) | Gravada ou transcrita? (sim/não/não sei) | Documentos anexados (nomes ou "nenhum") | Pauta em uma frase (ou "sem pauta")

Não resuma nem agrupe. Não omita reuniões recorrentes, curtas ou bloqueios com participantes.
Se houver conflito de horário, marque as duas com "CONFLITO".
```

**Se o número não bater com sua agenda:** peça de novo dividindo em "reuniões das 9h às 13h" e "das 13h às 18h".
