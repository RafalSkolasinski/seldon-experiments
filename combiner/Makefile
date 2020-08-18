KIND_NAME ?= seldon

LOCALHOST_PORT ?= 5000
AMBASSADOR_PORT ?= 8003


image:
	docker build . -t combiner-test:latest

kind-load-image: image
	kind load docker-image combiner-test:latest --name ${KIND_NAME}


deploy:
	kubectl apply -f deploy.yaml

remove:
	kubectl delete -f deploy.yaml


request:
	curl -X POST -H 'Content-Type: application/json' \
		-d '{"data": {"names": ["input"], "ndarray": ["data"]}}' \
		http://localhost:8003/seldon/seldon/combiner-experiments/api/v1.0/predictions | jq .
