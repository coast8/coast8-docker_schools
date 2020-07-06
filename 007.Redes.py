


***************************************************************************************
# REDES
***************************************************************************************


"""
TIPOD DE REDES

	- None NetWork
	- Bridge (Default)
	- Host
	- Overlay (Swarm)

"""

docker network ls                                   	# list redes.
docker network inspect bridge							# inspecionando a rede.
docker container run -d --net none debian               # container no modo none network.


"""
Devemos verificar as interfaces de rede do container:

ifconfig
	- inet IP de acesso a REDE.
	- lo = Interface de LOOPBACK, não se comunicar com outros containers e nem tem acesso a internet.
"""




***************************************************************************************
# CRIANDO UMA NOVA REDE
***************************************************************************************

"""
references, cod3r, cap 6. Aula 43.
"""

docker network create --drive bridge rede_nova             	# criando uma nova rede.
docker network ls 											# listando as redes.
docker network inspect rede_nova 							# ver as faixas de rede.
docker network connect bridge container_name                # connectando conteiner a outra rede.
docker conteiner exec -it container_name ifconfig           # ver as interfaces das duas redes que o mesmo tem acesso.




***************************************************************************************
# REDE DO TIPO HOST
***************************************************************************************

"""
Essa rede fica na mesma camada que o host fisico
"""

docker conteiner run -d --name container4 --net host alpine sleep 1000      # cria e executa o container.
docker conteiner exec -it container4 ifconfig                             	# ver interfaces de redes.