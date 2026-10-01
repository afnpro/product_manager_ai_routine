---
name: roadmap
description: Cria e mantém o roadmap mensal do tema (mês atual, próximo, daqui a dois meses, longo prazo), rola o roadmap depois de cada demo registrando motivos, e gera visões em slide ou FigJam. Use no início do trimestre, após a demo ou quando o PM digitar /roadmap.
---

# /roadmap

Modos:
- `/roadmap` ou `/roadmap criar` → monta ou revisa o roadmap.
- `/roadmap rolar` → depois da demo: empurra tudo uma coluna.
- `/roadmap slide` → gera slide(s) no template.
- `/roadmap figjam` → gera o prompt (ou o diagrama via conector) de uma timeline mensal.

## Regras dos horizontes

| Horizonte | Compromisso | Descrição |
| --- | --- | --- |
| Mês atual | Compromisso, aparece na demo | Entregas concretas |
| Próximo mês | Planejado | Entregas ajustáveis |
| Daqui a dois meses | Direção | Problemas a resolver, não funcionalidades |
| Longo prazo | Apostas | Temas e resultados, sem data |

Toda iniciativa tem ID (`R-001`), resultado esperado, OKR ligado e evidência. Sem OKR ou sem evidência: marque `#revisar` ("por que isso está no roadmap?").

## Criar

1. Leia `OKRs/` do trimestre, `Evidencias/`, decisões e o roadmap atual.
2. Pergunte ao PM o que já está comprometido para o mês atual. Não decida isso sozinho.
3. Proponha a distribuição nos quatro horizontes, explicando cada escolha em uma linha (ligação com KR e evidência).
4. Aponte KRs sem nenhuma iniciativa e iniciativas sem KR.
5. Salve em `Roadmap.md` (`status: rascunho`).

## Rolar (após a demo)

1. Leia `Entregas/AAAA-MM.md` do mês que fechou.
2. Itens entregues saem do mês atual (ficam registrados em Entregas).
3. Itens não entregues: pergunte ao PM se voltam para o novo mês atual, descem ou saem. Registre o motivo.
4. Próximo mês vira mês atual; daqui a dois meses vira próximo (reescrito como entregas); longo prazo alimenta o novo "daqui a dois meses" (reescrito como problemas).
5. Atualize `ciclo_atual` e acrescente cada movimento no "Registro de mudanças" (data, ID, de → para, motivo, fonte).

## Visões

- **Slide:** siga `90-Config/ppt/como-gerar-ppt.md`. Uma coluna por horizonte, compromisso indicado visualmente, sem datas no longo prazo. Versão para stakeholders sem IDs internos.
- **FigJam:** prompt com colunas por horizonte e os itens; ou, com o conector do Figma, gere o diagrama.
