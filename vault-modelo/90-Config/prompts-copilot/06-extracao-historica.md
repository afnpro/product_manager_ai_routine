# Prompt 06 · Extração histórica (para o /importar)

**Quando:** na semana de largada e depois, aos poucos, para trazer o histórico de um tema.
**Como:** um mês por vez, do mais recente para o mais antigo. Salve cada resposta em `00-Inbox/_entrada/copilot-<tema>-AAAA-MM.md` e rode `/importar <tema>`.

## Por mês

```text
Considere todas as reuniões de que participei em {{mês/ano}} sobre {{tema}} (assuntos relacionados: {{palavras do glossário e gatilhos}}).

Comece com: "Encontrei N reuniões sobre o tema em {{mês/ano}}. Com transcrição: X."

Para cada reunião, em ordem de data:

### AAAA-MM-DD · Título
- Participantes principais
- Decisões (quem decidiu + trecho curto)
- Mudanças de rumo em relação a decisões anteriores
- Necessidades ou problemas de usuários citados (trecho curto)
- Riscos, incidentes, preocupações de governança ou segurança
- Pendências que ficaram em aberto
- Documentos ou apresentações citados (nomes)

Não resuma nem agrupe reuniões. Se uma reunião não tiver transcrição, liste só título, data e participantes.
Ignore 1:1s e reuniões sobre pessoas, avaliações ou RH.
```

## Se o Copilot cortar a resposta

```text
Continue a lista a partir da reunião "{{última reunião listada}}", no mesmo formato.
```

Se ainda assim cortar, peça por quinzena.
