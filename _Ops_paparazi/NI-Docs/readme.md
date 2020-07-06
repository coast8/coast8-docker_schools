
************************************
--            Config              --
************************************



# Step 1 - Usar o amigem base

o comando abaixo contem mapeamento das portas, mapeamento dos volumes e terminal bash. OBs: Altere o mapeamento do volume para o local do seu volume em seu pc.



	docker run -d -i -t -p 7002:7001 -p 7018:7018 -p 9004:9002 -p 4011:4011 -v /c/Users/asmythy/docker-files/vol-weblogic11:/home wl-10.3.6_v1.2 /bin/bash 



# Step 2 - Alteração no WSDL do Terus

pesquisar por `ws-linhaIndividual` no NI, e altere de `127.0.0.1` para `172.28.0.1`, se você acessar na url este caminho, notara que é o wsdl do terus, não se esqueça de abrir o tunel do Terus :).

	antigo  =>	http://127.0.0.1:7018/ws-linhaIndividual/NumeracaoLIService?wsdl

	novo 	=>	http://172.28.0.1:7018/ws-linhaIndividual/NumeracaoLIService?wsdl



# Step 3 - Start WebLogic

	sh /u01/oracle/weblogic/user_projects/domains/base_domain/startWebLogic.sh



# Step 4 - Credencias

	weblogic
	welcome1


# Step 5 - Configurar o Dubug no Eclipse

evidecia-001.PNG



# Step 6 - Testando Aplicação

teste sisnum 		=>		evidecia-002.PNG
teste terus, sigan 	=>		evidecia-003.PNG