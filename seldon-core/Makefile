DIR := $(dir $(realpath $(firstword $(MAKEFILE_LIST))))

KIND_NAME ?= seldon

TEMPRESOURCES_DIR := $(DIR)tmp_resources
SELDON_CORE_TEMPDIR := $(TEMPRESOURCES_DIR)/seldon-core

SELDON_CORE_SOURCE_DIR ?= $(SELDON_CORE_TEMPDIR)

SELDON_CORE_GITHUB ?= https://github.com/SeldonIO/seldon-core.git
SELDON_CORE_VERSION ?= origin/master

SELDON_CORE_OPERATOR_NAMESPACE ?= seldon-system

EXECUTOR_IMAGE ?= seldonio/seldon-core-executor
EXECUTOR_VERSION ?= 1.1.1-rc

OPERATOR_IMAGE ?= seldonio/seldon-core-operator
OPERATOR_VERSION ?= 1.1.1-rc

ENGINE_IMAGE ?= seldonio/engine
ENGINE_VERSION ?= 1.1.1-rc


EXECUTOR_ENABLED ?= true
AMBASSADOR_ENABLED ?= true
ISTIO_ENABLED ?= false

USAGE_METRICS ?= false

install: clone-seldon-core seldon-core
install-custom: clone-seldon-core seldon-core-custom


clone-seldon-core: tempdir
	git -C ${SELDON_CORE_TEMPDIR} fetch origin || git clone ${SELDON_CORE_GITHUB} ${SELDON_CORE_TEMPDIR}
	git -C ${SELDON_CORE_TEMPDIR} checkout ${SELDON_CORE_VERSION}

seldon-core:
	helm delete seldon-core --namespace ${SELDON_CORE_OPERATOR_NAMESPACE} || echo "seldon-core not installed"
	kubectl create namespace ${SELDON_CORE_OPERATOR_NAMESPACE} || echo "namespace ${SELDON_CORE_OPERATOR_NAMESPACE} exists"
	helm install seldon-core ${SELDON_CORE_SOURCE_DIR}/helm-charts/seldon-core-operator \
		--set usageMetrics.enabled=${USAGE_METRICS} \
		--set ambassador.enabled=${AMBASSADOR_ENABLED} \
	    --namespace ${SELDON_CORE_OPERATOR_NAMESPACE}

seldon-core-custom:
	helm delete seldon-core --namespace ${SELDON_CORE_OPERATOR_NAMESPACE} || echo "seldon-core not installed"
	kubectl create namespace ${SELDON_CORE_OPERATOR_NAMESPACE} || echo "namespace ${SELDON_CORE_OPERATOR_NAMESPACE} exists"
	helm install seldon-core ${SELDON_CORE_SOURCE_DIR}/helm-charts/seldon-core-operator \
		--set usageMetrics.enabled=${USAGE_METRICS} \
		--set ambassador.enabled=${AMBASSADOR_ENABLED} \
		--set istio.enabled=${ISTIO_ENABLED} \
		--set image.repository=${OPERATOR_IMAGE} \
		--set image.tag=${OPERATOR_VERSION} \
		--set executor.enabled=${EXECUTOR_ENABLED} \
		--set engine.image.repository=${ENGINE_IMAGE} \
		--set engine.image.tag=${ENGINE_VERSION} \
		--set executor.image.repository=${EXECUTOR_IMAGE} \
		--set executor.image.tag=${EXECUTOR_VERSION} \
		--namespace ${SELDON_CORE_OPERATOR_NAMESPACE}


ambassador:
	kubectl create namespace ambassador || echo "namespace ambassador exists"
	helm install ambassador stable/ambassador \
		--set crds.keep=false \
		--namespace ambassador


seldon-core-analytics:
	helm delete seldon-core-analytics --namespace ${SELDON_CORE_OPERATOR_NAMESPACE} || echo "seldon-core-analytics not installed"
	helm install seldon-core-analytics ${SELDON_CORE_SOURCE_DIR}/helm-charts/seldon-core-analytics \
	   --namespace ${SELDON_CORE_OPERATOR_NAMESPACE}


tempdir:
	mkdir -p ${TEMPRESOURCES_DIR}

clean:
	rm -rf ${TEMPRESOURCES_DIR}


kind-cluster:
	kind create cluster --name ${KIND_NAME}

kind-delete:
	kind delete cluster --name ${KIND_NAME}

port-forward:
	kubectl port-forward -n ambassador svc/ambassador 8003:80
