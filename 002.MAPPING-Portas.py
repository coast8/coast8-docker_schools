

***************************************************************************************
# Docker Toolbox 
***************************************************************************************

"""
por padrão o docker TooBox não escuta em 127.0.0.1
o mesmo escuta em `192.168.99.100`
"""

http://192.168.99.100:8080/



***************************************************************************************
# Comandos
***************************************************************************************

"""
-p, é o parametro usado para sinalizar o mapeamento.
"""

docker run -d -p 8080:80 -it nginx bash 
docker run -d -p 8080:80 -v /c/Development/vol1:usr/share/nginx/html nginx




*****************************
# FONTES:
*****************************

https://stackoverflow.com/questions/36530905/cant-access-apache-on-docker-from-my-localhost/36551016


*****************************
# 1 Bugs
*****************************

"""
Host não encontra o ip do docker. Como resolver?
"""
https://pt.stackoverflow.com/questions/257536/host-n%C3%A3o-encontra-o-ip-do-docker-como-resolver

https://pt.stackoverflow.com/questions/415265/problemas-em-acessar-a-aplica%C3%A7%C3%A3o-pelo-browser

https://cursos.alura.com.br/forum/topico-docker-for-windows-nao-acessa-pelo-localhost-59249
