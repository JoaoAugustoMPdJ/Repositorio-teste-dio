# Política Simples de Controle de Custos na GCP

Esta política tem como objetivo orientar o uso seguro da GCP em ambientes de estudo, laboratório e portfólio.

## 1. Orçamentos obrigatórios

Todo projeto criado na GCP deve possuir um orçamento associado ou estar coberto por um orçamento da conta de faturamento.

## 2. Alertas mínimos

Todo orçamento deve possuir alertas em pelo menos três níveis:

- 50%: alerta inicial de acompanhamento;
- 75%: alerta de atenção;
- 90%: alerta crítico;
- 100%: orçamento totalmente consumido.

## 3. Revisão de recursos

Quando um alerta for recebido, devem ser verificados:

- máquinas virtuais ativas;
- discos persistentes;
- endereços IP externos reservados;
- clusters Kubernetes;
- serviços serverless com uso inesperado;
- buckets com armazenamento elevado;
- BigQuery, Vertex AI ou outros serviços de maior custo.

## 4. Evidências

Para fins de documentação, devem ser salvos prints das configurações do orçamento e do painel de custos.

## 5. Segurança antes de publicar

Nenhum print público deve expor dados sensíveis, como conta de faturamento, forma de pagamento, e-mails privados ou informações de clientes.
