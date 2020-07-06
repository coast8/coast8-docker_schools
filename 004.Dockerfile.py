

***************************************************************************************
# 1.0  O que é o Dockerfile ?
***************************************************************************************


"""
O Dockerfile nada mais é do que um meio que utilizamos para criar nossas próprias imagens. 
Em outras palavras, ele serve como a receita para construir um container, 
permitindo definir um ambiente personalizado e próprio para meu projeto pessoal ou empresarial.

"""


***************************************************************************************
# DockerFile
***************************************************************************************

"""
Então, iniciei o processo de criação da imagem. Para isso, abri o terminal e acessei a 
pasta que contém o Dockerfile. 
Após isso, executei o comando `docker build .` (com o ponto) e o docker começou a construir a 
imagem a partir do arquivo.
"""

docker build . -t badtux/nginx-ubuntu:1.0 .              	# usando dockerflile p criar image
docker run -it badtux/nginx-ubuntu:1.0 /bin/bash       		# rodando container
pf -ef          											# cmds unix
netstat -atunp												# cmds unix




***************************************************************************************
# Entendendo as instruções do Dockerfile
***************************************************************************************

"""

https://www.alura.com.br/artigos/desvendando-o-dockerfile#:~:text=O%20Dockerfile%20nada%20mais%20%C3%A9,meu%20projeto%20pessoal%20ou%20empresarial.

"""



***************************************************************************************
# passasndo parametros para o Dockerfile
***************************************************************************************
"""

references, livro da cod3r, 4.6. Construção de uma imagem, pag 22



documentação:
	https://docs.docker.com/engine/reference/builder/


Automatizacao do Container
	https://woliveiras.com.br/posts/Criando-uma-imagem-Docker-personalizada/
"""