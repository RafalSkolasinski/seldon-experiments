all:

.ONESHELL:

.PHONY: force-build
force-build:


deploy-sklearn:
	kubectl apply -f sklearnserver-iris.yaml


cleanup:
	kubectl delete -f sklearnserver-iris.yaml
