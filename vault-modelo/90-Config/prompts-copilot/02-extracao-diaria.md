# Prompt 02 · Extração diária (fim do dia)

**Quando:** 18h, antes do `/fechar-dia`.
**Como:** use a versão gerada pelo `/abrir-dia` em `00-Inbox/prompt-extracao-hoje.md`, que já vem com os gatilhos dos seus temas. Este arquivo é o modelo; `{{GATILHOS}}` é substituído automaticamente.

## Primeira passada

```text
Liste TODAS as reuniões de que participei hoje, inclusive as que não estavam na agenda de manhã.

Comece com: "Encontrei N reuniões. Com transcrição: X. Sem transcrição: Y (liste os títulos)."

Para cada reunião COM transcrição, neste formato:

### HH:MM · Título
- Decisões: cada decisão + quem decidiu + trecho curto da transcrição + horário aproximado
- Tarefas minhas ou que dependem de mim: tarefa + prazo, se citado + trecho + horário
- Tarefas de outras pessoas que me afetam: pessoa + tarefa + trecho
- Menções a estes assuntos (mesmo de passagem): {{GATILHOS}}
  Para cada menção: assunto + o que foi dito + trecho + horário
- Necessidades ou reclamações de usuários citadas: necessidade + quem trouxe + trecho
- Pontos sem conclusão ou com discordância: ponto + posições + trecho

Regras:
- NÃO resuma e NÃO agrupe. Prefiro uma lista longa a perder algo.
- Se um campo não tiver nada, escreva "nenhum".
- Trechos com no máximo 2 frases, copiados da transcrição.
- Se uma reunião não tiver transcrição, apenas liste o título e escreva "sem transcrição".
```

## Segunda passada (mande logo depois da resposta)

```text
Revise as transcrições de hoje de novo, do começo ao fim.
Que assuntos, decisões, tarefas ou menções foram ditos e NÃO entraram na sua lista anterior?
Liste só o que faltou, no mesmo formato. Se nada faltou, responda "nada faltou" e diga quantas transcrições você releu.
```

## Pergunta avulsa (quando uma palavra-chave sua não aparecer)

```text
Na reunião "{{título}}" de hoje, o que foi dito sobre "{{palavra-chave}}"? Traga os trechos exatos com horário.
```
