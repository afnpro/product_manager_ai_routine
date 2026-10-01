# Rotina de PM com IA

Motor genérico para a rotina de PM com Obsidian, Excalidraw, Copilot M365, Claude Code, FigJam e Power Automate. Nada neste kit é corporativo: template de apresentação, regras de pontuação das histórias e histórico entram depois, no seu computador.

## Por que tudo está na raiz

Para dar para baixar sem `git clone`, todos os arquivos ficam na raiz do repositório, sem pastas, com o caminho no próprio nome. O prefixo `raiz_` marca a raiz do kit e cada `_` seguinte separa uma pasta:

```text
raiz_vault-modelo_.claude_skills_abrir-dia_SKILL.md   →   vault-modelo/.claude/skills/abrir-dia/SKILL.md
raiz_guia_Setup passo a passo.md                      →   guia/Setup passo a passo.md
```

Como alguns nomes originais também têm `_` (como `_contexto.md` e `_modelo-tema`), não converta os nomes à mão: use o script ou o mapa no fim desta página.

## Por onde começar

1. **Leia o guia** direto aqui no GitHub:
   - `raiz_guia_Rotina de PM com IA.md`: o sistema completo (rotina, reuniões, desenhos, comandos, roadmap, OKRs, métricas, comunicação)
   - `raiz_guia_Setup passo a passo.md`: a instalação, etapa por etapa
   - `raiz_guia_Prompts do Copilot.md`: os 7 prompts prontos para copiar
2. **Baixe os arquivos** para uma pasta vazia: **Code > Download ZIP**, ou, se o ZIP for bloqueado, **Download raw file** em cada arquivo `raiz_*` e no `montar_vault.py`.
3. **Monte as pastas** e copie para o seu vault, na pasta dos arquivos:

   ```bash
   # Mac
   python3 montar_vault.py --vault "/caminho/do/seu/vault"
   # Windows
   python montar_vault.py --vault "C:\caminho\do\seu\vault"
   ```

   O script cria `kit-rotina-pm/` (com `guia/` e `vault-modelo/`) e copia o conteúdo de `vault-modelo/` para a raiz do vault, incluindo a pasta oculta `.claude`. Ele **nunca sobrescreve** arquivos existentes, avisa se faltar algum arquivo no download e confere se o caminho é mesmo um vault (tem a pasta `.obsidian`). Sem `--vault`, só monta `kit-rotina-pm/`.

   **Sem Python?** Abra o Claude Code na pasta dos arquivos e peça: "Monte as pastas seguindo a tabela 'Mapa de arquivos' do README.md e depois copie o conteúdo de vault-modelo para o meu vault em <caminho>, sem sobrescrever nada".
4. **Siga o `Setup passo a passo`** a partir da etapa 3 (plugins do Obsidian).

## O que vem no kit

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

## Dependências no computador

- Claude Code
- Python 3 (para o `montar_vault.py` e para os comandos que geram PPT e leem documentos; o Claude Code instala `python-pptx`, `python-docx`, `pypdf` e `lzstring` quando precisar)
- Opcional: `pandoc`, `pdftotext`, LibreOffice (para conferir PPTs como imagem)

## Atualizar o kit

Baixe de novo e rode o script. Como ele não sobrescreve, para receber a versão nova de um comando, apague antes no vault a pasta daquele comando em `.claude/skills/`. Suas notas e configurações ficam intactas.

Ao adicionar ou renomear arquivos no repositório, atualize também a lista `MAPA` no `montar_vault.py` e a tabela abaixo.

## Para compartilhar com outros PMs

Compartilhe este repositório como está. Nunca compartilhe o seu vault: notas, temas, desenhos, rubrica calibrada e template ficam com você. Cada PM preenche o próprio `config.md` e calibra.

## Mapa de arquivos

| Arquivo no repositório | Caminho no kit |
| --- | --- |
| `raiz_guia_Prompts do Copilot.md` | `guia/Prompts do Copilot.md` |
| `raiz_guia_Rotina de PM com IA.md` | `guia/Rotina de PM com IA.md` |
| `raiz_guia_Setup passo a passo.md` | `guia/Setup passo a passo.md` |
| `raiz_vault-modelo_.claude_skills_abrir-dia_SKILL.md` | `vault-modelo/.claude/skills/abrir-dia/SKILL.md` |
| `raiz_vault-modelo_.claude_skills_comunicado_SKILL.md` | `vault-modelo/.claude/skills/comunicado/SKILL.md` |
| `raiz_vault-modelo_.claude_skills_configurar-rubrica_SKILL.md` | `vault-modelo/.claude/skills/configurar-rubrica/SKILL.md` |
| `raiz_vault-modelo_.claude_skills_configurar-template_SKILL.md` | `vault-modelo/.claude/skills/configurar-template/SKILL.md` |
| `raiz_vault-modelo_.claude_skills_daily_SKILL.md` | `vault-modelo/.claude/skills/daily/SKILL.md` |
| `raiz_vault-modelo_.claude_skills_demo_SKILL.md` | `vault-modelo/.claude/skills/demo/SKILL.md` |
| `raiz_vault-modelo_.claude_skills_entrevista_SKILL.md` | `vault-modelo/.claude/skills/entrevista/SKILL.md` |
| `raiz_vault-modelo_.claude_skills_fechar-dia_SKILL.md` | `vault-modelo/.claude/skills/fechar-dia/SKILL.md` |
| `raiz_vault-modelo_.claude_skills_figjam_SKILL.md` | `vault-modelo/.claude/skills/figjam/SKILL.md` |
| `raiz_vault-modelo_.claude_skills_historias_SKILL.md` | `vault-modelo/.claude/skills/historias/SKILL.md` |
| `raiz_vault-modelo_.claude_skills_importar_SKILL.md` | `vault-modelo/.claude/skills/importar/SKILL.md` |
| `raiz_vault-modelo_.claude_skills_metricas_SKILL.md` | `vault-modelo/.claude/skills/metricas/SKILL.md` |
| `raiz_vault-modelo_.claude_skills_novo-tema_SKILL.md` | `vault-modelo/.claude/skills/novo-tema/SKILL.md` |
| `raiz_vault-modelo_.claude_skills_okr_SKILL.md` | `vault-modelo/.claude/skills/okr/SKILL.md` |
| `raiz_vault-modelo_.claude_skills_ppt_SKILL.md` | `vault-modelo/.claude/skills/ppt/SKILL.md` |
| `raiz_vault-modelo_.claude_skills_prd_SKILL.md` | `vault-modelo/.claude/skills/prd/SKILL.md` |
| `raiz_vault-modelo_.claude_skills_principio_SKILL.md` | `vault-modelo/.claude/skills/principio/SKILL.md` |
| `raiz_vault-modelo_.claude_skills_refino_SKILL.md` | `vault-modelo/.claude/skills/refino/SKILL.md` |
| `raiz_vault-modelo_.claude_skills_roadmap_SKILL.md` | `vault-modelo/.claude/skills/roadmap/SKILL.md` |
| `raiz_vault-modelo_.claude_skills_semana_SKILL.md` | `vault-modelo/.claude/skills/semana/SKILL.md` |
| `raiz_vault-modelo_.claude_skills_status_SKILL.md` | `vault-modelo/.claude/skills/status/SKILL.md` |
| `raiz_vault-modelo_02-Temas__modelo-tema_Evidencias__modelo-evidencia.md` | `vault-modelo/02-Temas/_modelo-tema/Evidencias/_modelo-evidencia.md` |
| `raiz_vault-modelo_02-Temas__modelo-tema_Metricas__dicionario.md` | `vault-modelo/02-Temas/_modelo-tema/Metricas/_dicionario.md` |
| `raiz_vault-modelo_02-Temas__modelo-tema_OKRs__modelo-trimestre.md` | `vault-modelo/02-Temas/_modelo-tema/OKRs/_modelo-trimestre.md` |
| `raiz_vault-modelo_02-Temas__modelo-tema_Principios__modelo-principio.md` | `vault-modelo/02-Temas/_modelo-tema/Principios/_modelo-principio.md` |
| `raiz_vault-modelo_02-Temas__modelo-tema_Roadmap.md` | `vault-modelo/02-Temas/_modelo-tema/Roadmap.md` |
| `raiz_vault-modelo_02-Temas__modelo-tema__contexto.md` | `vault-modelo/02-Temas/_modelo-tema/_contexto.md` |
| `raiz_vault-modelo_04-Comunicacao_Exemplos__LEIA.md` | `vault-modelo/04-Comunicacao/Exemplos/_LEIA.md` |
| `raiz_vault-modelo_04-Comunicacao_Power-Automate_exemplo-edicao.json` | `vault-modelo/04-Comunicacao/Power-Automate/exemplo-edicao.json` |
| `raiz_vault-modelo_04-Comunicacao_Power-Automate_passo-a-passo.md` | `vault-modelo/04-Comunicacao/Power-Automate/passo-a-passo.md` |
| `raiz_vault-modelo_04-Comunicacao_card-template.json` | `vault-modelo/04-Comunicacao/card-template.json` |
| `raiz_vault-modelo_90-Config_config.md` | `vault-modelo/90-Config/config.md` |
| `raiz_vault-modelo_90-Config_convencoes.md` | `vault-modelo/90-Config/convencoes.md` |
| `raiz_vault-modelo_90-Config_ppt__LEIA.md` | `vault-modelo/90-Config/ppt/_LEIA.md` |
| `raiz_vault-modelo_90-Config_ppt_como-gerar-ppt.md` | `vault-modelo/90-Config/ppt/como-gerar-ppt.md` |
| `raiz_vault-modelo_90-Config_prompts-copilot_01-lista-reunioes.md` | `vault-modelo/90-Config/prompts-copilot/01-lista-reunioes.md` |
| `raiz_vault-modelo_90-Config_prompts-copilot_02-extracao-diaria.md` | `vault-modelo/90-Config/prompts-copilot/02-extracao-diaria.md` |
| `raiz_vault-modelo_90-Config_prompts-copilot_03-daily.md` | `vault-modelo/90-Config/prompts-copilot/03-daily.md` |
| `raiz_vault-modelo_90-Config_prompts-copilot_04-revisao-documento.md` | `vault-modelo/90-Config/prompts-copilot/04-revisao-documento.md` |
| `raiz_vault-modelo_90-Config_prompts-copilot_05-respostas-comunicado.md` | `vault-modelo/90-Config/prompts-copilot/05-respostas-comunicado.md` |
| `raiz_vault-modelo_90-Config_prompts-copilot_06-extracao-historica.md` | `vault-modelo/90-Config/prompts-copilot/06-extracao-historica.md` |
| `raiz_vault-modelo_90-Config_prompts-copilot_07-busca-documentos.md` | `vault-modelo/90-Config/prompts-copilot/07-busca-documentos.md` |
| `raiz_vault-modelo_90-Config_rubrica-fontes__LEIA.md` | `vault-modelo/90-Config/rubrica-fontes/_LEIA.md` |
| `raiz_vault-modelo_90-Config_rubrica-historias.md` | `vault-modelo/90-Config/rubrica-historias.md` |
| `raiz_vault-modelo_90-Config_template-prd.md` | `vault-modelo/90-Config/template-prd.md` |
| `raiz_vault-modelo_99-Templates_nota-diaria.md` | `vault-modelo/99-Templates/nota-diaria.md` |
| `raiz_vault-modelo_99-Templates_reuniao-nao-prevista.md` | `vault-modelo/99-Templates/reuniao-nao-prevista.md` |
| `raiz_vault-modelo_99-Templates_secao-reuniao.md` | `vault-modelo/99-Templates/secao-reuniao.md` |
| `raiz_vault-modelo_A revisar.md` | `vault-modelo/A revisar.md` |
| `raiz_vault-modelo_CLAUDE.md` | `vault-modelo/CLAUDE.md` |

Pastas que o kit cria vazias:

- `vault-modelo/00-Inbox/_entrada/`
- `vault-modelo/00-Inbox/_processado/`
- `vault-modelo/01-Diario/`
- `vault-modelo/01-Diario/Semanas/`
- `vault-modelo/02-Temas/_arquivo/`
- `vault-modelo/02-Temas/_modelo-tema/Artefatos/`
- `vault-modelo/02-Temas/_modelo-tema/Diagramas/`
- `vault-modelo/02-Temas/_modelo-tema/Entregas/`
- `vault-modelo/02-Temas/_modelo-tema/Historias/`
- `vault-modelo/02-Temas/_modelo-tema/Historico/`
- `vault-modelo/02-Temas/_modelo-tema/Metricas/Relatorios/`
- `vault-modelo/02-Temas/_modelo-tema/PRDs/`
- `vault-modelo/03-Backlog/Retratos/`
- `vault-modelo/04-Comunicacao/Comunicados/`
