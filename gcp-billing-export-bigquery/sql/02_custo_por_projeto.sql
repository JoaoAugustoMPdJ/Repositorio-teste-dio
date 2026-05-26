-- Custo por projeto no mês atual ou em período filtrado

SELECT
  project.id AS projeto_id,
  project.name AS projeto_nome,
  currency AS moeda,
  ROUND(SUM(cost), 2) AS custo_total
FROM `SEU_PROJECT_ID.billing_export.gcp_billing_export_v1_SEU_BILLING_ACCOUNT_ID`
WHERE usage_start_time >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 30 DAY)
GROUP BY projeto_id, projeto_nome, moeda
ORDER BY custo_total DESC;
