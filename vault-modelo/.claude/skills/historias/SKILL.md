---
name: historias
description: Quebra um PRD em épico, histórias com critérios de aceite e sugestão de tasks, autoavaliando cada história contra a rubrica do sistema interno de backlog para chegar com nota alta. Use antes do refino ou quando o PM digitar /historias.
---

# /historias

Argumento: o PRD (nome ou link). Ex.: `/historias exportação de relatórios`.

## Entrada

- O PRD em `PRDs/` (idealmente `status: validado`; se estiver em rascunho, avise e siga).
- Rubrica: `90-Config/rubrica-historias.md`. Se `configurada: não`, use os critérios genéricos e diga que a nota não pode ser estimada até rodar `/configurar-rubrica`.
- Caixogramas e evidências citados no PRD.
- Retrato mais recente do board (para não duplicar itens existentes).

## Passos

1. **Épico:** título, objetivo (do PRD), KR ligado, critério de conclusão do épico.
2. **Histórias:** fatie por valor para o usuário (fluxo, perfil, regra de negócio), não por camada técnica. Formato padrão, salvo se a rubrica exigir outro:
   - Título curto e orientado a resultado.
   - "Como <perfil>, quero <capacidade>, para <valor>."
   - Contexto e link para o requisito do PRD (`RQ-xx`) e para a evidência.
   - Critérios de aceite em Dado/Quando/Então, incluindo o caminho de erro e os requisitos derivados dos princípios do tema.
   - Fora de escopo da história.
   - Dependências.
3. **Tasks sugeridas:** quando fizer sentido, sugestão de quebra. Marque como "sugestão, validar com tech lead".
4. **Autoavaliação:** para cada história, aplique cada critério da rubrica, dê a nota estimada e corrija o que estiver abaixo do esperado. Repita até a nota estimada atingir o alvo da rubrica ou até 2 rodadas. Mostre a nota final e o que ainda puxa para baixo.
5. **Duplicidade:** compare com os itens do board. Se já existir algo parecido, aponte.
6. **Salve** em `02-Temas/<Tema>/Historias/<épico>.md` (`tipo: historias`, `status: rascunho`), uma seção por história.
7. **Formato de saída para a ferramenta:** se a rubrica ou o `config.md` indicar formato de importação (CSV ou campos), gere também o arquivo pronto. Com `backlog.modo: mcp` e pedido explícito do PM, crie os itens pelo MCP; caso contrário, nunca crie.

## Saída no chat

Tabela: história, nota estimada, ponto de atenção. E as perguntas em aberto que devem ir para o refino.
