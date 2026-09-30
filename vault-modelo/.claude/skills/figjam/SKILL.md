---
name: figjam
description: Gera prompts fundamentados no vault para a IA do FigJam (jornada, service blueprint, visioning, naming, story map, esboço de dashboard, entre outros) ou cria o diagrama direto quando o conector do Figma estiver disponível; também traz de volta para o vault o resultado de um board. Use quando o PM digitar /figjam.
---

# /figjam

Argumentos: o artefato e o assunto. Ex.: `/figjam jornada publicar um server`, `/figjam blueprint aprovação`, `/figjam visioning`, `/figjam trazer <link do board>`.

## Princípio

Prompt genérico gera board genérico. Cada prompt leva dados reais do vault: segmentos, evidências com citação curta, sistemas dos caixogramas, princípios, métricas.

## Biblioteca de artefatos

| Artefato | Dados do vault que entram |
| --- | --- |
| Mapa de jornada | Segmento, etapas, dores e necessidades de `Evidencias/` por etapa, emoções citadas, oportunidades |
| Service blueprint | Jornada (camada do usuário) + sistemas e processos dos caixogramas (backstage e suporte) + pontos de contato |
| Visioning | Objetivo do tema, OKRs, apostas de longo prazo, evidências fortes. Dinâmica em etapas com tempo |
| Naming | Objetivo, públicos, glossário, nomes já usados e proibidos, critérios de avaliação |
| Story map | Épico, etapas da jornada, histórias de `Historias/` distribuídas por release |
| Árvore de oportunidades | Resultado (KR), oportunidades das evidências, soluções já propostas |
| Mapa de stakeholders | Stakeholders do `_contexto.md` em poder x interesse |
| Retro | Formato escolhido e eventos do período (entregas, decisões, incidentes) |
| Esboço de dashboard | Spec em `Metricas/dashboard-*.md` |
| Timeline do roadmap | `Roadmap.md` por horizonte |

## Passos

1. Identifique o artefato e reúna os dados listados na tabela.
2. **Com o conector do Figma disponível** (ferramentas de gerar diagrama no FigJam): para diagramas estruturados (fluxos, blueprint, timeline), gere direto. Informe o link.
3. **Sem conector, ou para dinâmicas livres** (visioning, naming, retro): escreva o prompt para a IA do FigJam com: objetivo do board, estrutura (colunas, raias, seções), conteúdo real para preencher, instruções de estilo (cores por tipo, legenda) e, para dinâmicas, as etapas com tempo.
4. Salve o prompt em `Artefatos/figjam-<artefato>-AAAA-MM-DD.md` e mostre no chat em bloco de código.

## Trazer um board de volta

`/figjam trazer <link>`: com o conector, leia o board; sem conector, peça ao PM um export ou print em `00-Inbox/_entrada/`. Registre no vault: decisões (→ `Historico/decisoes.md`), ideias priorizadas, necessidades (→ `Evidencias/`), nomes finalistas etc., com link para o board.
