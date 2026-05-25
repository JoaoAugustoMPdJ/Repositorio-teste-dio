#!/bin/bash

echo "Iniciando o provisionamento do servidor web..."

# Verifica se o script está sendo executado como root
if [ "$EUID" -ne 0 ]; then
  echo "Execute este script como root ou usando sudo."
  exit 1
fi

echo "Atualizando os pacotes do sistema..."

apt-get update -y
apt-get upgrade -y

echo "Instalando o Apache..."

apt-get install apache2 -y

echo "Instalando o Unzip..."

apt-get install unzip -y

echo "Instalando o Wget..."

apt-get install wget -y

echo "Habilitando e iniciando o serviço Apache..."

systemctl enable apache2
systemctl start apache2

echo "Removendo página padrão do Apache..."

rm -rf /var/www/html/*

echo "Criando página web personalizada..."

cat <<EOF > /var/www/html/index.html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Servidor Web Provisionado</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            text-align: center;
            padding-top: 100px;
        }

        h1 {
            color: #2c3e50;
        }

        p {
            color: #555;
            font-size: 18px;
        }
    </style>
</head>
<body>
    <h1>Servidor Web Apache configurado com sucesso!</h1>
    <p>Este servidor foi provisionado automaticamente por meio de um script Bash.</p>
    <p>Projeto de Infraestrutura como Código.</p>
</body>
</html>
EOF

echo "Ajustando permissões do diretório web..."

chown -R www-data:www-data /var/www/html
chmod -R 755 /var/www/html

echo "Verificando status do Apache..."

systemctl status apache2 --no-pager

echo "Provisionamento concluído com sucesso!"
echo "Acesse o servidor pelo navegador usando o IP da máquina."