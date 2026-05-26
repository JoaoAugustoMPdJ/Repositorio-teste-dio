-- Evolução diária dos custos

SELECT
  DATE(usage_start_time) AS data_uso,
  currency AS moeda,
  ROUND(SUM(cost), 2) AS custo_total
FROM `SEU_PROJECT_ID.billing_export.gcp_billing_export_v1_SEU_BILLING_ACCOUNT_ID`
WHERE usage_start_time >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 30 DAY)
GROUP BY data_uso, moeda
ORDER BY data_uso;
