

# Lista de comandos basicos

## listando todos os containers
	docker ps -a

## listando images
	docker images

## startando um container
	docker start CONTAINER_ID

## entrando no container
	docker attach CONTAINER_ID

## parando o container
	docker stop CONTAINER_ID

## inspecionando o container
	docker inspect CONTAINER_ID

## executando um comando de fora do container
	docker exec CONTAINER_ID comando_linux_bash