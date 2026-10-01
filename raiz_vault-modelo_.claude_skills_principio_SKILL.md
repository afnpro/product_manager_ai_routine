---
name: principio
description: Registra princípios de produto do tema (regras de decisão que o time aplica sem precisar perguntar ao PM, de qualquer natureza - valor, experiência, dados, segurança, operação, limites técnicos) a partir de decisões recorrentes, e verifica artefatos contra os princípios validados. Use na revisão semanal ou quando o PM digitar /principio.
---

# /principio

Um princípio é uma **regra de decisão** que qualquer pessoa do time consegue aplicar sozinha. Cada princípio registrado é uma pergunta a menos que precisa passar pelo PM. Vale para qualquer produto e qualquer natureza de decisão.

## Modos

- `/principio` → sugere e redige o próximo princípio a partir das decisões recentes.
- `/principio <texto>` → redige a partir do que o PM escreveu.
- `/principio verificar <artefato>` → confere um caixograma, PRD, conjunto de histórias ou proposta contra os princípios validados.
- `/principio revisar` → revisão periódica: princípios que não são citados há muito tempo, que conflitam entre si ou que foram contrariados por decisões recentes.

## Categorias

Use a que melhor descreve o princípio. O `_contexto.md` do tema pode indicar quais categorias importam mais.

| Categoria | Responde a | Exemplo (genérico) |
| --- | --- | --- |
| Valor e escopo | O que entra e o que não entra no produto | "Só construímos o que resolve um problema com evidência de pelo menos dois segmentos" |
| Experiência | Como o usuário deve ser tratado | "Nenhuma ação irreversível sem confirmação e sem forma de desfazer" |
| Dados e privacidade | O que pode ser coletado, exibido, guardado | "Dado pessoal só é exibido para quem tem necessidade de negócio registrada" |
| Segurança e conformidade | Controles que não se negociam | "Todo acesso a dado classificado passa por autorização central e fica auditado" |
| Operação | Como o produto é mantido e suportado | "Nada vai para produção sem dono de suporte definido" |
| Limites técnicos de produto | Restrições que o produto impõe à solução (o quê, não o como) | "Funcionalidades novas funcionam para usuários sem conexão estável" |
| Comunicação | Como o produto fala com usuários e stakeholders | "Mudança que quebra uso existente é avisada com 30 dias de antecedência" |

## Redigir

1. Leia `Historico/decisoes.md`, a revisão semanal mais recente e os princípios existentes em `Principios/`.
2. Sem texto do PM: escolha a decisão que **mais se repete** ou que **mais gente precisaria aplicar sem perguntar**. Explique a escolha em uma frase.
3. Verifique se já existe princípio parecido. Se existir, proponha atualizar em vez de criar outro.
4. Preencha o modelo `Principios/_modelo-principio.md`: título afirmativo, categoria, a regra em uma frase, por quê, quando vale, exceções e quem pode abrir, como verificar, decisões de origem com link.
5. Numere na sequência (`P-001`, `P-002`…). `status: rascunho`.

**Teste de um bom princípio:**
- Curto e afirmativo.
- Aplicável sem o PM: alguém novo no time consegue decidir com ele.
- Verificável: dá para olhar um artefato e dizer se está cumprido.
- Fala do **quê**, não do **como**. "Usar a biblioteca X" ou "cachear por 5 minutos" são decisões de implementação: viram pergunta para o tech lead, não princípio.
- Tem um custo real: se ninguém discordaria, é uma obviedade, não um princípio.

## Verificar um artefato

1. Leia o artefato:
   - **Caixograma:** caixas de texto e setas (descomprima o JSON se necessário).
   - **PRD ou histórias:** requisitos, critérios de aceite, escopo.
   - **Proposta ou documento:** decisões e premissas.
2. Para cada princípio com `status: validado` que se aplica ao tipo de artefato, use o campo "Como verificar".
3. Liste violações e dúvidas como requisitos, apontando o trecho, a caixa ou a seta envolvida e o princípio (`P-003`).
4. Salve em `Artefatos/verificacao-<artefato>-AAAA-MM-DD.md` e crie um `#revisar` para cada violação.

## Revisar

1. Para cada princípio validado: quando foi citado pela última vez (decisões, PRDs, verificações), se alguma decisão recente o contrariou e se conflita com outro princípio.
2. Sugira manter, ajustar, fundir ou arquivar (`status: arquivado`), com o motivo. O PM decide.
