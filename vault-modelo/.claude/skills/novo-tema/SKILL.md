---
name: novo-tema
description: Cria a pasta de um tema novo a partir do modelo e entrevista o PM para preencher o contexto (objetivo, públicos, gatilhos, glossário, sistemas, stakeholders, rituais); também arquiva um tema encerrado. Use ao assumir ou revisar um tema, ou quando o PM digitar /novo-tema.
---

# /novo-tema

Argumentos: nome do tema. `/novo-tema arquivar <tema>` arquiva.

## Criar ou revisar

1. Se `02-Temas/<Tema>/` não existir, copie `02-Temas/_modelo-tema/` para lá. Se existir (por exemplo, criado pelo `/importar`), entre em modo revisão.
2. **Modo revisão:** mostre o que já está preenchido no `_contexto.md` e pergunte só o que falta ou está em dúvida.
3. **Entrevista** (uma pergunta por vez, no máximo 10 no total, pule o que já souber):
   1. Em duas frases, por que este produto existe e para quem?
   2. Quais são os públicos e o que cada um mais valoriza?
   3. Que assuntos, se aparecerem numa reunião, você precisa saber? (gatilhos)
   4. Que termos e siglas alguém novo não entenderia?
   5. Quais sistemas compõem o produto e onde estão os caixogramas?
   6. Quem são os stakeholders e o que cada um quer?
   7. Quais rituais existem, quem é owner e o que é transcrito?
   8. Qual é a métrica que melhor mostra que o produto entrega valor?
   9. Que decisões ou regras todo mundo deveria seguir sem perguntar a você? (candidatos a princípio)
   10. O que está em aberto hoje e te preocupa?
4. Preencha `_contexto.md` (`status: rascunho`). Candidatos a princípio viram rascunhos em `Principios/`.
5. Acrescente o tema em "Temas ativos" no `config.md`.
6. Sugira os próximos passos: `/okr`, `/roadmap`, `/metricas definir`.

## Arquivar

1. Mova `02-Temas/<Tema>/` para `02-Temas/_arquivo/<Tema>/`.
2. Tire o tema de "Temas ativos" no `config.md`.
3. Crie `_encerramento.md` na pasta arquivada: período, principais decisões, estado do roadmap, pendências passadas a quem (pergunte ao PM).
