# Fluxo do comunicado semanal no Power Automate

O Claude Code grava o JSON da edição; o fluxo mostra a prévia, pede sua aprovação e só então dispara. Os nomes das ações podem aparecer em português ou inglês conforme o idioma do seu Power Automate. As expressões abaixo usam os nomes sugeridos entre aspas: renomeie as ações com esses nomes ou ajuste as expressões.

## 1. Lista do SharePoint: "Destinatarios Comunicado"

| Coluna | Tipo | Observação |
| --- | --- | --- |
| Title | Texto | Nome da pessoa |
| Email | Texto (uma linha) | E-mail corporativo |
| Segmento | Escolha: `geral`, `consome`, `publica`, `seguranca` | Mesmos nomes das chaves do JSON, em minúsculas |
| OptOut | Sim/Não (padrão: Não) | Quem pediu para não receber |
| Observacoes | Texto | Opcional |

Quem pedir para sair: marque `OptOut = Sim`. Não apague a linha.

## 2. Pasta no OneDrive

Crie `Comunicados/prontos` e `Comunicados/enviados` no seu OneDrive. Informe o caminho de `prontos` em `pasta_onedrive_comunicados` no `90-Config/config.md`.

## 3. O fluxo

**Gatilho:** OneDrive for Business · *Quando um arquivo é criado* (When a file is created) · pasta `Comunicados/prontos`.

**Condição de entrada:** o nome termina em `.json` → `endsWith(triggerOutputs()?['headers']?['x-ms-file-name'], '.json')`. Se não, encerre.

**Ação "Edicao"** (Compor / Compose):
```
json(base64ToString(triggerBody()?['$content']))
```
Se der erro de formato, troque por `json(triggerBody())`.

**Ação "Previa"** · Teams · *Postar cartão em um chat ou canal* (Post card in a chat or channel):
- Postar como: Flow bot · Postar em: Chat com o Flow bot · Destinatário: seu e-mail
- Cartão adaptável: `outputs('Edicao')?['cards']?['geral']`

**Ação "Aprovacao"** · Aprovações · *Iniciar e aguardar uma aprovação* (Start and wait for an approval):
- Tipo: Aprovar/Rejeitar – primeiro a responder · Atribuído a: você
- Título: `Comunicado edição @{outputs('Edicao')?['edicao']}: @{outputs('Edicao')?['assunto']}`
- Detalhes: "Veja a prévia no chat do Flow bot. Aprovar dispara para a lista e o canal."

**Condição:** `outputs('Aprovacao')?['body/outcome']` é igual a `Approve`.

### Se aprovado

1. **"Destinatarios"** · SharePoint · *Obter itens* (Get items) · lista "Destinatarios Comunicado"
   - Consulta de filtro: `OptOut eq 0`
   - Configurações: ative a paginação (limite 5000)
2. **"Para cada pessoa"** · *Aplicar a cada* sobre `body('Destinatarios')?['value']`
   - Configurações: controle de simultaneidade **ativado, grau 1** (envio em sequência)
   - **"Segmento"** (Compor): `if(empty(items('Para_cada_pessoa')?['Segmento']?['Value']), 'geral', toLower(items('Para_cada_pessoa')?['Segmento']?['Value']))`
   - **"Card"** (Compor): `coalesce(outputs('Edicao')?['cards']?[outputs('Segmento')], outputs('Edicao')?['cards']?['geral'])`
   - **Envio:** a mesma ação que você já usa hoje para postar o card no chat individual, com o cartão = `outputs('Card')` e o destinatário = `items('Para_cada_pessoa')?['Email']`
   - **Atraso** (Delay): 5 segundos
3. **"Canal"** · *Postar cartão em um chat ou canal* · Postar em: Canal · equipe e canal do produto · cartão `outputs('Edicao')?['cards']?['geral']`
4. **Mover o arquivo** · OneDrive · *Mover ou renomear um arquivo* → `Comunicados/enviados`
5. **Confirmação:** mensagem para você no Flow bot com o número de envios: `length(body('Destinatarios')?['value'])`

### Se rejeitado

Mensagem para você com os comentários da aprovação. O arquivo fica em `prontos`; gere um novo com `/comunicado` depois dos ajustes (apague o rejeitado para não confundir).

### Falhas

Na ação de envio, configure "Configurar execução após" para também seguir quando falhar, e registre numa variável (matriz) os e-mails que falharam. No fim, mande a lista para você.

## 4. Testes antes do primeiro envio real

1. Crie uma lista de teste com você e mais uma pessoa de confiança, um de cada segmento.
2. Rode `/comunicado`, copie o JSON para `prontos`, aprove, confira os cards no chat e no canal (use um canal de teste).
3. Confira o card no celular também.
4. Só então aponte o fluxo para a lista real.

## Observações

- O conector do Teams tem limites de chamadas. O atraso de 5 segundos e o envio em sequência evitam bloqueio. Para listas muito grandes, divida o envio em blocos (por exemplo, filtrando por segmento) em horários diferentes.
- Valide o visual do template no Adaptive Cards Designer (adaptivecards.io/designer), com o host "Microsoft Teams".
- Nunca coloque texto gerado direto em `prontos` sem ter passado pelo `/comunicado`: é ele que valida o JSON.
