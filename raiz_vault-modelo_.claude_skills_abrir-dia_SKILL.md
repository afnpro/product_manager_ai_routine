---
name: abrir-dia
description: Monta a nota diária do PM a partir da lista de reuniões do Copilot e gera o prompt de extração do dia com os gatilhos dos temas ativos. Use no arranque da manhã ou quando o PM digitar /abrir-dia.
---

# /abrir-dia

Objetivo: em até 2 minutos, deixar a nota do dia pronta, com uma seção por reunião e as prioridades.

## Entrada

- A lista de reuniões que o PM colar depois do comando (resposta do prompt `90-Config/prompts-copilot/01-lista-reunioes.md`). Se ele não colar, peça.
- `90-Config/config.md`, `90-Config/convencoes.md`, `_contexto.md` de cada tema ativo.
- Nota do dia anterior útil (`01-Diario/`), seção "O que amanhã precisa de mim?" e pendências abertas.

## Passos

1. **Cheque a completude:** a lista do Copilot começa com "Encontrei N reuniões". Conte as linhas. Se não bater, avise e sugira pedir de novo dividindo em manhã e tarde.
2. **Crie `01-Diario/AAAA-MM-DD.md`** a partir de `99-Templates/nota-diaria.md` (substitua as expressões do Templater pelos valores reais). Se a nota já existir, só acrescente o que falta, nunca sobrescreva.
3. **Para cada reunião**, insira uma seção no formato de `99-Templates/secao-reuniao.md`, em ordem de horário:
   - **Tema:** sugira pelo título, organizador e participantes, comparando com glossário e stakeholders de cada `_contexto.md`. Na dúvida, use `#tema/indefinido`.
   - **Tipo:** `ritual` para daily, refino, retro, planning, demo; `entrevista` se o título indicar; `gravada` se o Copilot disser que tem transcrição; senão `nao-gravada`.
   - **Gatilhos a observar:** só os gatilhos do tema que o título ou a pauta sugerem. Não liste todos.
   - **Preparo:** documentos anexados ao convite e pendências suas ligadas a essa reunião ou pessoa.
   - Mantenha os campos de compromissos e bloqueios só nos rituais, e o campo de registro só nas não gravadas.
4. **Prioridades:** sugira até 3 a partir de "O que amanhã precisa de mim?" de ontem e das pendências com prazo. O PM confirma.
5. **Marque as reuniões que exigem preparo** com `⚑` no título da seção.
6. **Gere o prompt de extração do dia:** copie `90-Config/prompts-copilot/02-extracao-diaria.md` e substitua `{{GATILHOS}}` pela união dos gatilhos de todos os temas ativos. Mostre esse prompt no final, pronto para copiar, e salve em `00-Inbox/prompt-extracao-hoje.md`.
7. Atualize o frontmatter `reunioes_planejadas` com o total.

## Saída no chat (curta)

- Nota criada ou atualizada, número de reuniões, quais pedem preparo.
- As 3 prioridades sugeridas.
- Se houver daily hoje: lembrete de salvar o print do board e rodar `/daily`.
- O prompt de extração do dia, em bloco de código.
