all:

.ONESHELL:

build_images:
	s2i build step-1 seldonio/seldon-core-s2i-python37:0.14 seldon-experiments:step-1
	s2i build step-2 seldonio/seldon-core-s2i-python37:0.14 seldon-experiments:step-2
	s2i build step-3 seldonio/seldon-core-s2i-python37:0.14 seldon-experiments:step-3

build_images_minikube:
	eval $$(minikube docker-env)
	make build_images

load_kind:
	kind load docker-image seldon-experiments:step-1 --name experiments
	kind load docker-image seldon-experiments:step-2 --name experiments
	kind load docker-image seldon-experiments:step-3 --name experiments

deploy:
	kubectl apply -f deploy.yaml

remove:
	kubectl delete -f deploy.yaml

redeploy:
	make remove
	make deploy

reload:
	kubectl delete pod -l seldon-deployment-id=three-steps-step-experiments

send_request:
	curl -X POST -H 'Content-Type: application/json' \
		-d "{'data': {'names': ['get'], 'ndarray': ['data']}}" \
		http://localhost:8003/seldon/seldon/step-experiments/api/v0.1/predictions
