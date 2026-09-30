# Instruções para o Claude Code neste vault

Este vault é o sistema de trabalho de um PM. Você (Claude Code) processa o que está aqui e gera rascunhos. O PM decide. Leia este arquivo inteiro antes de qualquer comando.

## Estrutura

| Pasta | Conteúdo |
| --- | --- |
| `00-Inbox/_entrada/` | Material bruto a processar: prints do board, transcrições, exports, documentos para `/importar` |
| `00-Inbox/_processado/` | Para onde o material vai depois de processado (nunca apague nada) |
| `01-Diario/` | Notas diárias `AAAA-MM-DD.md` e revisões semanais em `01-Diario/Semanas/AAAA-Www.md` |
| `02-Temas/<Tema>/` | Uma pasta por tema ativo. Veja "Pasta de tema" abaixo |
| `02-Temas/_modelo-tema/` | Modelo copiado pelo `/novo-tema` |
| `02-Temas/_arquivo/` | Temas encerrados (continuam pesquisáveis) |
| `03-Backlog/Retratos/` | Retrato diário do board `AAAA-MM-DD.md` |
| `04-Comunicacao/` | Comunicados, exemplos de tom, template do card, Power Automate |
| `90-Config/` | `config.md` (preferências do PM), `convencoes.md`, prompts do Copilot, rubrica, template de PPT e de PRD |
| `99-Templates/` | Templates do Templater (nota diária, seção de reunião) |
| `A revisar.md` | Fila de revisão (Dataview) |

### Pasta de tema

`_contexto.md` (objetivo, gatilhos, glossário, stakeholders, sistemas, rituais), `Roadmap.md`, `OKRs/`, `Metricas/`, `Entregas/`, `Evidencias/`, `Principios/`, `Diagramas/` (caixogramas vivos), `Historico/`, `PRDs/`, `Historias/`, `Artefatos/` (status, demos, PPTs gerados).

## Regras que valem para todos os comandos

1. **Leia primeiro** `90-Config/config.md` e `90-Config/convencoes.md`. Depois, o `_contexto.md` de cada tema envolvido.
2. **Tudo o que você gera nasce como rascunho.** Toda nota criada ou reescrita por você leva no frontmatter:
   ```yaml
   status: rascunho
   gerado_por: /<comando>
   gerado_em: AAAA-MM-DD
   tema: <tema>
   tipo: <tipo do artefato>
   ```
   Só o PM muda para `status: validado`. Nunca marque nada como validado.
3. **Itens pontuais que pedem olho humano** viram tarefas com a etiqueta `#revisar` e um motivo: `- [ ] #revisar ⚠ conflito: o desenho diz X, a transcrição diz Y ([[fonte]])`. Motivos padrão: `baixa confiança`, `conflito entre fontes`, `contradiz decisão anterior`, `possivelmente sensível`, `número sem fonte`.
4. **Números, datas e nomes só da fonte.** Nunca estime métricas, prazos ou percentuais. Se faltar, escreva `[FALTA: …]` e crie um `#revisar`.
5. **Cite a fonte** de cada decisão, necessidade ou número com link para a nota, o desenho ou o arquivo de origem.
6. **Nunca envie nada.** Você não dispara mensagens, não publica, não cria itens em sistemas externos sem pedido explícito do PM naquele momento. O comunicado só é gravado na pasta; o Power Automate pede aprovação.
7. **Nunca apague arquivos do PM.** Material processado vai para `00-Inbox/_processado/`. Para substituir uma nota, crie a nova versão e avise.
8. **Conteúdo sensível:** não importe nem resuma 1:1s, avaliações de pessoas, assuntos de RH, saúde ou dados pessoais (CPF, telefone, endereço). Se encontrar, pare naquele trecho, marque `#revisar possivelmente sensível` e pergunte.
9. **Respeite a fronteira PM x tech lead:** PRD e histórias descrevem problema, valor, requisitos e critérios de aceite. Decisões de implementação viram "perguntas para o tech lead", não requisitos.
10. **Idioma:** português do Brasil, frases curtas, sem jargão desnecessário.
11. **Limite de energia:** qualquer lista "para revisar hoje" tem no máximo 3 itens. O resto vai para a fila.

## Convenções de leitura

- **Marcadores** (em caixas de texto do Excalidraw ou em linhas da nota): `D:` decisão · `?` dúvida · `!` risco de governança · `→ Nome: ação` ação com responsável. Veja `90-Config/convencoes.md`.
- **Etiquetas de reunião:** `#tema/<slug>` e `#reuniao/<tipo>` onde tipo ∈ `gravada`, `ritual`, `nao-gravada`, `entrevista`, `surgiu-no-dia`, `cancelada`.
- **Desenhos Excalidraw** são arquivos `.excalidraw.md`. Os textos ficam na seção `## Text Elements`. As formas e setas ficam no bloco `json` (ou `compressed-json`, comprimido com LZ-String em base64; descomprima com a biblioteca `lz-string` para ler as ligações `startBinding`/`endBinding` das setas). Se houver PNG exportado ao lado, você pode olhar a imagem.

## Integrações

- **Backlog:** veja `backlog.modo` em `config.md`. `manual` = prints/exports em `00-Inbox/_entrada/`. `mcp` = use o servidor MCP configurado.
- **PPT:** gere `.pptx` com `python-pptx` sempre a partir do template em `90-Config/ppt/` seguindo `90-Config/ppt/mapa-layouts.md`. Sem mapa, avise o PM para rodar `/configurar-template` e use um layout neutro.
- **FigJam:** se o conector do Figma estiver disponível, pode gerar diagramas; se não, entregue o prompt para a IA do FigJam.
