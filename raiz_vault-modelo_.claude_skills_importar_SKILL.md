---
name: importar
description: Importa o histórico de um tema (transcrições, extrações do Copilot, desenhos Excalidraw, apresentações, documentos e PDFs) em lotes, gerando linha do tempo, log de decisões, princípios candidatos, evidências e contexto preenchido, sem duplicar e filtrando conteúdo sensível. Use quando o PM digitar /importar.
---

# /importar

Argumentos: tema e, opcionalmente, o lote. Ex.: `/importar mcp`, `/importar mcp desenhos`.

Tudo roda localmente. Nada é enviado para fora do computador do PM.

## Controle

- **Manifesto:** `02-Temas/<Tema>/Historico/_importados.md`, uma linha por arquivo: caminho original, hash (sha1), data do conteúdo, data da importação, o que foi gerado. Antes de processar um arquivo, confira o hash: se já foi importado, pule. Assim o comando pode rodar várias vezes.
- **Lotes:** processe até 20 arquivos por vez, do mais recente para o mais antigo. No fim de cada lote, informe o progresso e continue se o PM tiver pedido processamento completo.
- **Originais:** depois de processados, mova de `00-Inbox/_entrada/` para `00-Inbox/_processado/AAAA-MM-DD/`. Desenhos já no vault não se movem.

## Conversão por tipo

| Tipo | Como ler |
| --- | --- |
| `.vtt`, `.docx` de transcrição do Teams | Texto com falante e horário; `python-docx` para .docx |
| Extração do Copilot (`.md`/`.txt`) | Já estruturada; use a data do período |
| `.pptx` | `python-pptx`: títulos, textos, notas do apresentador; um bloco por slide |
| `.docx` | `python-docx` ou `pandoc` para markdown |
| `.pdf` | `pdftotext -layout` ou `pypdf`; se não houver texto, avise (OCR opcional) |
| `.excalidraw.md` | Seção `## Text Elements` + JSON. Se `compressed-json`: junte as linhas e descomprima com `lzstring` (`LZString().decompressFromBase64`). Leia setas por `startBinding`/`endBinding` |

Instale o que faltar com `pip install python-pptx python-docx pypdf lzstring`.

## Para cada arquivo

1. **Sensível?** 1:1, avaliação de pessoas, RH, saúde, dados pessoais → não importe o conteúdo. Registre no manifesto como `ignorado: sensível` e liste para o PM.
2. **Nota-resumo** em `Historico/fontes/AAAA-MM-DD <título>.md` (`tipo: fonte-importada`, `status: rascunho`): de onde veio (caminho ou link original, que continua sendo a referência), data, participantes ou autor, resumo em até 10 linhas, e o conteúdo convertido em markdown num bloco recolhível para busca.
3. **Extraia:**
   - Decisões → `Historico/decisoes.md` (data · decisão · quem · fonte).
   - Marcos → `Historico/linha-do-tempo.md`.
   - Necessidades de usuários → `Evidencias/` (`origem: importacao`).
   - Termos, sistemas, stakeholders → propostas para `_contexto.md` (acrescente numa seção "Sugestões da importação", não sobrescreva).
   - Pendências antigas ainda sem desfecho → "Pendências históricas" no `_contexto.md`.
4. **Desenhos:** classifique como `diagrama vivo` (arquitetura de um sistema, caixograma recorrente) ou `rascunho de reunião`. Vivos: se não estiverem em `Diagramas/`, sugira mover (não mova sem ok). Associe rascunhos à reunião pela data do arquivo e pelo conteúdo, quando possível.

## Depois de cada lote

1. **Contradições:** se uma decisão nova contradiz uma anterior, mantenha as duas no log com a ordem temporal e marque a mais recente como vigente. Crie `#revisar contradiz decisão anterior` só quando a vigente não for óbvia.
2. **Princípios candidatos:** decisões que se repetem em 3 ou mais fontes viram rascunhos em `Principios/`, com as fontes.
3. **Relatório** em `Historico/importacao-AAAA-MM-DD.md`: arquivos processados, ignorados (e por quê), decisões, evidências, princípios candidatos, contradições, lacunas de período ("nada de março a maio").

## Saída no chat

Progresso, o que precisa de revisão (máximo 5 itens mais importantes) e a sugestão do próximo lote.
