<%*
const titulo = await tp.system.prompt("Título da reunião");
const tipo = await tp.system.suggester(
  ["Gravada", "Ritual do time", "Não gravada", "Entrevista"],
  ["gravada", "ritual", "nao-gravada", "entrevista"]
);
const tema = await tp.system.prompt("Tema (slug, ex.: mcp)", "mcp");
-%>
### <% tp.date.now("HH:mm") %> · <% titulo %>
#tema/<% tema %> #reuniao/<% tipo %> #reuniao/surgiu-no-dia

**Palavras-chave:** 

**Desenho:** 

**Registro:** 
