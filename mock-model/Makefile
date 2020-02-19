KIND_NAME ?= seldon

image:
	docker build . -t mock-model:latest

deploy:
	kubectl apply -f deploy.yaml

kind_image: image
	kind load docker-image mock-model:latest --name ${KIND_NAME}

run:
	docker rm -f mock-model || echo "Already removed"
	docker run --name "mock-model" --rm -d -p 127.0.0.1:5000:5000 mock-model:latest

request_localhost:
	curl -X POST -H 'Content-Type: application/json' \
		-d '{"data": {"names": ["get"], "ndarray": ["data"]}}' \
		http://localhost:5000/api/v0.1/predictions

request_k8s:
	curl -X POST -H 'Content-Type: application/json' \
		-d '{"data": {"names": ["get"], "ndarray": ["data"]}}' \
		http://localhost:8003/seldon/seldon/seldon-mock-model/api/v0.1/predictions
