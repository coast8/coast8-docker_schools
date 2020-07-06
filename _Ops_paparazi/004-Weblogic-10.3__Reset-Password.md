

# Reset Password

### 0- 
Variaveis de Ambientes

MWHOME :

	export MWHOME=/u01/oracle/weblogic

DOMAIN_HOME:

	export DOMAIN_HOME=$MWHOME/user_projects/domains/base_domain


### 1 - 
Devemos executar o script setDomainEnv.sh, para que todas as variáveis do Weblogic sejam carregadas de forma correta no S.O.

Para executar este script entre no diretório cd $DOMAIN_HOME/bin e execute o script com o comando ./setDomainEnv.sh, a tela abaixo ilustra este passo:


### 2- 
Iremos fazer um backup do atual arquivo do provedor de autenticação default, pois no processo para se criar um novo usuário e senha, será criado um novo arquivo de autenticação.

Entre no diretório security de seu domínio, usando o comando cd $DOMAIN_HOME/security em seguida mova o arquivo atual para outro nome com o comando: mv DefaultAuthenticatorInit.ldift oldDefaultAuthenticator.ldift

### 3-
Agora iremos rodar o comando que irá criar um novo usuário e senha:

java weblogic.security.utils.AdminAccount weblogic welcome1 .


### 4-
Após executar o comando veja que foi criado um novo arquivo DefaultAuthenticatorInit.ldift:



### 5-
Vamos mover a pasta data do servidor gerenciado e apagar o arquivo boot.properties:

Entre no diretório cd $DOMAIN_HOME/servers/AdminServer

Mova a pasta data com o comando mv data/ dataold/


### 6-
Entre na pasta security do AdminServer e remova o arquivo boot.properties:



### 7-
Inicialize o Weblogic, neste ponto você deverá informar o novo usuário e senha criados anteriormente:



# fontes and helpers
https://obieebrasil.wordpress.com/2012/10/22/resetar-senha-perdida-do-weblogic/