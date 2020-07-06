

***************************************************************************************
# 1.0 Comandos docker basicos
***************************************************************************************
docker ps         										# listando containers ativos
docker ps -a 											# listando todos os containers
docker images     										# listando images
docker start CONTAINER_ID                               # startando um container
docker stop CONTAINER_ID 								# finalizando o container
docker attach CONTAINER_ID                              # entrando no container
docker container run --name mydeb -it debian bash 		# Renomeando Container
docker inspect CONTAINER_ID                             # inspecionando o container
docker exec CONTAINER_ID comando_linux_bash             # executando um comando de fora do container
docker status CONTAINER_ID                              # ver consumo de cpu



***************************************************************************************
# 2.0 baixando o ubunto
***************************************************************************************

"""
baixando o ubunto passando a versao e processo a ser startado.
se a imagem n existir localmente, ira baixar  no repositorio do docker.
"""


docker run -i -t ubuntu:14.10 /bin/bash



***************************************************************************************
# 3.0 Comandos linux basicos
***************************************************************************************

uname -a                 			# venda a dist linux
cat /etc/issue           			# venda a dist linux
ps -ef                   			# vendo o process executed
curl ip_container:porta_nginx 		# access nginx pelo host real





***************************************************************************************
# 4.0 Saindo do container e voltando para o container
***************************************************************************************
CTRL + D               			# encera, mata o container
CTRL + P + Q           			# sai mais deixa o conteiner ativo
docker ps 						# para pegar o CONTAINER_ID 
docker attach CONTAINER_ID      # Voltando para o container
docker diff CONTAINER_ID        # Verificando hitorico do container




***************************************************************************************
# 5.0 Montando um container
***************************************************************************************

docker run -i -t -p 8080:80 ubuntu:14.10 /bin/bash        # image docker
apt-get install nginx                                     # install nginx
ps -ef                                                    # processos
/etc/init.d/nginx start                                   # startando nginx
ps -ef                                                    # processos
netstat -atunp	                                          # verifica as portas
tail -f /var/log/nginx/access.log                         # log
CTRL + P + Q                                              # sai mais deixa o conteiner ativo
localhost:8080                                            # access nginx




***************************************************************************************
# 6.0 Salvando modificações, commit container
***************************************************************************************
"""
as modificacoes feitas no container devem  ser commitadas, senao seram todas pedidas quando sair
do container."""


docker commit CONTAINER_ID badtux/nginx-ubuntu:1.0        # commitando o conteiner





***************************************************************************************
# 7.0 Excluindo container
***************************************************************************************

docker rm CONTAINER_ID
docker rm -f CONTAINER_ID





***************************************************************************************
# 8.0 Excluindo imagem
***************************************************************************************

docker rmi IMAGE_ID
docker rmi -f IMAGE_ID

