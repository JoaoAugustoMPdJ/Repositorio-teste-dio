-- Validação rápida de registros e período disponível

SELECT
  COUNT(*) AS total_linhas,
  MIN(DATE(usage_start_time)) AS primeira_data,
  MAX(DATE(usage_start_time)) AS ultima_data,
  ROUND(SUM(cost), 2) AS custo_total
FROM `SEU_PROJECT_ID.billing_export.gcp_billing_export_v1_SEU_BILLING_ACCOUNT_ID`;
