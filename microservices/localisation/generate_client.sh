echo 'Installation: https://openapi-generator.tech/docs/installation'
PACKAGE_NAME=localisation
sudo docker buildx build --progress=plain -t $PACKAGE_NAME -f build/Dockerfile . && \
 (sudo docker run --name $PACKAGE_NAME --gpus all --net=host $PACKAGE_NAME --host=0.0.0.0 --port=5731 &) && \
 sleep 5 && \
 npx @openapitools/openapi-generator-cli generate -i http://127.0.0.1:5786/openapi.json -g python -o ./client --additional-properties=packageName={$PACKAGE_NAME}_microservice
echo 'Use pip install $PACKAGE_NAME/client'
