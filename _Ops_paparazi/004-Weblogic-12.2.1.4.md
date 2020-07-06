

##########################################
# step 1 - baixando a imagem
##########################################

docker run -d -i -t -p 7002:7001 -p 9004:9002 -v /c/Users/55869/vol-weblogic12:/u01/oracle/properties store/oracle/weblogic:12.2.1.4 /bin/bash


###
###  desciption step 1

### portas 	=>	 	p 7002:7001 -p 9004:9002
### volume 	=> 		/c/Users/55869/vol-weblogic12:/u01/oracle/properties
### IMG DOCKER =>		store/oracle/weblogic:12.2.1.4
 
 

##########################################
# step 2 - Mapeando senhas 
##########################################

### O arquivo para o mapeamento de senhas `domain.properties`
### localizado em `/u01/oracle/properties`
### padrao user e password 

cd /u01/oracle/properties

username=weblogic
password=welcome1




##########################################
# step 3 - Create Domain
##########################################

### arquivo para python para a cração do dominio `create-wls-domain.py`
### localizado em `/u01/oracle`
### deves alterar o script com os dados do seu dominio

### depois deve executa o comando `sh createAndStartEmptyDomain.sh`
### este comando cria o dominio 




##########################################
# step 4 - Start Web Logic
##########################################

### acesse o dominio criado no step 3 
### start o WebLogic

cd /u01/oracle/user_projects/domains/my_domain

sh startWebLogic.sh

http://192.168.99.100:7001/console



FONTES:

# Docker Hub
https://hub.docker.com/u/asmythy/content/sub-9d436ec1-5033-400c-9b04-a50913a1ebb2
 
# start weblogic
https://github.com/oracle/docker-images/issues/1517	

# acessar console weblogic - corrigi erro sem permissao
https://github.com/oracle/docker-images/issues/1026

# Configurando Debug Remoto com Eclipse e Weblogic 12.
http://www.ciceroednilson.com.br/configurando-debug-remoto-com-eclipse-e-weblogic-12/

# Configurando o WebLogic com interface grafica
https://www.oracle.com/webfolder/technetwork/tutorials/obe/fmw/wls/12c/12_1_3/01/installwls.html