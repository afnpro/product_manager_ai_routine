# Rotina de PM com IA

Motor genérico para a rotina de PM com Obsidian, Excalidraw, Copilot M365, Claude Code, FigJam e Power Automate. O guia completo está na pasta `guia/`, em markdown: `Rotina de PM com IA.md`, `Setup passo a passo.md` e `Prompts do Copilot.md`.

Nada neste kit é corporativo. Template de apresentação, regras de pontuação das histórias e histórico entram depois, no seu computador.

## O que tem aqui

```text
guia/                        o guia em markdown (rotina, setup, prompts do Copilot)
vault-modelo/
  CLAUDE.md                  regras que o Claude Code segue no vault
  A revisar.md               fila de revisão (Dataview)
  .claude/skills/            21 comandos (/abrir-dia, /fechar-dia, /status, /prd, ...)
  00-Inbox/                  entrada de material e processados
  01-Diario/                 notas diárias e revisões semanais
  02-Temas/_modelo-tema/     modelo de pasta de tema
  03-Backlog/Retratos/       retratos diários do board
  04-Comunicacao/            template do card, exemplos de tom, fluxo do Power Automate
  90-Config/                 config pessoal, convenções, prompts do Copilot, PPT, PRD, rubrica
  99-Templates/              templates do Templater
```

## Instalação (cerca de 30 minutos)

1. **Confirme com a empresa** os pontos da seção "Pontos a confirmar" do guia.
2. **Copie o conteúdo de `vault-modelo/`** para a raiz do seu vault do Obsidian, inclusive a pasta oculta `.claude/`. Se já tiver pastas com esses nomes, mescle.
3. **Plugins do Obsidian** (Configurações → Plugins da comunidade):
   - **Templater:** pasta de templates = `99-Templates`. Crie um atalho de teclado para inserir `reuniao-nao-prevista`. Opcional: template da nota diária = `99-Templates/nota-diaria.md`.
   - **Dataview:** ative. A nota "A revisar" passa a funcionar.
   - **Excalidraw:** desative a compressão do JSON no markdown. Exportação automática em PNG é opcional.
   - **Obsidian Git** (opcional): versiona o vault e permite comparar caixogramas ao longo do tempo.
4. **Preencha `90-Config/config.md`.**
5. **Crie o tema:** copie `02-Temas/_modelo-tema/` para `02-Temas/MCP/` (ou deixe o `/novo-tema` fazer isso).
6. **Abra o Claude Code na pasta do vault** (`cd` para a pasta e `claude`). Os comandos aparecem digitando `/`.
7. **Calibre:**
   - Template de apresentação em `90-Config/ppt/` → `/configurar-template`
   - Regras e exemplos de histórias em `90-Config/rubrica-fontes/` → `/configurar-rubrica`
   - 2 ou 3 comunicados antigos em `04-Comunicacao/Exemplos/`
   - Se a empresa tiver template de PRD, substitua `90-Config/template-prd.md`
8. **Importe o histórico:** use os prompts `06` e `07` de `90-Config/prompts-copilot/`, baixe o material para `00-Inbox/_entrada/` e rode `/importar mcp`.
9. **Monte o fluxo de comunicação** seguindo `04-Comunicacao/Power-Automate/passo-a-passo.md`. Teste com `exemplo-edicao.json` antes do primeiro envio real.
10. **Na sexta:** `/novo-tema MCP` (revisão), `/okr`, `/roadmap`, `/metricas definir`.
11. **Na segunda:** arranque às 8h40 com o prompt `01` + `/abrir-dia`; fechamento às 18h com o prompt do dia + `/fechar-dia`.

## Dependências no computador

- Claude Code
- Python 3 com `python-pptx`, `python-docx`, `pypdf`, `lzstring` (o Claude Code instala se faltar)
- Opcional: `pandoc`, `pdftotext`, LibreOffice (para conferir PPTs como imagem)

## Para compartilhar com outros PMs

Compartilhe esta pasta como está (ou transforme `.claude/skills/` num plugin do Claude Code num repositório interno). Nunca compartilhe o seu vault: notas, temas, desenhos, rubrica calibrada e template ficam com você. Cada PM preenche o próprio `config.md` e calibra.
