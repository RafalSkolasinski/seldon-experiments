all:

.ONESHELL:

.PHONY: force-build
force-build:


provision:
	kubectl create namespace seldon
	kubectl config set-context $(kubectl config current-context) --namespace=seldon

	kubectl create namespace seldon-system
	helm install seldon-core seldon-core-operator \
		--repo https://storage.googleapis.com/seldon-charts \
		--set ambassador.enabled=true \
		--set usageMetrics.enabled=true \
		--namespace seldon-system

	helm repo add stable https://kubernetes-charts.storage.googleapis.com/
	helm repo update
	helm install ambassador stable/ambassador --set crds.keep=false --namespace seldon

	kubectl rollout status deployment.apps/ambassador
