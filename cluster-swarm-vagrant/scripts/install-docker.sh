#!/bin/bash

echo "Atualizando pacotes do sistema..."

apt-get update -y

echo "Instalando dependências..."

apt-get install -y ca-certificates curl gnupg lsb-release

echo "Configurando repositório oficial do Docker..."

install -m 0755 -d /etc/apt/keyrings

if [ ! -f /etc/apt/keyrings/docker.gpg ]; then
  curl -fsSL https://download.docker.com/linux/ubuntu/gpg | \
  gpg --dearmor -o /etc/apt/keyrings/docker.gpg
fi

chmod a+r /etc/apt/keyrings/docker.gpg

echo \
"deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
$(lsb_release -cs) stable" | \
tee /etc/apt/sources.list.d/docker.list > /dev/null

echo "Instalando Docker..."

apt-get update -y

apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

echo "Habilitando Docker na inicialização..."

systemctl enable docker
systemctl start docker

echo "Adicionando usuário vagrant ao grupo docker..."

usermod -aG docker vagrant

echo "Docker instalado com sucesso."