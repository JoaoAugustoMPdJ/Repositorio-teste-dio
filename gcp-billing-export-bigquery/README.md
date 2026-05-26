# Exportação do Cloud Billing para BigQuery

Projeto de documentação do processo de exportação dos dados de faturamento do Google Cloud para o BigQuery.

> Data da documentação: 2026-05-25

## Objetivo

Registrar, de forma organizada e reutilizável, o passo a passo para configurar a exportação de dados do **Cloud Billing** para o **BigQuery**, permitindo análise de custos, serviços mais caros, projetos com maior consumo e evolução diária dos gastos.

## Arquitetura do processo

```text
Google Cloud Billing
        ↓
Billing Export
        ↓
BigQuery Dataset
        ↓
Tabelas automáticas de faturamento
        ↓
Consultas SQL / Relatórios / Dashboards
```

## Principais pontos considerados

### 1. Projeto separado para FinOps

Foi considerado como boa prática manter os dados de faturamento em um projeto específico, por exemplo:

```text
finops-billing-monitoring
```

Isso facilita a organização, o controle de permissões e a separação dos dados financeiros dos projetos de aplicação.

### 2. Dataset dedicado no BigQuery

Foi proposto o dataset:

```text
billing_export
```

Ele será usado apenas para armazenar as tabelas geradas automaticamente pela exportação do Cloud Billing.

### 3. Localização do dataset

Para laboratório, foi sugerida uma localização multi-região, como:

```text
US
```

Motivo: em exportações padrão ou detalhadas, datasets multi-região como `US` ou `EU` podem receber dados retroativos do mês atual e do mês anterior quando a exportação é ativada pela primeira vez. Em datasets regionais compatíveis, os dados normalmente começam a partir da data de ativação da exportação.

### 4. Tipos de exportação

Foram considerados três tipos principais:

| Tipo de exportação | Uso recomendado |
|---|---|
| Standard usage cost | Análise geral de custos por projeto, serviço, SKU, data e moeda |
| Detailed usage cost | Análise mais granular, incluindo dados em nível de recurso quando disponíveis |
| Pricing data | Consulta de informações de preços e SKUs |

Para um laboratório de portfólio, recomenda-se habilitar pelo menos **Standard usage cost**. Para análise mais robusta, habilite também **Detailed usage cost** e **Pricing data**.

### 5. Atenção a custos do BigQuery

A exportação para o BigQuery pode gerar custos mínimos de armazenamento e consulta. Por isso, as consultas SQL deste repositório usam filtros por data e agrupamentos simples.

## Passo a passo resumido

1. Criar ou selecionar um projeto para dados FinOps.
2. Ativar faturamento nesse projeto.
3. Criar dataset no BigQuery.
4. Acessar **Billing > Billing export**.
5. Ir na aba **BigQuery export**.
6. Clicar em **Edit settings** no tipo de exportação desejado.
7. Selecionar o projeto e o dataset.
8. Salvar a configuração.
9. Aguardar a criação automática das tabelas.
10. Validar os dados com consultas SQL.

## Tabelas esperadas

As tabelas são criadas automaticamente pelo Google Cloud após a ativação da exportação:

```text
gcp_billing_export_v1_<BILLING_ACCOUNT_ID>
gcp_billing_export_resource_v1_<BILLING_ACCOUNT_ID>
cloud_pricing_export
```

A tabela `gcp_billing_export_v1_<BILLING_ACCOUNT_ID>` é usada para custos padrão.  
A tabela `gcp_billing_export_resource_v1_<BILLING_ACCOUNT_ID>` é usada para custos detalhados.  
A tabela `cloud_pricing_export` é usada para dados de preços.

## Evidências / Prints

Os prints devem ser salvos em:

```text
docs/prints/
```

Sugestão de evidências:

| Arquivo | Evidência |
|---|---|
| `01-billing-export-menu.png` | Tela do menu Billing export |
| `02-criacao-dataset-bigquery.png` | Criação ou seleção do dataset no BigQuery |
| `03-configuracao-standard-export.png` | Configuração do Standard usage cost |
| `04-configuracao-detailed-export.png` | Configuração do Detailed usage cost |
| `05-tabelas-criadas-bigquery.png` | Tabelas criadas automaticamente no BigQuery |
| `06-consulta-validacao-custos.png` | Consulta SQL validando os custos exportados |

> Os prints incluídos neste repositório são modelos visuais. Substitua-os pelos prints reais do seu ambiente GCP antes de entregar o projeto.

## Consultas SQL incluídas

As consultas estão na pasta `sql/`:

```text
01_custo_total_mes.sql
02_custo_por_projeto.sql
03_custo_por_servico.sql
04_custo_diario.sql
05_creditos_e_descontos.sql
06_validacao_tabelas.sql
```

Antes de executar, substitua:

```text
SEU_PROJECT_ID.billing_export.gcp_billing_export_v1_SEU_BILLING_ACCOUNT_ID
```

pelo caminho real da sua tabela no BigQuery.

## Como subir no GitHub

```bash
git init
git add .
git commit -m "Documenta exportacao do Cloud Billing para BigQuery"
git branch -M main
git remote add origin https://github.com/seu-usuario/gcp-billing-export-bigquery.git
git push -u origin main
```

## Observações importantes

- A exportação não é instantânea; pode levar algumas horas para as primeiras tabelas aparecerem.
- Em casos de backfill retroativo, a carga completa pode levar até alguns dias.
- Não altere manualmente as tabelas criadas pela exportação do Cloud Billing.
- Para evitar que consultas quebrem com mudanças futuras de schema, uma boa prática é criar views de normalização.
- O uso de labels nos recursos do GCP melhora muito a análise de custos por área, ambiente, sistema ou responsável.
