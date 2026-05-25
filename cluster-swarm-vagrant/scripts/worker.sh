#!/bin/bash

echo "Configurando worker do Docker Swarm..."

if docker info | grep -q "Swarm: active"; then
  echo "Este nó já faz parte do Swarm."
  exit 0
fi

echo "Aguardando o master gerar o token..."

while [ ! -f /vagrant/join-worker.sh ]; do
  sleep 5
done

echo "Entrando no cluster Swarm como worker..."

bash /vagrant/join-worker.sh

echo "Worker adicionado ao cluster com sucesso."