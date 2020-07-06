


# ip

devem se testado os ip, para descobrir que o ip do container e qual o ip da maquina real.
investigar o ip pelo docker inspect.


# container
192.168.56.1


# host real
172.28.0.1


# test wsdl do host real via continer docker
curl http://172.28.0.1:7018/ws-linhaIndividual/NumeracaoLIService?wsdl