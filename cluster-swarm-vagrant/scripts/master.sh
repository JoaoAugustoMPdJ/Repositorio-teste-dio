#!/bin/bash

MASTER_IP="192.168.56.10"

echo "Configurando nó master do Docker Swarm..."

if docker info | grep -q "Swarm: active"; then
  echo "Swarm já está ativo no master."
else
  docker swarm init --advertise-addr $MASTER_IP

  echo "Swarm iniciado no master."
fi

echo "Gerando token para os workers..."

WORKER_TOKEN=$(docker swarm join-token -q worker)

cat > /vagrant/join-worker.sh <<EOF
#!/bin/bash
docker swarm join --token $WORKER_TOKEN $MASTER_IP:2377
EOF

chmod +x /vagrant/join-worker.sh

echo "Arquivo de entrada dos workers criado em /vagrant/join-worker.sh"