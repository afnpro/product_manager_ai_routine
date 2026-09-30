---
name: comunicado
description: Redige a newsletter semanal do produto na voz do PM e gera o JSON com um Adaptive Card por segmento para o Power Automate disparar após aprovação. Use na sexta ou quando o PM digitar /comunicado.
---

# /comunicado

Objetivo: o PM só revisa e aprova. Você nunca dispara nada.

## Entrada

- Tema (argumento ou o único tema ativo).
- Entregas e decisões da semana (revisão semanal, `Historico/decisoes.md`, `Entregas/`).
- `Roadmap.md` (seção mês atual e próximo mês, para "o que vem a seguir").
- `Evidencias/` recentes (dúvidas recorrentes viram dica; casos de uso viram "caso real").
- Exemplos de tom em `04-Comunicacao/Exemplos/` e o último comunicado enviado, para não repetir.
- `_contexto.md` → segmentos e o que importa para cada um.
- Template `04-Comunicacao/card-template.json` e `config.md` (links de feedback, documentação e canal).

## Passos

1. **Escolha o conteúdo** (uma coisa de cada, a mais relevante):
   - **Destaque:** entrega ou mudança que afeta o usuário. Nada interno.
   - **Dica da semana:** a partir de dúvidas recorrentes.
   - **Caso real:** um time usando o produto (só com fonte; se não houver, omita o bloco).
   - **Próximos passos:** até 3 itens do mês atual ou próximo, sem prometer data que não esteja no roadmap.
2. **Por segmento** (`geral`, `consome`, `publica`, `seguranca`): mesma estrutura, mas o destaque e a dica mudam para o que importa ao segmento. Se um segmento não tiver nada específico, use o conteúdo geral.
3. **Linha pessoal no topo**, na voz do PM (imite os exemplos): uma frase, primeira pessoa, sem exagero.
4. **Rascunho legível** em `04-Comunicacao/Comunicados/AAAA-MM-DD.md` (`tipo: comunicado`, `status: rascunho`), com o texto de cada segmento e as fontes de cada afirmação.
5. **Mostre o rascunho ao PM e espere o ok ou os ajustes.** Só depois disso gere o JSON.
6. **Gere o JSON** preenchendo `card-template.json` uma vez por segmento. Substitua todos os `{{…}}`. Blocos sem conteúdo (ex.: caso real) devem ser removidos do card, não deixados vazios. Envelope:

   ```json
   {
     "edicao": 1,
     "data": "AAAA-MM-DD",
     "tema": "MCP",
     "assunto": "Resumo em até 8 palavras",
     "cards": { "geral": {}, "consome": {}, "publica": {}, "seguranca": {} }
   }
   ```

7. **Valide:** JSON válido (rode `python -m json.tool`), `"version": "1.4"` em cada card, nenhum `{{` restante, textos sem markdown não suportado (Adaptive Cards aceitam **negrito**, _itálico_, listas e links simples).
8. **Salve** o JSON em `04-Comunicacao/Comunicados/AAAA-MM-DD.json`. Diga ao PM para copiar esse arquivo para a pasta do OneDrive monitorada pelo fluxo (`pasta_onedrive_comunicados` em `config.md`), ou copie você mesmo se a pasta for sincronizada e o PM pedir.

## Quando o PM corrigir o texto

Salve a versão final aprovada em `04-Comunicacao/Exemplos/` para melhorar o tom das próximas.

## Edição especial da demo

Com o argumento `demo`, use `Entregas/AAAA-MM.md` do mês: destaque = as 3 entregas mais relevantes, link para a gravação da demo, próximos passos do novo mês atual.
