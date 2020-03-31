KIND_NAME ?= seldon
SELDON_CORE_DIR ?= ${HOME}/work/seldon-core

LOCALHOST_PORT ?= 5000
AMBASSADOR_PORT ?= 8003


image:
	docker build . -t mock-model:latest

deploy:
	kubectl apply -f deploy.yaml

remove:
	kubectl delete -f deploy.yaml

kind-load-image: image
	kind load docker-image mock-model:latest --name ${KIND_NAME}


local-run:
	PREDICTIVE_UNIT_SERVICE_PORT=${LOCALHOST_PORT} seldon-core-microservice Model REST --service-type MODEL --log-level DEBUG

local-run-grpc:
	PREDICTIVE_UNIT_SERVICE_PORT=${LOCALHOST_PORT} seldon-core-microservice Model GRPC --service-type MODEL --log-level DEBUG


docker-run:
	docker rm -f mock-model || echo "Already removed"
	docker run --name "mock-model" --rm -d -p 127.0.0.1:${LOCALHOST_PORT}:5000 mock-model:latest

docker-rm:
	docker rm -f mock-model



request-localhost:
	curl -X POST -H 'Content-Type: application/json' \
		-d '{"meta": {"tags": {"a": -1, "foo": "bar"}}, "data": {"names": ["input"], "ndarray": ["data"]}}' \
		http://localhost:${LOCALHOST_PORT}/api/v0.1/predictions | jq .

request-localhost-grpc:
	cd ${SELDON_CORE_DIR}/executor/proto && grpcurl \
		-d '{"meta": {"tags": {"a": -1, "foo": "bar"}}, "data": {"names": ["input"], "ndarray": ["data"]}}' \
		-plaintext -proto ./prediction.proto  0.0.0.0:5000 seldon.protos.Seldon/Predict

request-k8s:
	curl -X POST -H 'Content-Type: application/json' \
		-d '{"meta": {"tags": {"a": -1, "foo": "bar"}}, "data": {"names": ["input"], "ndarray": ["data"]}}' \
		http://localhost:${AMBASSADOR_PORT}/seldon/seldon/seldon-mock-model/api/v1.0/predictions  | jq .
