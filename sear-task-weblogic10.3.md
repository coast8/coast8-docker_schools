

== imagem padrao da oracle

docker run -d -i -t -p 7002:7001 -p 9004:9002 -v /c/Users/55869/vol-weblogic12:/u01/oracle/properties store/oracle/weblogic:10.3.6 /bin/bash


docker run -d -i -t -p 7002:7001 -p 9004:9002 guok/weblogic-10.3.5 /bin/bash


docker run -d -i -t -p 7002:7001 -p 9004:9002 daniloichaves/weblogic-10.3.6-base /bin/bash


== drexduarte ok 
docker run -d -i -t -p 7002:7001 -p 9004:9002 drexduarte/weblogic-10.3.6 /bin/bash 

commit

docker run -d -i -t -p 7002:7001 -p 9004:9002 -v /c/Users/55869/vol-weblogic11:/home as-wl-10.3.6 /bin/bash 

docker run -p 8080:8080 -td test02

== v2 do container
== com NI
== com DataSouces
== com Mapeamento portas WEbLogic e Terus
docker run -d -i -t -p 7001:7001 -p 9002:9002 -p 7018:7018 -v /c/Users/55869/vol-weblogic11:/home as-wl-10.3.6_v2 /bin/bash 

== shared volume
/u01/oracle/weblogic/user_projects/domains/base_domain


java.io.FileNotFoundException: C:/oracle/Middleware/user_projects/domains/base_domain/servers
/AdminServer/logs/NumberInventoryServices.log (No such file or directory)

ssh -L 7018:10.27.80.15:7018 10.41.254.249 

ssh -L 7018:10.27.80.15:7018 10.41.254.249 

== end helpers
https://hub.docker.com/r/drexduarte/weblogic-10.3.6
https://obieebrasil.wordpress.com/2012/10/22/resetar-senha-perdida-do-weblogic/




docker run -d -i -t -p 7002:7001 -p 9004:9002 drexduarte/weblogic-10.3.6 /bin/bash


docker run -d -i -t -p 7002:7001 -p 9004:9002 af233a505351 /bin/bash




docker pull 
docker run -d -i -t -p 7002:7001 -p 9004:9002 iwanttobefreak/weblogic1036 /bin/bash


docker build . --build-arg ORACLE_USER= --build-arg ORACLE_PASSWORD= -t myweblogic1036 docker-weblogic1036


docker pull fengzhou/docker-weblogic-1036:latest
docker run -d -i -t -p 7002:7001 -p 9004:9002 fengzhou/docker-weblogic-1036:latest /bin/bash


docker build --build-arg SMB_PASS=swed24sw --build-arg SMB_USER=Ubuntu . -t IMAGE_TAG





= docker hub weblogic 10
https://hub.docker.com/search?q=weblogic-10.3&type=image

https://hub.docker.com/search?q=weblogic%2010.3&type=image

https://stackoverflow.com/questions/42297387/docker-build-with-build-arg-with-multiple-arguments

https://stackoverflow.com/questions/37234940/centos-locate-command-doesnt-work


