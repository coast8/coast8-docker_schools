


# Debug
edite file $YouDomain/bin/startWebLogic.sh
https://docs.oracle.com/cd/E23717_01/doc.71/e23701/dev_debug_test.htm

startWebLogic.sh
	echo "Launching Java with debug port: 10171"
	 
	JAVA_OPTIONS="-Xdebug -Djava.compiler=NONE -Xnoagent -Xrunjdwp:transport=dt_socket,server=y,address=10171,suspend=n $JAVA_OPTIONS"