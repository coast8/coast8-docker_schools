

##########################################
# step 1 - baixando a imagem
##########################################


A imagem escolhida para usar como base para o container `https://hub.docker.com/r/drexduarte/weblogic-10.3.6`.


	docker run -d -i -t -p 7002:7001 -p 9004:9002 -v /c/Users/asmythy/docker-files/vol-weblogic11:/home drexduarte/weblogic-10.3.6 /bin/bash 



# Start
sh /u01/oracle/weblogic/user_projects/domains/base_domain/startWebLogic.sh



# commit

docker stop test01
docker commit drexduarte/weblogic-10.3.6 wl-10.3.6_v1.0
docker run -p 8080:8080 -td test02


docker run -d -i -t -p 7002:7001 -p 7018:7018 -p 9004:9002 -v /c/Users/asmythy/docker-files/vol-weblogic11:/home wl-10.3.6_v1.0 /bin/bash 




# fontes and helpers
https://hub.docker.com/r/drexduarte/weblogic-10.3.6
