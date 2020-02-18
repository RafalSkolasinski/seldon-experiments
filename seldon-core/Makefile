DIR:=$(dir $(realpath $(firstword $(MAKEFILE_LIST))))
TEMPRESOURCES_DIR:=$(DIR)/tmp_resources

SELDON_CORE_OPERATOR_VERSION ?= master
SELDON_COPRE_OPERATOR_NAMESPACE ?= seldon-system

ENGINE_IMAGE ?= seldonio/engine
ENGINE_VERSION ?= 1.0.3-SNAPSHOT

EXECUTOR_IMAGE ?= seldonio/seldon-core-executor
EXECUTOR_VERSION ?= 1.0.3-SNAPSHOT


EXECUTOR_ENABLED ?= false
AMBASSADOR_ENABLED ?= true


seldon-core-operator: clone-seldon-core
	helm delete seldon-core --namespace ${SELDON_COPRE_OPERATOR_NAMESPACE} || echo "seldon-core not installed"
	kubectl create namespace ${SELDON_COPRE_OPERATOR_NAMESPACE} || echo "namespace ${SELDON_COPRE_OPERATOR_NAMESPACE} exists"
	helm install seldon-core ${TEMPRESOURCES_DIR}/seldon-core/helm-charts/seldon-core-operator \
		--set ambassador.enabled=${AMBASSADOR_ENABLED} \
		--set executor.enabled=${EXECUTOR_ENABLED} \
		--set engine.image.repository=${ENGINE_IMAGE} \
		--set engine.image.tag=${ENGINE_VERSION} \
		--set executor.image.repository=${EXECUTOR_IMAGE} \
		--set executor.image.tag=${EXECUTOR_VERSION} \
		--namespace ${SELDON_COPRE_OPERATOR_NAMESPACE}


clone-seldon-core: tempresources-dir
	git clone https://github.com/SeldonIO/seldon-core.git tmp_resources/seldon-core -b ${SELDON_CORE_OPERATOR_VERSION}

tempresources-dir: remove-tempresources-dir
	mkdir -p ${TEMPRESOURCES_DIR}

remove-tempresources-dir:
	rm -rf ${TEMPRESOURCES_DIR}
