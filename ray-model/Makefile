KIND_NAME ?= seldon


LOCALHOST_PORT ?= 5000
AMBASSADOR_PORT ?= 8003



image:
	docker build . -t ray-model:latest

push-image: image
	docker tag ray-model:latest rafalskolasinski/ray-model:latest
	docker push rafalskolasinski/ray-model:latest

deploy:
	kubectl apply -f deploy.yaml

remove:
	kubectl delete -f deploy.yaml

kind-load-image: image
	kind load docker-image ray-model:latest --name ${KIND_NAME}










local-run:
	PREDICTIVE_UNIT_SERVICE_PORT=${LOCALHOST_PORT} seldon-core-microservice Model REST --service-type MODEL --debug --log-level DEBUG



local-request-single:
	curl -s -H 'Content-Type: application/json' \
		-d '{"data": {"ndarray": [1, 2, 3]}}' \
		http://localhost:${LOCALHOST_PORT}/api/v1.0/predictions | jq .


local-request-many:
	curl -H 'Content-Type: application/json' \
		-d '{"data": {"ndarray": [[1, 2, 3], [4, 5, 6], [7, 8, 9]]}}' \
		http://localhost:${LOCALHOST_PORT}/api/v1.0/predictions | jq .
