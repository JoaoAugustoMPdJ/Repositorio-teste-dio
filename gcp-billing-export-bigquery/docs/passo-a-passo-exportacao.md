# Passo a passo executado: exportação de Billing para BigQuery

Este documento descreve o processo que deve ser executado no Console do Google Cloud.

## 1. Acessar o Console do Google Cloud

Entre no Console:

```text
https://console.cloud.google.com/
```

Confirme se está no projeto correto ou crie um projeto separado para FinOps.

Sugestão de nome:

```text
finops-billing-monitoring
```

## 2. Criar dataset no BigQuery

Acesse:

```text
BigQuery > Explorer > seu projeto > Create dataset
```

Configuração sugerida:

| Campo | Valor sugerido |
|---|---|
| Dataset ID | `billing_export` |
| Location type | Multi-region |
| Region | `US` |
| Table expiration | Não definir expiração automática |
| Encryption | Google-managed key para laboratório |

Salve o print como:

```text
docs/prints/02-criacao-dataset-bigquery.png
```

## 3. Acessar Cloud Billing

No menu principal, acesse:

```text
Billing > Billing export
```

Caso tenha mais de uma conta de faturamento, selecione a conta correta.

Salve o print como:

```text
docs/prints/01-billing-export-menu.png
```

## 4. Habilitar Standard usage cost

Na aba:

```text
BigQuery export
```

Em **Standard usage cost**, clique em:

```text
Edit settings
```

Selecione:

| Campo | Valor |
|---|---|
| Project | Projeto onde está o dataset |
| Dataset | `billing_export` |

Clique em **Save**.

Salve o print como:

```text
docs/prints/03-configuracao-standard-export.png
```

## 5. Habilitar Detailed usage cost

Ainda em **Billing export > BigQuery export**, localize:

```text
Detailed usage cost
```

Clique em **Edit settings**.

Selecione o mesmo projeto e dataset:

```text
Projeto: finops-billing-monitoring
Dataset: billing_export
```

Clique em **Save**.

Salve o print como:

```text
docs/prints/04-configuracao-detailed-export.png
```

## 6. Habilitar Pricing data

Esta etapa é opcional, mas recomendada para uma documentação mais completa.

Antes disso, garanta que a API abaixo esteja ativa no projeto:

```text
BigQuery Data Transfer Service API
```

Depois, em **Billing export > BigQuery export**, localize:

```text
Pricing data
```

Clique em **Edit settings**, selecione projeto e dataset, e salve.

## 7. Validar tabelas criadas no BigQuery

Acesse:

```text
BigQuery > Explorer > projeto > billing_export
```

As tabelas esperadas são:

```text
gcp_billing_export_v1_<BILLING_ACCOUNT_ID>
gcp_billing_export_resource_v1_<BILLING_ACCOUNT_ID>
cloud_pricing_export
```

Salve o print como:

```text
docs/prints/05-tabelas-criadas-bigquery.png
```

## 8. Executar consulta de validação

Use uma consulta simples para validar os dados:

```sql
SELECT
  invoice.month AS mes_fatura,
  service.description AS servico,
  ROUND(SUM(cost), 2) AS custo_total
FROM `SEU_PROJECT_ID.billing_export.gcp_billing_export_v1_SEU_BILLING_ACCOUNT_ID`
GROUP BY mes_fatura, servico
ORDER BY custo_total DESC;
```

Salve o print como:

```text
docs/prints/06-consulta-validacao-custos.png
```

## 9. Resultado esperado

Após a configuração, o BigQuery passa a receber dados de faturamento de forma automática, permitindo consultas e análises como:

- custo por projeto;
- custo por serviço;
- custo diário;
- análise de créditos;
- identificação de serviços mais caros;
- criação de dashboards no Looker Studio.
