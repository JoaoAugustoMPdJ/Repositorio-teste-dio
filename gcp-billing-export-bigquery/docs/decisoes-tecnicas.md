# Decisões técnicas consideradas

## Separação do projeto de faturamento

Foi recomendado utilizar um projeto separado para armazenar dados de faturamento. Essa abordagem ajuda a:

- centralizar análises financeiras;
- controlar melhor permissões;
- evitar misturar dados de aplicação com dados administrativos;
- facilitar auditoria e governança.

## Escolha do BigQuery

O BigQuery foi escolhido porque é o destino nativo da exportação de Billing do Google Cloud e permite consultas analíticas usando SQL.

## Escolha do dataset

O dataset `billing_export` foi usado para manter uma nomenclatura simples, direta e fácil de identificar.

## Tipo de exportação

Foram documentadas três exportações:

1. **Standard usage cost**: suficiente para análises gerais.
2. **Detailed usage cost**: útil para granularidade por recurso.
3. **Pricing data**: útil para consulta de preços e SKUs.

## Cuidados com custos

Apesar de a exportação ser útil para análise, o armazenamento e as consultas no BigQuery podem gerar custos. Por isso:

- evite `SELECT *` em tabelas grandes;
- use filtros por data;
- crie views resumidas;
- limite consultas exploratórias;
- monitore o custo do próprio BigQuery.

## Cuidados com segurança

As evidências em prints podem conter dados sensíveis. Antes de publicar:

- oculte IDs de faturamento;
- oculte e-mails;
- não publique dados bancários;
- não publique chaves ou credenciais;
- revise os prints antes do commit.
