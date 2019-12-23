all:

.ONESHELL:

images:
	s2i build step-1 seldonio/seldon-core-s2i-python37:0.14 seldon-experiments:step-1
	s2i build step-2 seldonio/seldon-core-s2i-python37:0.14 seldon-experiments:step-2
	s2i build step-3 seldonio/seldon-core-s2i-python37:0.14 seldon-experiments:step-3

deploy:
	kubectl apply -f deploy.yaml

remove:
	kubectl delete -f deploy.yaml

restart:
	kubectl delete pod -l seldon-deployment-id=three-steps-step-experiments


kind_images:
	make images
	kind load docker-image seldon-experiments:step-1 --name experiments
	kind load docker-image seldon-experiments:step-2 --name experiments
	kind load docker-image seldon-experiments:step-3 --name experiments

kind_reload:
	make kind_images
	make restart


minikube_images:
	eval $$(minikube docker-env)
	make images

minikube_reload:
	make minikube_images
	make restart


send_request:
	curl -X POST -H 'Content-Type: application/json' \
		-d "{'data': {'names': ['get'], 'ndarray': ['data']}}" \
		http://localhost:8003/seldon/seldon/step-experiments/api/v0.1/predictions
