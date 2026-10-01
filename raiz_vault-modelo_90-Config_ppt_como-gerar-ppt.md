# Como gerar PPT neste vault (instruções para o Claude Code)

Todos os comandos que geram apresentação seguem estas regras.

## Pré-requisitos

- `python-pptx` instalado (`pip install python-pptx`).
- Template da empresa nesta pasta e `mapa-layouts.md` gerado por `/configurar-template`.
- Sem mapa: avise o PM, gere com o layout padrão do python-pptx e marque `#revisar` com o motivo.

## Processo

1. **Conteúdo primeiro, slides depois.** Escreva o roteiro em markdown na pasta `Artefatos/` do tema (`tipo: ppt`, `status: rascunho`): um bloco por slide com título, mensagem principal (uma frase), conteúdo e nota do apresentador.
2. **Uma ideia por slide.** O título do slide é a conclusão ("Adoção cresceu 18% em outubro"), não o assunto ("Adoção").
3. **Abra o template** com `Presentation("<template>")`, remova os slides de exemplo que ele tiver e crie os novos usando os layouts indicados no `mapa-layouts.md` (pelo nome do layout, nunca pelo índice).
4. **Preencha os placeholders** do layout (título, corpo, imagem). Não desenhe caixas soltas por cima do template, salvo quando o mapa indicar.
5. **Números** só da fonte, com a fonte no rodapé do slide ou na nota do apresentador.
6. **Gráficos:** use gráfico nativo do PowerPoint (`chart_data`) com os dados da fonte, para que o PM possa editar.
7. **Notas do apresentador** em todo slide: o que falar em 2 ou 3 frases.
8. **Salve** em `02-Temas/<Tema>/Artefatos/<nome>-AAAA-MM-DD.pptx`.
9. **Confira:** reabra o arquivo, conte os slides, verifique se nenhum placeholder ficou vazio ou com texto de exemplo e se nenhum texto passou de 6 linhas. Se conseguir renderizar (LibreOffice), olhe as imagens.

## Limites

- Máximo de 12 slides para status e 20 para demo, salvo pedido do PM.
- O PM sempre revisa no PowerPoint antes de apresentar. Diga isso no fim.
