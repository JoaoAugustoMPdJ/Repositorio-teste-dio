-- Custo total por mês de fatura
-- Substitua o nome da tabela pelo caminho real do seu BigQuery.

SELECT
  invoice.month AS mes_fatura,
  currency AS moeda,
  ROUND(SUM(cost), 2) AS custo_total
FROM `SEU_PROJECT_ID.billing_export.gcp_billing_export_v1_SEU_BILLING_ACCOUNT_ID`
GROUP BY mes_fatura, moeda
ORDER BY mes_fatura DESC;
