# Prompt 05 · Respostas ao comunicado

**Quando:** segunda de manhã, depois do disparo de sexta.
**Como:** cole no Copilot; salve a resposta em `00-Inbox/_entrada/respostas-comunicado-AAAA-MM-DD.md` e peça ao Claude Code: "processe as respostas ao comunicado" (ele cria as evidências).

```text
Desde a última sexta-feira, liste TODAS as mensagens que recebi no Teams em resposta ao comunicado "{{assunto do comunicado}}", tanto em chats individuais quanto no canal "{{canal do produto}}".

Comece com: "Encontrei N respostas de M pessoas."

Para cada resposta:
Pessoa | Área ou time (se souber) | Canal (chat ou canal) | Tipo (dúvida, pedido, problema, elogio, sugestão, outro) | O que disse (trecho curto) | Precisa de resposta minha? (sim/não) | Já respondi? (sim/não)

Depois, separadamente:
- Dúvidas que apareceram mais de uma vez
- Problemas relatados (possíveis incidentes)
- Mensagens sem resposta minha há mais de 1 dia útil
```
