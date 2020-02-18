SELDON_CORE_OPERATOR_VERSION ?= master

DIR:=$(dir $(realpath $(firstword $(MAKEFILE_LIST))))
TEMPRESOURCES_DIR:=$(DIR)/tmp_resources


seldon-core-operator: clone-seldon-core
	helm delete seldon-core --namespace seldon-system || echo "seldon-core not installed"
	kubectl create namespace seldon-system || echo "namespace seldon-system exists"
	helm install seldon-core ${TEMPRESOURCES_DIR}/seldon-core/helm-charts/seldon-core-operator \
		--set ambassador.enabled=true \
		--set executor.enabled=true \
		--namespace seldon-system


clone-seldon-core: tempresources-dir
	git clone https://github.com/SeldonIO/seldon-core.git tmp_resources/seldon-core -b ${SELDON_CORE_OPERATOR_VERSION}

tempresources-dir: remove-tempresources-dir
	mkdir -p ${TEMPRESOURCES_DIR}

remove-tempresources-dir:
	rm -rf ${TEMPRESOURCES_DIR}
