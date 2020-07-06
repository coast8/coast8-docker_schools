
* ensina como parsar parametros para o arquivo Dockerfile


# executando o docker file padrão sem passar argumentos.
docker image build -t ex-build-arg .
docker container run ex-build-arg bash -c 'echo $S3_BUCKET'


# alterando o valor $S3_BUCKET, passando o valor como parametro para essa varialvel
docker image build --build-arg S3_BUCKET=myapp -t ex-build-arg 