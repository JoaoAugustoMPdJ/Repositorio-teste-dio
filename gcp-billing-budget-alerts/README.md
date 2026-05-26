# Controle de Orçamentos e Alertas no Painel de Faturamento da GCP

Este repositório documenta a configuração de **controle de orçamento e alertas de faturamento** no Google Cloud Platform (GCP), com o objetivo de reduzir riscos de gastos inesperados em projetos de laboratório, portfólio e ambientes de estudo.

> Observação: este repositório foi preparado como documentação de evidência. Os prints reais devem ser substituídos pelos screenshots do seu próprio Console da GCP após a configuração no painel de faturamento.

---

## Objetivo do projeto

Criar e documentar um orçamento no **Cloud Billing** da GCP com alertas por percentual de consumo, permitindo acompanhar a evolução dos custos e agir antes que o orçamento seja ultrapassado.

---

## Pontos considerados na configuração

Para este projeto, foram considerados os seguintes pontos:

1. **Escopo do orçamento**  
   O orçamento deve estar vinculado ao projeto ou à conta de faturamento correta. Para ambientes de estudo, é recomendado criar orçamento por projeto para facilitar o acompanhamento individual.

2. **Valor do orçamento**  
   O valor deve ser baixo e compatível com o objetivo do laboratório. Exemplo sugerido: R$ 50,00 ou valor equivalente na moeda da conta de faturamento.

3. **Alertas progressivos**  
   Foram definidos alertas em diferentes níveis para permitir ação antecipada:
   - 50% do orçamento;
   - 75% do orçamento;
   - 90% do orçamento;
   - 100% do orçamento.

4. **Alerta por previsão de gasto**  
   Além dos alertas por gasto real, pode ser configurado um alerta baseado em gasto previsto, por exemplo, quando a projeção indicar que o orçamento será ultrapassado até o fim do período.

5. **Notificações por e-mail**  
   Os alertas devem ser enviados para administradores de faturamento, usuários responsáveis pelo projeto e, se necessário, canais adicionais configurados no Cloud Monitoring.

6. **Registro de evidências**  
   Os prints salvos neste repositório servem como evidência de configuração do orçamento, dos limites de alerta e da tela de acompanhamento dos custos.

7. **Limitação importante**  
   O orçamento da GCP gera alertas, mas não bloqueia automaticamente o consumo. Portanto, o orçamento deve ser entendido como um mecanismo de monitoramento, não como um limite rígido de cobrança.

---

## Configuração sugerida

| Item | Configuração recomendada |
|---|---|
| Nome do orçamento | `orcamento-laboratorio-gcp` |
| Escopo | Projeto específico ou conta de faturamento |
| Período | Mensal |
| Valor | R$ 50,00 ou valor definido pelo usuário |
| Alerta 1 | 50% do orçamento - gasto real |
| Alerta 2 | 75% do orçamento - gasto real |
| Alerta 3 | 90% do orçamento - gasto real |
| Alerta 4 | 100% do orçamento - gasto real |
| Alerta adicional | 100% do orçamento - gasto previsto |
| Notificação | E-mail para administradores/responsáveis |

---

## Evidências / prints

Os prints devem ser salvos na pasta [`docs/prints`](docs/prints).  
Os arquivos de exemplo neste repositório são modelos visuais e devem ser substituídos pelos prints reais da sua conta GCP.

Sugestão de evidências:

| Arquivo | Descrição |
|---|---|
| `01-painel-faturamento.png` | Tela inicial do painel de faturamento |
| `02-criacao-orcamento.png` | Tela de criação/configuração do orçamento |
| `03-limites-alerta.png` | Tela com os limites de alerta configurados |
| `04-resumo-orcamento.png` | Tela final com orçamento ativo |
| `05-relatorio-custos.png` | Relatório de custos vinculado ao orçamento |

---

## Passo a passo resumido

1. Acessar o Console da GCP.
2. Entrar em **Billing / Faturamento**.
3. Acessar **Budgets & alerts / Orçamentos e alertas**.
4. Clicar em **Create budget / Criar orçamento**.
5. Definir o escopo do orçamento.
6. Definir o valor mensal do orçamento.
7. Criar limites de alerta em 50%, 75%, 90% e 100%.
8. Configurar os destinatários das notificações.
9. Salvar o orçamento.
10. Registrar os prints de evidência na pasta `docs/prints`.

---

## Estrutura do repositório

```text
.
├── README.md
├── docs/
│   ├── checklist-configuracao.md
│   ├── politica-controle-custos.md
│   ├── passo-a-passo-console-gcp.md
│   └── prints/
│       ├── README.md
│       ├── 01-painel-faturamento.png
│       ├── 02-criacao-orcamento.png
│       ├── 03-limites-alerta.png
│       ├── 04-resumo-orcamento.png
│       └── 05-relatorio-custos.png
└── scripts/
    └── budget-api-template.json
```

---

## Boas práticas adotadas

- Separar orçamento por projeto quando o objetivo é controlar laboratórios independentes.
- Usar alertas progressivos, evitando ser notificado apenas quando o orçamento já foi totalmente consumido.
- Definir orçamento abaixo do valor máximo disponível, considerando atrasos de contabilização de uso.
- Documentar evidências com prints para facilitar auditoria e apresentação do projeto.
- Evitar expor dados sensíveis da conta de faturamento em prints públicos.

---

## O que ocultar antes de publicar no GitHub

Antes de subir os prints reais para o GitHub, confira se não aparecem:

- ID completo da conta de faturamento;
- dados de cartão ou forma de pagamento;
- e-mails pessoais que você não deseja expor;
- nome de organização privada;
- valores financeiros sensíveis;
- projetos de clientes ou terceiros.

Caso apareçam, oculte ou borre essas informações antes de publicar.

---

## Conclusão

A criação de alertas e orçamento no painel de faturamento da GCP é uma prática essencial para ambientes cloud, pois permite acompanhar custos, identificar desvios e reduzir riscos financeiros durante testes, estudos e projetos em nuvem.
