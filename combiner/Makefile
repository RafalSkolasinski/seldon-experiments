all:

.ONESHELL:

images:
	s2i build model-1 seldonio/seldon-core-s2i-python37:0.14 seldon-experiments:model-1
	s2i build model-2 seldonio/seldon-core-s2i-python37:0.14 seldon-experiments:model-2
	s2i build combiner seldonio/seldon-core-s2i-python37:0.14 seldon-experiments:combiner

minikube_images:
	eval $$(minikube docker-env)
	make images

deploy:
	kubectl apply -f deploy.yaml

remove:
	kubectl delete -f deploy.yaml

restart:
	kubectl delete pod -l seldon-deployment-id=combiner-experiments-combiner-experiments


send_request:
	curl -X POST -H 'Content-Type: application/json' \
		-d "{'data': {'names': ['get'], 'ndarray': ['data']}}" \
		http://localhost:8003/seldon/seldon/combiner-experiments/api/v0.1/predictions
