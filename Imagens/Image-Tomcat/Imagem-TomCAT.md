



docker run -d -i -p 9090:8080 -v /c/Users/55869/vol-tomcat7:/tmp tomcat:7.0.85-jre7 /bin/bash

docker run -d -i -t -p 9090:8080 -v /c/Users/55869/vol-tomcat:/tmp ubuntu /bin/bash





docker run -d -p 7002:7001 -p 9004:9002 -v /c/Users/55869/vol-weblogic12:/u01/oracle/properties store/oracle/weblogic:12.2.1.4


docker run -d -i
-p 9090:8080 
-v /c/Users/55869/vol-tomcat7:/u01/oracle/properties store/oracle/weblogic:12.2.1.4
tomcat:7.0.85-jre7 
/bin/bash





42a3e0609323
$ 
docker exec 42a3e0609323 cat /etc/issue


/usr/share/tomcat7/bin/startup.sh





/usr/share/tomcat7 

docker exec 29387c77fa75 mv /tmp/tomcat7 /etc/init.d

docker exec 29387c77fa75 chmod 755 /etc/init.d/tomcat7

docker exec 29387c77fa75 update-rc.d /etc/init.d/tomcat7 defaults









====================================================
JAVA_HOME=/usr/lib/jvm/java-8-oracle/jre/bin/java
export JAVA_HOME
export PATH=$PATH:$JAVA_HOME
echo $JAVA_HOME
====================================================




====================================================
export VARIAVEL="VALOR"
export JAVA_HOME= "/usr/lib/jvm/java-8-openjdk-amd64"
export JRE_HOME=/usr/lib/jvm/java-8-openjdk-amd64/jre
====================================================




====================================================
CATALINA_HOME=/usr/local/tomcat8
export CATALINA_HOME
export PATH=$PATH:$CATALINA_HOME
echo $CATALINA_HOME
====================================================


# start tomcat
/usr/local/tomcat8/bin/startup.sh


# referece
https://tecadmin.net/install-oracle-java-8-ubuntu-via-ppa/
http://michelsjava.blogspot.com/2017/08/configurar-o-javahome-path-no-ubuntu.html



https://tecadmin.net/install-tomcat-8-on-centos-rhel-and-ubuntu/
https://www.liquidweb.com/kb/install-apache-tomcat-8-ubuntu-16-04/




 cp artigo-jsf-primefaces-fileupload.war /usr/local/tomcat8/webapps
