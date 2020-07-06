


apt update
apt install openjdk-8-jdk openjdk-8-jre
java -version


# variaveis de ambiemte

JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
export JAVA_HOME
export PATH=$PATH:$JAVA_HOME
echo $JAVA_HOME

JRE_HOME=/usr/lib/jvm/java-8-openjdk-amd64/jre
export JRE_HOME
export PATH=$PATH:$JRE_HOME
echo $JRE_HOME




FONTE:
https://tecadmin.net/install-oracle-java-8-ubuntu-via-ppa/