# Passo a Passo - Criar Orçamento e Alertas no Console da GCP

## 1. Acessar o faturamento

1. Entre no Google Cloud Console.
2. No menu lateral, acesse **Billing / Faturamento**.
3. Selecione a conta de faturamento correta.

## 2. Acessar orçamentos e alertas

1. No menu de faturamento, clique em **Budgets & alerts / Orçamentos e alertas**.
2. Clique em **Create budget / Criar orçamento**.

## 3. Definir nome e escopo

Sugestão de nome:

```text
orcamento-laboratorio-gcp
```

Configure o escopo conforme o objetivo:

- conta de faturamento inteira; ou
- projeto específico; ou
- serviço específico; ou
- recurso filtrado por label.

Para projeto de portfólio, recomenda-se escopo por projeto.

## 4. Definir valor do orçamento

Configure o orçamento como mensal e informe o valor planejado.

Exemplo:

```text
R$ 50,00 por mês
```

## 5. Definir limites de alerta

Configure os alertas:

| Percentual | Tipo sugerido |
|---|---|
| 50% | Gasto real |
| 75% | Gasto real |
| 90% | Gasto real |
| 100% | Gasto real |
| 100% | Gasto previsto |

## 6. Configurar notificações

Marque a opção para enviar alertas por e-mail aos administradores/responsáveis.

Se necessário, configure canais adicionais no Cloud Monitoring.

## 7. Salvar orçamento

Revise as informações e clique em **Finish / Concluir**.

## 8. Registrar evidências

Salve prints nas seguintes telas:

- painel de faturamento;
- configuração do orçamento;
- limites de alerta;
- orçamento criado;
- relatório de custos.
