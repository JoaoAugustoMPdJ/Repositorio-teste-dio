-- Análise simples de créditos e descontos
-- Créditos ficam em um campo repetido, por isso usamos UNNEST.

SELECT
  invoice.month AS mes_fatura,
  IFNULL(credit.name, 'Sem crédito') AS tipo_credito,
  currency AS moeda,
  ROUND(SUM(IFNULL(credit.amount, 0)), 2) AS total_creditos
FROM `SEU_PROJECT_ID.billing_export.gcp_billing_export_v1_SEU_BILLING_ACCOUNT_ID`
LEFT JOIN UNNEST(credits) AS credit
GROUP BY mes_fatura, tipo_credito, moeda
ORDER BY mes_fatura DESC, total_creditos ASC;
