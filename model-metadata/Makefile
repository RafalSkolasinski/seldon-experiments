KIND_NAME ?= seldon
SELDON_CORE_DIR ?= ${HOME}/work/seldon-core

LOCALHOST_PORT ?= 5000
AMBASSADOR_PORT ?= 8003


image:
	docker build . -t metadata-model:latest

deploy:
	kubectl apply -f deploy.yaml

remove:
	kubectl delete -f deploy.yaml

kind-load-image: image
	kind load docker-image metadata-model:latest --name ${KIND_NAME}


local-run:
	PREDICTIVE_UNIT_SERVICE_PORT=${LOCALHOST_PORT} seldon-core-microservice Model REST --service-type MODEL --log-level DEBUG

# local-run-grpc:
# 	PREDICTIVE_UNIT_SERVICE_PORT=${LOCALHOST_PORT} seldon-core-microservice Model GRPC --service-type MODEL --log-level DEBUG


# docker-run:
# 	docker rm -f metadata-model || echo "Already removed"
# 	docker run --name "metadata-model" --rm -d -p 127.0.0.1:${LOCALHOST_PORT}:5000 metadata-model:latest

# docker-rm:
# 	docker rm -f metadata-model



# local-request:
# 	curl -X POST -H 'Content-Type: application/json' \
# 		-d '{"meta": {"tags": {"a": -1, "foo": "bar"}}, "data": {"names": ["input"], "ndarray": ["data"]}}' \
# 		http://localhost:${LOCALHOST_PORT}/api/v0.1/predictions | jq .

# local-request-grpc:
# 	cd ${SELDON_CORE_DIR}/executor/proto && grpcurl \
# 		-d '{"meta": {"tags": {"a": -1, "foo": "bar"}}, "data": {"names": ["input"], "ndarray": ["data"]}}' \
# 		-plaintext -proto ./prediction.proto  0.0.0.0:5000 seldon.protos.Seldon/Predict

request:
	curl -X POST -H 'Content-Type: application/json' \
		-d '{"data": {"names": ["input"], "ndarray": ["data"]}}' \
		http://localhost:${AMBASSADOR_PORT}/seldon/seldon/metadata-model-01/api/v1.0/predictions  | jq .
	curl -X POST -H 'Content-Type: application/json' \
		-d '{"data": {"names": ["input"], "ndarray": ["data"]}}' \
		http://localhost:${AMBASSADOR_PORT}/seldon/seldon/metadata-model-02-yml/api/v1.0/predictions  | jq .
	curl -X POST -H 'Content-Type: application/json' \
		-d '{"data": {"names": ["input"], "ndarray": ["data"]}}' \
		http://localhost:${AMBASSADOR_PORT}/seldon/seldon/metadata-model-02-env/api/v1.0/predictions  | jq .

request-metadata:
	curl -s http://localhost:${AMBASSADOR_PORT}/seldon/seldon/metadata-model-01/api/v1.0/metadata/my-metadata-model | jq .
	curl -s http://localhost:${AMBASSADOR_PORT}/seldon/seldon/metadata-model-02-yml/api/v1.0/metadata/my-metadata-model | jq .
	curl -s http://localhost:${AMBASSADOR_PORT}/seldon/seldon/metadata-model-02-env/api/v1.0/metadata/my-metadata-model | jq .
	curl -s http://localhost:${AMBASSADOR_PORT}/seldon/seldon/metadata-sklearn/api/v1.0/metadata/classifier| jq .
