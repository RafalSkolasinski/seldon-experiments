KIND_NAME ?= seldon
SELDON_CORE_DIR ?= ${HOME}/work/seldon-core

LOCALHOST_PORT ?= 5000
AMBASSADOR_PORT ?= 8003


image:
	docker build . -t misc-model:latest

kind-load-image: image
	kind load docker-image misc-model:latest --name ${KIND_NAME}


deploy:
	kubectl apply -f deploy.yaml

remove:
	kubectl delete -f deploy.yaml



request-single:
	curl -s -H 'Content-Type: application/json' \
		-d '{"data": {"names": ["input"], "ndarray": ["input-data"]}}' \
		http://localhost:${AMBASSADOR_PORT}/seldon/seldon/misc-single/api/v1.0/predictions  | jq .

request-chain:
	curl -s -H 'Content-Type: application/json' \
		-d '{"data": {"names": ["input"], "ndarray": ["input-data"]}}' \
		http://localhost:${AMBASSADOR_PORT}/seldon/seldon/misc-chain/api/v1.0/predictions  | jq .

request-forked-chain:
	curl -s -H 'Content-Type: application/json' \
		-d '{"data": {"names": ["input"], "ndarray": ["input-data"]}}' \
		http://localhost:${AMBASSADOR_PORT}/seldon/seldon/misc-forked-chain/api/v1.0/predictions  | jq .
