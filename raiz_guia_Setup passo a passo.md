# Setup passo a passo

O setup leva cerca de 1h30 no total, feito no seu computador de trabalho: 30 min de instalação, 30 min de calibração e o tempo que quiser dedicar à importação. Marque cada passo conforme avança.

## 1. Antes de começar

- [ ] Confirme com a empresa: uso do Claude Code sobre o vault, cópia de transcrições e documentos no vault, transcrição da daily e do refino, disparo em massa pelo Power Automate
- [ ] Obsidian instalado, com o vault que você já usa
- [ ] Claude Code funcionando no terminal (rode `claude --version`)
- [ ] Python 3 instalado (rode `python3 --version` no Mac ou `python --version` no Windows). As bibliotecas o próprio Claude Code instala quando precisar
- [ ] Faça uma cópia de segurança do vault antes de mexer (copie a pasta inteira para outro lugar)

## 2. Baixar o kit e montar as pastas

O repositório (github.com/afnpro/product_manager_ai_routine) guarda todos os arquivos na raiz, sem pastas, com o caminho no próprio nome: `raiz_vault-modelo_.claude_skills_abrir-dia_SKILL.md` é o arquivo `vault-modelo/.claude/skills/abrir-dia/SKILL.md`. Assim dá para baixar sem `git clone`. O script `montar_vault.py` refaz as pastas.

1. **Baixe os arquivos** para uma pasta vazia (ex.: `Downloads/kit-pm`), de um destes jeitos:
    - No GitHub, **Code > Download ZIP**, e descompacte.
    - Se o ZIP for bloqueado: abra cada arquivo no GitHub e use **Download raw file**. Baixe todos os `raiz_*` e o `montar_vault.py` para a mesma pasta.
2. **Monte as pastas.** No terminal, dentro dessa pasta, rode:
    - Mac: `python3 montar_vault.py --vault "/caminho/do/seu/vault"`
    - Windows: `python montar_vault.py --vault "C:\caminho\do\seu\vault"`

    O script cria `kit-rotina-pm/` (com `guia/` e `vault-modelo/`) ao lado dos arquivos e copia o conteúdo de `vault-modelo/` para a raiz do seu vault, incluindo a pasta oculta `.claude`. Ele **nunca sobrescreve** um arquivo que já existe: pula e avisa. Também avisa se faltar algum arquivo no download. Sem `--vault`, ele só monta `kit-rotina-pm/` e você copia depois (nesse caso, mostre os arquivos ocultos: Cmd + Shift + . no Finder; Exibir > Mostrar > Itens ocultos no Windows).
3. **Sem Python?** Abra o Claude Code na pasta dos arquivos e peça: "Monte as pastas seguindo a tabela 'Mapa de arquivos' do README.md e depois copie o conteúdo de vault-modelo para o meu vault em <caminho>, sem sobrescrever nada".
4. **Confira** na raiz do vault: `CLAUDE.md`, `A revisar.md`, `.claude/skills/` (com 21 pastas) e as pastas `00-Inbox` a `99-Templates`.

O Obsidian não mostra a pasta `.claude` nem os arquivos `.json`. É normal.

**Atualizações do kit:** baixe de novo e rode o script. Como ele não sobrescreve, para receber a versão nova de um comando apague antes, no vault, a pasta daquele comando em `.claude/skills/` (seus arquivos de configuração e notas ficam intactos).

## 3. Plugins do Obsidian

Em Configurações > Plugins da comunidade, desative o modo restrito, clique em Procurar e instale e ative cada um.

**Templater**

- [ ] Em "Template folder location", escolha `99-Templates`
- [ ] Ative "Trigger Templater on new file creation" (para a nota diária funcionar com o template)
- [ ] Em "Template hotkeys", adicione `99-Templates/reuniao-nao-prevista.md`. Depois, em Configurações > Atalhos, busque por "reuniao-nao-prevista" e defina uma tecla (ex.: Ctrl/Cmd + Shift + R)

**Notas diárias (plugin nativo)**

- [ ] Em Configurações > Plugins nativos, ative "Notas diárias"
- [ ] Pasta: `01-Diario` · Formato: `YYYY-MM-DD` · Template: `99-Templates/nota-diaria.md`

**Dataview**

- [ ] Instale e ative. Abra a nota "A revisar": as tabelas devem aparecer vazias, sem erro

**Excalidraw**

- [ ] Nas configurações do plugin, na parte de salvamento, desligue a opção de comprimir o JSON no markdown (o nome exato varia conforme a versão; procure por "compress")
- [ ] Exportação automática em PNG: deixe desligada por enquanto

**Obsidian Git (opcional)**

- [ ] Instale se quiser comparar versões dos caixogramas. Configure para fazer commit automático a cada 30 ou 60 minutos, sem push (fica só no seu computador)

## 4. Preencher a configuração

Abra `90-Config/config.md` no Obsidian e preencha:

- [ ] Identidade: nome, produto, gestor
- [ ] Temas ativos: `MCP`
- [ ] Horários: já vêm com a rotina combinada; ajuste se quiser
- [ ] Backlog: deixe `modo: manual` até o MCP da ferramenta ficar pronto
- [ ] Comunicação: canal do produto, pasta do OneDrive, links de feedback e documentação (pode completar no passo 8)
- [ ] Métricas: ferramenta de dashboards

## 5. Abrir o Claude Code no vault

1. Abra o terminal e vá até a pasta do vault:
    - Mac: `cd "/caminho/do/seu/vault"` (dica: digite `cd ` e arraste a pasta do Finder para o terminal)
    - Windows: `cd "C:\caminho\do\seu\vault"`
2. Rode `claude`.
3. Digite `/` e confira se aparecem os comandos do kit (`/abrir-dia`, `/fechar-dia`, `/status`...). Se não aparecerem, a pasta `.claude` não está na raiz do vault: volte ao passo 2.
4. Teste de leitura: escreva "Leia o CLAUDE.md e me explique em 5 linhas como este vault funciona". A resposta deve citar a estrutura de pastas e a regra de rascunho.
5. O Claude Code vai pedir permissão para criar arquivos e rodar Python. Aprove quando fizer sentido; você pode aprovar "para esta sessão" para não repetir.

Todo comando do kit roda sempre a partir dessa pasta. Abra o terminal no vault no arranque e deixe aberto o dia todo.

## 6. Calibrar com o material da empresa

Tudo isso fica só no seu computador.

- [ ] **Template de apresentação:** copie o arquivo para `90-Config/ppt/` e rode `/configurar-template`. Abra o `teste-template.pptx` gerado no PowerPoint e confira
- [ ] **Regras das histórias:** salve em `90-Config/rubrica-fontes/` o texto da wiki, prints da tela de avaliação e 3 a 5 histórias com nota alta. Rode `/configurar-rubrica` e confira a tabela de calibração
- [ ] **Tom do comunicado:** salve 2 ou 3 comunicados antigos em `04-Comunicacao/Exemplos/`
- [ ] **PRD:** se a empresa tiver template oficial, substitua `90-Config/template-prd.md` (mantenha o bloco do topo entre `---`)

## 7. Importar o histórico do MCP

1. No Copilot, rode o prompt de busca de documentos (arquivo `Prompts do Copilot.md`, prompt 7). Baixe os de relevância alta para `00-Inbox/_entrada/`.
2. No Teams, baixe as transcrições das reuniões que você organizou nos últimos 3 a 6 meses para a mesma pasta.
3. No Copilot, rode o prompt de extração histórica (prompt 6) mês a mês, do mais recente para o mais antigo. Salve cada resposta como `copilot-mcp-AAAA-MM.md` na mesma pasta.
4. No Claude Code, rode `/importar mcp`. Ele processa em lotes de 20 e para entre eles; diga "continue" para seguir.
5. Revise o relatório em `02-Temas/MCP/Historico/importacao-AAAA-MM-DD.md` e os itens em "A revisar".

Os desenhos do Excalidraw que já estão no vault entram automaticamente no `/importar`.

## 8. Montar o fluxo de comunicação

Pode ficar para a semana seguinte. O passo a passo completo, com as expressões, está no kit em `04-Comunicacao/Power-Automate/passo-a-passo.md`. Em resumo:

1. Crie no SharePoint a lista "Destinatarios Comunicado" com as colunas Title, Email, Segmento (escolha: geral, consome, publica, seguranca), OptOut (Sim/Não) e Observacoes.
2. Crie no OneDrive as pastas `Comunicados/prontos` e `Comunicados/enviados`.
3. Monte o fluxo: gatilho de arquivo criado em `prontos` → ler o JSON → prévia do card para você → aprovação → envio individual por segmento com 5 s de intervalo → post no canal → mover para `enviados`.
4. Teste com `04-Comunicacao/Power-Automate/exemplo-edicao.json`, uma lista só com você e mais uma pessoa, e um canal de teste.

## 9. Sexta, 2/10: planejar o Q4

- [ ] `/novo-tema MCP` (revisa o contexto que a importação preencheu)
- [ ] `/okr`
- [ ] `/roadmap`
- [ ] `/metricas definir`
- [ ] Validar os princípios candidatos mais importantes

## 10. Segunda, 5/10: primeiro dia

1. **8h40:** prompt 1 no Copilot → cole a resposta depois de `/abrir-dia`. Salve o print do board como `00-Inbox/_entrada/board-2026-10-05.png` e rode `/daily`.
2. **Durante o dia:** palavras-chave na nota; desenhos criados dentro da seção da reunião; atalho para reunião não prevista.
3. **18h:** rode no Copilot o prompt que o `/abrir-dia` gerou (fica em `00-Inbox/prompt-extracao-hoje.md`), depois a segunda passada, e cole as duas respostas depois de `/fechar-dia`.

## Problemas comuns

| Sintoma | Causa provável | O que fazer |
| --- | --- | --- |
| Comandos não aparecem ao digitar `/` | `.claude` fora da raiz ou Claude Code aberto em outra pasta | Rode `pwd` (Mac) ou `cd` (Windows) e confira a pasta |
| Nota diária com `<% tp... %>` no texto | Templater não processou | Ative "Trigger Templater on new file creation" ou crie a nota pelo `/abrir-dia` |
| "A revisar" mostra erro | Dataview desativado | Ative o plugin |
| Claude não lê as setas dos desenhos | JSON comprimido | Desligue a compressão; os antigos o `/importar` descomprime |
| Copilot devolve menos reuniões que a agenda | Resposta cortada | Peça por período (manhã e tarde) |
| PPT sai fora do padrão | Template não configurado | Rode `/configurar-template` |
