---
name: prd
description: Escreve um PRD (documento de produto) a partir de notas, caixogramas, evidências e princípios, no template da empresa, terminando em perguntas para o tech lead. Use quando o PM pedir um PRD ou digitar /prd.
---

# /prd

Argumento: nome ou descrição curta da iniciativa. Ex.: `/prd exportação de relatórios`.

## Fronteira

O PRD diz **o quê** e **por quê**: problema, usuários, objetivos, requisitos, escopo, riscos. O **como** é da spec do tech lead. Toda decisão técnica que surgir vira item de "Perguntas para o tech lead".

## Entrada

- Template: `config.md` → `template_prd` (padrão `90-Config/template-prd.md`). Respeite as seções do template da empresa se ele tiver sido trocado.
- Busque no tema: notas diárias e decisões que mencionam a iniciativa, `Evidencias/`, `Principios/` validados, caixogramas em `Diagramas/`, item no `Roadmap.md`, KRs relacionados.

## Passos

1. **Levantamento:** liste o que encontrou por seção do template e o que falta. Se faltar problema ou objetivo, pergunte ao PM antes de escrever (no máximo 3 perguntas).
2. **Problema com evidência:** cada afirmação sobre usuário leva link para uma evidência. Sem evidência: marque como premissa a validar.
3. **Objetivos e métricas:** ligue a KRs existentes. Não invente baseline nem meta.
4. **Requisitos:** numerados (`RQ-01`), com prioridade (obrigatório, importante, desejável) e origem.
5. **Requisitos derivados dos princípios:** para cada princípio validado do tema que se aplica à iniciativa (de qualquer categoria: experiência, dados, segurança, operação etc.), escreva o requisito correspondente e cite o princípio (`P-003`).
6. **Contexto do sistema:** descreva o caixograma relevante em texto e, se útil, gere um diagrama Mermaid. É contexto, não proposta de arquitetura.
7. **Perguntas para o tech lead:** tudo o que é "como", viabilidade, estimativa e alternativas técnicas.
8. **Salve** em `02-Temas/<Tema>/PRDs/<nome>.md` (`tipo: prd`, `status: rascunho`, `versao: 0.1`).

## Saída no chat

Link do PRD, as lacunas marcadas e as premissas a validar. Sugira `/historias` como próximo passo quando o PM validar.
