# Desafio de Projeto - Esquema Conceitual de E-commerce

## Descrição do Projeto
Este projeto apresenta o refinamento de um modelo conceitual para um sistema de e-commerce, com base nos requisitos propostos no desafio.

O objetivo foi expandir o modelo inicial acrescentando regras e entidades importantes para representar melhor o cenário de negócio, especialmente em relação aos tipos de cliente, formas de pagamento e processo de entrega.

## Objetivo do Refinamento
O modelo foi ajustado para contemplar os seguintes pontos:

- Cliente pode ser do tipo **Pessoa Física (PF)** ou **Pessoa Jurídica (PJ)**;
- Uma conta não pode possuir simultaneamente os dados de PF e PJ;
- Um cliente pode cadastrar **mais de uma forma de pagamento**;
- Cada pedido possui informações de **entrega**, incluindo **status** e **código de rastreio**.

## Decisões de Modelagem

### 1. Cliente PF e PJ
A entidade **Cliente** foi modelada com especialização em:
- **Cliente_PF**
- **Cliente_PJ**

Essa especialização é **disjunta**, pois um cliente não pode ser PF e PJ ao mesmo tempo.

### 2. Pagamento
Foi criada a entidade **Pagamento**, relacionada ao cliente, permitindo que um mesmo cliente cadastre várias formas de pagamento, como cartão, PIX ou boleto.

### 3. Entrega
Foi criada a entidade **Entrega**, associada ao pedido, contendo:
- status da entrega
- código de rastreio
- datas relacionadas ao envio

## Principais Entidades do Modelo
- Cliente
- Cliente_PF
- Cliente_PJ
- Pedido
- Produto
- Item_Pedido
- Pagamento
- Entrega

## Relacionamentos Principais
- Um cliente realiza vários pedidos;
- Um pedido possui vários itens;
- Um produto pode compor vários itens de pedido;
- Um cliente pode cadastrar várias formas de pagamento;
- Um pedido possui uma entrega;
- Um cliente é obrigatoriamente PF ou PJ, mas não ambos.

## Observação
O modelo foi desenvolvido no nível conceitual, priorizando a representação das regras de negócio do sistema de e-commerce.