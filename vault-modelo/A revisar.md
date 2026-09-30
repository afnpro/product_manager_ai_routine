# A revisar

Tudo o que a IA gerou e ainda espera seu olho. Ao revisar uma nota, troque `status: rascunho` por `status: validado`. Ao resolver um item pontual, marque a tarefa.

## Sempre revisar (sai para outras pessoas ou vira compromisso)

```dataview
TABLE tipo, tema, gerado_por AS "Comando", gerado_em AS "Gerado em"
FROM "02-Temas" OR "04-Comunicacao"
WHERE status = "rascunho" AND contains(list("status","comunicado","historias","prd","okr","roadmap","principio","ppt","demo","metricas-definicao","dashboard-spec","rubrica"), tipo)
SORT gerado_em ASC
```

## Itens sinalizados

```dataview
TASK
FROM ""
WHERE contains(tags, "#revisar") AND !completed
GROUP BY file.link
```

## Outros rascunhos

```dataview
TABLE tipo, tema, gerado_em AS "Gerado em"
FROM ""
WHERE status = "rascunho" AND !contains(list("status","comunicado","historias","prd","okr","roadmap","principio","ppt","demo","metricas-definicao","dashboard-spec","rubrica"), tipo)
SORT gerado_em DESC
LIMIT 30
```
