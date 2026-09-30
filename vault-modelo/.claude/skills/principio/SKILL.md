---
name: principio
description: Registra um princípio de governança do tema no formato padrão a partir de decisões recorrentes, e verifica caixogramas contra os princípios validados. Use na revisão semanal ou quando o PM digitar /principio.
---

# /principio

Modos:
- `/principio` → sugere e redige o próximo princípio.
- `/principio <texto>` → redige a partir do que o PM escreveu.
- `/principio verificar <diagrama>` → revisa um caixograma contra os princípios validados.

## Redigir

1. Leia `Historico/decisoes.md`, a revisão semanal e os princípios existentes em `Principios/`.
2. Sem texto do PM: escolha a decisão que mais se repete ou que mais gente precisaria aplicar sem perguntar. Explique a escolha em uma frase.
3. Verifique se já existe princípio parecido. Se existir, proponha atualizar em vez de criar outro.
4. Preencha `Principios/_modelo-principio.md`: título afirmativo, frase aplicável sem o PM, por quê, quando vale, exceções e quem pode abrir, como verificar, decisões de origem com link.
5. Numere na sequência (`P-001`, `P-002`…). `status: rascunho`.

Um bom princípio é curto, verificável e fala do **quê**, não do **como** técnico. "Todo MCP server que acessa dados classificados passa por autorização centralizada" é bom. "Usar OAuth 2.1 com PKCE" é decisão técnica: vira pergunta para o tech lead.

## Verificar um caixograma

1. Leia o desenho (caixas de texto e setas; descomprima o JSON se necessário).
2. Para cada princípio com `status: validado`, aplique o "Como verificar".
3. Liste violações e dúvidas como requisitos de produto, com a caixa ou seta envolvida: "A seta de `Server X` para `Base de clientes` não passa por `Autorização` (P-003)".
4. Salve em `Artefatos/verificacao-<diagrama>-AAAA-MM-DD.md` e crie `#revisar` para cada violação.
