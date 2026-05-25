# Infraestrutura como Código - Linux

Este projeto contém um script Bash responsável por criar automaticamente uma infraestrutura básica de usuários, grupos, diretórios e permissões em uma máquina Linux.

## Estrutura criada

### Diretórios

- /publico
- /adm
- /ven
- /sec

### Grupos

- GRP_ADM
- GRP_VEN
- GRP_SEC

### Usuários

#### Grupo GRP_ADM

- carlos
- maria
- joao

#### Grupo GRP_VEN

- debora
- sebastiana
- roberto

#### Grupo GRP_SEC

- josefina
- amanda
- rogerio

## Permissões

- O diretório `/publico` possui permissão total para todos os usuários.
- O diretório `/adm` é acessível apenas para usuários do grupo `GRP_ADM`.
- O diretório `/ven` é acessível apenas para usuários do grupo `GRP_VEN`.
- O diretório `/sec` é acessível apenas para usuários do grupo `GRP_SEC`.

## Como executar

```bash
chmod +x iac.sh
sudo ./iac.sh
```

## Objetivo

Automatizar a configuração inicial de uma máquina Linux, permitindo que a infraestrutura seja recriada de forma rápida, padronizada e reutilizável.