-- Serviços com maior custo nos últimos 30 dias

SELECT
  service.description AS servico,
  currency AS moeda,
  ROUND(SUM(cost), 2) AS custo_total
FROM `SEU_PROJECT_ID.billing_export.gcp_billing_export_v1_SEU_BILLING_ACCOUNT_ID`
WHERE usage_start_time >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 30 DAY)
GROUP BY servico, moeda
ORDER BY custo_total DESC
LIMIT 20;
