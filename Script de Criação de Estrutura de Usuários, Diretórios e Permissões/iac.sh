#!/bin/bash

echo "Iniciando criação da infraestrutura..."

# Verifica se o script está sendo executado como root
if [ "$EUID" -ne 0 ]; then
  echo "Execute este script como root."
  exit 1
fi

# Senha inicial dos usuários
SENHA_PADRAO="Senha123"

echo "Criando diretórios..."

mkdir -p /publico
mkdir -p /adm
mkdir -p /ven
mkdir -p /sec

echo "Criando grupos de usuários..."

getent group GRP_ADM > /dev/null || groupadd GRP_ADM
getent group GRP_VEN > /dev/null || groupadd GRP_VEN
getent group GRP_SEC > /dev/null || groupadd GRP_SEC

echo "Criando usuários..."

criar_usuario() {
  USUARIO=$1
  GRUPO=$2

  if id "$USUARIO" &>/dev/null; then
    echo "Usuário $USUARIO já existe. Pulando..."
  else
    useradd "$USUARIO" -m -s /bin/bash -G "$GRUPO"
    echo "$USUARIO:$SENHA_PADRAO" | chpasswd
    passwd -e "$USUARIO"
    echo "Usuário $USUARIO criado e adicionado ao grupo $GRUPO."
  fi
}

# Usuários do grupo administrativo
criar_usuario carlos GRP_ADM
criar_usuario maria GRP_ADM
criar_usuario joao GRP_ADM

# Usuários do grupo de vendas
criar_usuario debora GRP_VEN
criar_usuario sebastiana GRP_VEN
criar_usuario roberto GRP_VEN

# Usuários do grupo de secretaria
criar_usuario josefina GRP_SEC
criar_usuario amanda GRP_SEC
criar_usuario rogerio GRP_SEC

echo "Definindo permissões dos diretórios..."

chown root:GRP_ADM /adm
chown root:GRP_VEN /ven
chown root:GRP_SEC /sec
chown root:root /publico

chmod 770 /adm
chmod 770 /ven
chmod 770 /sec
chmod 777 /publico

echo "Infraestrutura criada com sucesso!"
echo "Usuários criados com senha inicial: $SENHA_PADRAO"
echo "A senha deverá ser alterada no primeiro login."