---
name: configurar-template
description: Lê o arquivo de apresentação da empresa em 90-Config/ppt e gera o mapa de layouts que todos os comandos usam para criar PPTs no padrão corporativo. Use uma vez na instalação, ao trocar o template, ou quando o PM digitar /configurar-template.
---

# /configurar-template

## Passos

1. Encontre o único `.pptx` ou `.potx` em `90-Config/ppt/`. Nenhum ou mais de um: peça ao PM para deixar só um. `.potx`: abra com python-pptx (se falhar, peça para salvar como .pptx).
2. Liste os **layouts do slide master**: nome, índice, e os placeholders de cada um (tipo, `idx`, nome, posição e tamanho).
3. Liste os **slides de exemplo** que o arquivo já tem, com o layout de cada um. Eles mostram como a empresa usa o template.
4. Mapeie cada papel para um layout, pelo nome:

   | Papel | Uso |
   | --- | --- |
   | capa | Título e subtítulo da apresentação |
   | secao | Divisor de seção |
   | conteudo | Título + texto ou tópicos |
   | duas_colunas | Comparação, antes e depois |
   | grafico | Título + área grande para gráfico |
   | tabela | Título + tabela |
   | imagem | Título + imagem grande (caixograma, print) |
   | destaque | Um número ou frase em destaque |
   | encerramento | Obrigado, contatos, próximos passos |

   Se um papel não tiver layout adequado, indique o substituto e o que ajustar.
5. Extraia as **cores do tema** e as **fontes** para que gráficos nativos usem a paleta da empresa.
6. Anote **regras visíveis** nos exemplos: limite de tópicos, uso de rodapé, posição do logo.
7. Gere uma **apresentação de teste** `90-Config/ppt/teste-template.pptx` com um slide de cada papel, preenchido com texto de exemplo, e confira reabrindo o arquivo (sem placeholder vazio). Se houver LibreOffice, renderize em imagem e olhe.
8. Salve `90-Config/ppt/mapa-layouts.md` (`tipo: config`, `status: rascunho`) com o mapeamento, as cores, as fontes, as regras e o caminho do template. Peça ao PM para abrir o teste no PowerPoint e confirmar.
