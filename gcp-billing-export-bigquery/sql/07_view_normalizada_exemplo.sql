-- Exemplo de view para normalizar campos mais usados
-- Ajuste o caminho da tabela e do dataset antes de executar.

CREATE OR REPLACE VIEW `SEU_PROJECT_ID.billing_export.vw_custos_normalizados` AS
SELECT
  DATE(usage_start_time) AS data_uso,
  invoice.month AS mes_fatura,
  project.id AS projeto_id,
  project.name AS projeto_nome,
  service.description AS servico,
  sku.description AS sku,
  location.location AS localidade,
  currency AS moeda,
  cost AS custo
FROM `SEU_PROJECT_ID.billing_export.gcp_billing_export_v1_SEU_BILLING_ACCOUNT_ID`;
