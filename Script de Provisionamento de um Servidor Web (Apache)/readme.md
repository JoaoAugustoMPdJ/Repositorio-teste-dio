# Provisionamento de Servidor Web com Apache

Este projeto tem como objetivo automatizar o provisionamento de um servidor web utilizando um script Bash.

O script realiza a instalação e configuração do Apache, permitindo que uma nova máquina Linux seja preparada automaticamente para hospedar páginas web.

## Tecnologias utilizadas

- Linux
- Bash Script
- Apache HTTP Server
- GitHub

## Funcionalidades do script

- Atualiza os pacotes do sistema
- Instala o Apache
- Instala pacotes auxiliares, como `wget` e `unzip`
- Habilita o serviço do Apache
- Inicia o servidor web
- Remove a página padrão do Apache
- Publica uma página HTML personalizada
- Ajusta permissões do diretório `/var/www/html`

## Como executar

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
```
## Acesse o diretório:

### cd seu-repositorio

## Dê permissão de execução ao script:
```bash
chmod +x provisionar-servidor-web.sh
```
Execute o script:

```bash
sudo ./provisionar-servidor-web.sh
```
## Como acessar

Após a execução do script, acesse o endereço IP da máquina no navegador:

```bash
http://IP-DA-MAQUINA
```

## Objetivo

Este projeto demonstra o uso de Infraestrutura como Código para automatizar a configuração de servidores, tornando o processo mais rápido, padronizado e reutilizável.


## Comandos para enviar ao GitHub

```bash
git init
git add .
git commit -m "Adiciona script de provisionamento de servidor web"
git branch -M main
git remote add origin https://github.com/seu-usuario/seu-repositorio.git
git push -u origin main
```