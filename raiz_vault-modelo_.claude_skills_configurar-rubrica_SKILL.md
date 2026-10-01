---
name: configurar-rubrica
description: Transforma as regras de pontuação do sistema interno de backlog e exemplos de histórias com nota alta numa rubrica verificável que o /historias usa para se autoavaliar. Use uma vez na instalação, quando as regras mudarem, ou quando o PM digitar /configurar-rubrica.
---

# /configurar-rubrica

## Entrada

Tudo em `90-Config/rubrica-fontes/`: textos da wiki ou guia, prints da tela de avaliação, exemplos de histórias com a nota recebida.

## Passos

1. Leia todos os arquivos (olhe as imagens). Liste o que encontrou.
2. **Extraia cada critério** de pontuação: nome, o que exige, peso ou pontos, como é verificado, exemplos de atende e não atende. Não invente critérios que não estejam nas fontes; se deduzir algo dos exemplos, marque como "inferido dos exemplos".
3. **Formato obrigatório:** campos exigidos, modelo de título, formato de critério de aceite, tamanho, etiquetas, vínculos (épico, OKR), definição de pronto.
4. **Nota-alvo:** qual nota é considerada alta. Pergunte ao PM se não estiver nas fontes.
5. **Calibração com os exemplos:** aplique a rubrica aos exemplos com nota conhecida e compare com a nota real. Se errar por mais de 10%, ajuste pesos ou interpretação e registre o ajuste. Mostre a tabela exemplo × nota real × nota estimada.
6. **Checklist de autoavaliação:** para cada critério, uma pergunta de sim ou não que o `/historias` aplica.
7. **Formato de importação** para a ferramenta, se as fontes indicarem (colunas de CSV, campos).
8. Sobrescreva `90-Config/rubrica-historias.md` com `configurada: sim`, `status: rascunho`, critérios, pesos, nota-alvo, checklist, formato e o resultado da calibração. Mantenha os critérios genéricos INVEST numa seção final como complemento.

## Saída no chat

Resumo dos critérios, a precisão na calibração e o que ficou em dúvida para o PM confirmar.
