---
name: ppt
description: Gera uma apresentação avulsa no template da empresa a partir de qualquer nota ou conjunto de notas do vault. Use quando o PM pedir um PPT, uma apresentação ou slides sobre um assunto, ou digitar /ppt.
---

# /ppt

Argumento: assunto, público e duração. Ex.: `/ppt proposta de nova política de acesso para a diretoria, 15 min`.

## Passos

1. **Entenda o objetivo:** o que o público deve decidir, entender ou fazer ao final? Se não estiver claro, pergunte (uma pergunta).
2. **Reúna o material** no vault: notas, PRDs, caixogramas, evidências, métricas, decisões. Liste as fontes.
3. **Escreva o roteiro** em markdown (`Artefatos/ppt-<assunto>-AAAA-MM-DD.md`, `tipo: ppt`): sequência de slides com título-conclusão, mensagem, conteúdo e nota do apresentador. Regra prática: 1 slide a cada 1,5–2 minutos.
4. **Mostre o roteiro ao PM** e ajuste antes de gerar o arquivo.
5. **Gere o .pptx** seguindo `90-Config/ppt/como-gerar-ppt.md`.
6. Caixogramas: descreva a ideia central no slide e, se o PM quiser o desenho, exporte o PNG do Excalidraw e insira como imagem.

## Estruturas úteis

- **Pedir decisão:** contexto → problema → opções com prós e contras → recomendação → o que precisamos de vocês.
- **Atualizar:** resumo → o que mudou → riscos → próximos passos.
- **Apresentar proposta:** problema com evidência → objetivo → proposta → impacto esperado → plano.
