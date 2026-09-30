# Prompts do Copilot

São 7 prompts, prontos para copiar e colar no Copilot M365 Chat. Troque o que estiver entre `{{ }}`. Todos começam com uma checagem de completude: se o número não bater com sua agenda, peça de novo por período.

| # | Prompt | Quando | Resposta vai para |
| --- | --- | --- | --- |
| 1 | Lista de reuniões | Todo dia, 8h40 | `/abrir-dia` |
| 2 | Extração diária + segunda passada | Todo dia, 18h | `/fechar-dia` |
| 3 | Daily | Depois da daily ou no fechamento | Seção da daily na nota |
| 4 | Revisão de documento | Ao receber documento para opinar | Nota do dia ou PRD |
| 5 | Respostas ao comunicado | Segunda de manhã | Evidências |
| 6 | Extração histórica | Largada, mês a mês | `/importar` |
| 7 | Busca de documentos | Largada | `/importar` |

## 1. Lista de reuniões do dia

Cole a resposta logo depois de digitar `/abrir-dia` no Claude Code.

```text
Liste TODAS as reuniões da minha agenda de hoje, incluindo as que eu ainda não aceitei.

Comece a resposta com a linha: "Encontrei N reuniões."

Depois, uma linha por reunião, em ordem de horário, exatamente neste formato:
HH:MM-HH:MM | Título | Organizador | Participantes principais (até 5) | Gravada ou transcrita? (sim/não/não sei) | Documentos anexados (nomes ou "nenhum") | Pauta em uma frase (ou "sem pauta")

Não resuma nem agrupe. Não omita reuniões recorrentes, curtas ou bloqueios com participantes.
Se houver conflito de horário, marque as duas com "CONFLITO".
```

## 2. Extração diária (fim do dia)

O `/abrir-dia` gera esta versão todo dia com os gatilhos atuais dos seus temas, em `00-Inbox/prompt-extracao-hoje.md`. Abaixo, a versão já preenchida com os gatilhos do MCP, para usar desde já. Cole a resposta das duas passadas depois de `/fechar-dia`.

**Primeira passada**

```text
Liste TODAS as reuniões de que participei hoje, inclusive as que não estavam na agenda de manhã.

Comece com: "Encontrei N reuniões. Com transcrição: X. Sem transcrição: Y (liste os títulos)."

Para cada reunião COM transcrição, neste formato:

### HH:MM · Título
- Decisões: cada decisão + quem decidiu + trecho curto da transcrição + horário aproximado
- Tarefas minhas ou que dependem de mim: tarefa + prazo, se citado + trecho + horário
- Tarefas de outras pessoas que me afetam: pessoa + tarefa + trecho
- Menções a estes assuntos (mesmo de passagem): novos MCP servers; permissões ou autenticação; dados sensíveis; prazos do roadmap; mudanças de escopo; incidentes
  Para cada menção: assunto + o que foi dito + trecho + horário
- Necessidades ou reclamações de usuários citadas: necessidade + quem trouxe + trecho
- Pontos sem conclusão ou com discordância: ponto + posições + trecho

Regras:
- NÃO resuma e NÃO agrupe. Prefiro uma lista longa a perder algo.
- Se um campo não tiver nada, escreva "nenhum".
- Trechos com no máximo 2 frases, copiados da transcrição.
- Se uma reunião não tiver transcrição, apenas liste o título e escreva "sem transcrição".
```

**Segunda passada** (mande logo depois da resposta)

```text
Revise as transcrições de hoje de novo, do começo ao fim.
Que assuntos, decisões, tarefas ou menções foram ditos e NÃO entraram na sua lista anterior?
Liste só o que faltou, no mesmo formato. Se nada faltou, responda "nada faltou" e diga quantas transcrições você releu.
```

**Pergunta avulsa** (quando uma palavra-chave sua não aparecer na extração)

```text
Na reunião "{{título}}" de hoje, o que foi dito sobre "{{palavra-chave}}"? Traga os trechos exatos com horário.
```

## 3. Daily

Salve a resposta na seção da daily da nota do dia. O `/daily` do dia seguinte usa os compromissos.

```text
Na daily de hoje ("{{título da daily}}"), liste para cada pessoa que falou:

Pessoa | O que disse que fez | O que disse que vai fazer (compromisso) | Bloqueios ou pedidos de ajuda | Itens do backlog citados (IDs ou nomes)

Depois, liste separadamente:
- Bloqueios sem responsável definido
- Assuntos que alguém pediu para discutir depois da daily

Comece com: "Pessoas que falaram: N." Não resuma: use as palavras de cada pessoa, de forma curta.
```

## 4. Revisão de documento

Use com o documento aberto ou referenciado no Copilot. Para specs do tech lead, a leitura é pela ótica de produto.

```text
Analise o documento "{{nome}}" pela ótica de um Product Manager responsável por uma plataforma de exposição e governança de MCP servers.

Traga, nesta ordem:
1. Decisões que o documento pede de mim, cada uma em uma frase
2. Premissas assumidas, explícitas ou implícitas
3. O que muda em relação ao estado atual do produto
4. Riscos de governança e segurança (permissões, dados sensíveis, autenticação, auditoria, prompt injection, conformidade)
5. Pontos que atendem ou não atendem aos requisitos de produto (se for uma spec técnica)
6. Afirmações técnicas ou números que devo verificar, com a página ou seção
7. Classifique cada decisão como: aprovar / ajustar / discutir, com uma linha de justificativa

Não resuma o documento inteiro. Foque no que exige minha decisão ou atenção.
Cite a seção de origem de cada item.
```

## 5. Respostas ao comunicado

Salve a resposta em `00-Inbox/_entrada/respostas-comunicado-AAAA-MM-DD.md` e peça ao Claude Code: "processe as respostas ao comunicado".

```text
Desde a última sexta-feira, liste TODAS as mensagens que recebi no Teams em resposta ao comunicado "{{assunto do comunicado}}", tanto em chats individuais quanto no canal "{{canal do produto}}".

Comece com: "Encontrei N respostas de M pessoas."

Para cada resposta:
Pessoa | Área ou time (se souber) | Canal (chat ou canal) | Tipo (dúvida, pedido, problema, elogio, sugestão, outro) | O que disse (trecho curto) | Precisa de resposta minha? (sim/não) | Já respondi? (sim/não)

Depois, separadamente:
- Dúvidas que apareceram mais de uma vez
- Problemas relatados (possíveis incidentes)
- Mensagens sem resposta minha há mais de 1 dia útil
```

## 6. Extração histórica (para o /importar)

Um mês por vez, do mais recente para o mais antigo. Salve cada resposta como `00-Inbox/_entrada/copilot-mcp-AAAA-MM.md`.

```text
Considere todas as reuniões de que participei em {{mês/ano}} sobre MCP e a plataforma de exposição e governança de MCP servers (assuntos relacionados: MCP servers, gateway, registro de servers, permissões, autenticação, dados sensíveis, governança de agentes).

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

**Se o Copilot cortar a resposta**

```text
Continue a lista a partir da reunião "{{última reunião listada}}", no mesmo formato.
```

Se ainda assim cortar, peça por quinzena.

## 7. Busca de documentos para importar

Baixe os de relevância alta para `00-Inbox/_entrada/`. O original continua no OneDrive ou SharePoint como referência.

```text
Liste os documentos, apresentações, planilhas e PDFs sobre MCP e a plataforma de exposição e governança de MCP servers que eu criei, editei ou que foram compartilhados comigo nos últimos 6 meses.

Comece com: "Encontrei N arquivos."

Para cada arquivo:
Nome | Tipo | Autor | Última modificação | Onde está (link) | Do que trata em uma frase | Relevância para o histórico do tema (alta, média, baixa)

Ordene por relevância e depois por data. Destaque: arquitetura, PRDs e documentos de produto, apresentações para liderança, decisões de governança, resultados de pesquisa com usuários.
```
