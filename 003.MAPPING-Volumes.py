
***************************************************************************************
# Docker Toolbox 
***************************************************************************************

"""
por padrão o docker TooBox recebe os volumes do host 127.0.0.1
da pasta c:users
"""



***************************************************************************************
# Comandos
***************************************************************************************

"""
A tag -v, é usado para sinalizar o uso do mapeamento de volume.
pc fisico/container docker
"""

docker run -d -p 8080:80 -v /c/Users/55869/vol1/not:/usr/share/nginx/html nginx
docker run -d -p 8080:80 -v $(pwd)/vol1/not:/usr/share/nginx/html nginx





***************************************************************************************
# docker tool box
***************************************************************************************


"""
No docker tool box, para acessa o conteiner, devemos utilizar o IP  192.168.99.100.
caso use localhost, não dara certo.
"""

192.168.99.100  											# ip docker tool box
ping host.docker.internal									# ping dinaminc ip in widows





***************************************************************************************
# Refereces:
***************************************************************************************

https://docs.docker.com/toolbox/toolbox_install_windows/#optional-add-shared-directories
mundodocker.com.br/montando-volumes-docker/




