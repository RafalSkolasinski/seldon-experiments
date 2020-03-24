KIND_NAME ?= seldon

AMBASSADOR_PORT ?= 8003

images:
	s2i build -E environment_rest . seldonio/seldon-core-s2i-python3:0.19-SNAPSHOT compat-mock-model:0.19-SNAPSHOT
	s2i build -E environment_rest . seldonio/seldon-core-s2i-python3:0.18 compat-mock-model:0.18
	s2i build -E environment_rest . seldonio/seldon-core-s2i-python3:0.17-SNAPSHOT compat-mock-model:0.17
	s2i build -E environment_rest . seldonio/seldon-core-s2i-python3:0.16 compat-mock-model:0.16
	s2i build -E environment_rest . seldonio/seldon-core-s2i-python3:0.15 compat-mock-model:0.15
	s2i build -E environment_rest . seldonio/seldon-core-s2i-python3:0.14 compat-mock-model:0.14
	s2i build -E environment_rest . seldonio/seldon-core-s2i-python3:0.13 compat-mock-model:0.13
	s2i build -E environment_rest . seldonio/seldon-core-s2i-python3:0.12 compat-mock-model:0.12
	s2i build -E environment_rest . seldonio/seldon-core-s2i-python3:0.11 compat-mock-model:0.11
	s2i build -E environment_rest . seldonio/seldon-core-s2i-python3:0.10 compat-mock-model:0.10
# 	s2i build -E environment_rest . seldonio/seldon-core-s2i-python3:0.9 compat-mock-model:0.9
# 	s2i build -E environment_rest . seldonio/seldon-core-s2i-python3:0.8 compat-mock-model:0.8
# 	s2i build -E environment_rest . seldonio/seldon-core-s2i-python3:0.7 compat-mock-model:0.7
# 	s2i build -E environment_rest . seldonio/seldon-core-s2i-python3:0.6 compat-mock-model:0.6
# 	s2i build -E environment_rest . seldonio/seldon-core-s2i-python3:0.5 compat-mock-model:0.5
# 	s2i build -E environment_rest . seldonio/seldon-core-s2i-python3:0.4 compat-mock-model:0.4
# 	s2i build -E environment_rest . seldonio/seldon-core-s2i-python3:0.3 compat-mock-model:0.3
# 	s2i build -E environment_rest . seldonio/seldon-core-s2i-python3:0.2 compat-mock-model:0.2
# 	s2i build -E environment_rest . seldonio/seldon-core-s2i-python3:0.1 compat-mock-model:0.1


kind-load-images: images
	kind load docker-image compat-mock-model:0.19-SNAPSHOT --name ${KIND_NAME}
	kind load docker-image compat-mock-model:0.18 --name ${KIND_NAME}
	kind load docker-image compat-mock-model:0.17 --name ${KIND_NAME}
	kind load docker-image compat-mock-model:0.16 --name ${KIND_NAME}
	kind load docker-image compat-mock-model:0.15 --name ${KIND_NAME}
	kind load docker-image compat-mock-model:0.14 --name ${KIND_NAME}
	kind load docker-image compat-mock-model:0.13 --name ${KIND_NAME}
	kind load docker-image compat-mock-model:0.12 --name ${KIND_NAME}
	kind load docker-image compat-mock-model:0.11 --name ${KIND_NAME}
	kind load docker-image compat-mock-model:0.10 --name ${KIND_NAME}
# 	kind load docker-image compat-mock-model:0.9 --name ${KIND_NAME}
# 	kind load docker-image compat-mock-model:0.8 --name ${KIND_NAME}
# 	kind load docker-image compat-mock-model:0.7 --name ${KIND_NAME}
# 	kind load docker-image compat-mock-model:0.6 --name ${KIND_NAME}
# 	kind load docker-image compat-mock-model:0.5 --name ${KIND_NAME}
# 	kind load docker-image compat-mock-model:0.4 --name ${KIND_NAME}
# 	kind load docker-image compat-mock-model:0.3 --name ${KIND_NAME}
# 	kind load docker-image compat-mock-model:0.2 --name ${KIND_NAME}
# 	kind load docker-image compat-mock-model:0.1 --name ${KIND_NAME}

deploy:
	kubectl apply -f deploy.yaml

remove:
	kubectl delete -f deploy.yaml





request:
	curl -s -X POST -H 'Content-Type: application/json' \
		-d '{"meta": {"foo":"bar", "tags": {"a": -1}}, "data": {"names": ["input"], "ndarray": ["data"]}}' \
		http://localhost:${AMBASSADOR_PORT}/seldon/seldon/seldon-mock-model-019-snapshot-executor/api/v1.0/predictions \
		| jq .
	curl -s -X POST -H 'Content-Type: application/json' \
		-d '{"meta": {"foo":"bar", "tags": {"a": -1}}, "data": {"names": ["input"], "ndarray": ["data"]}}' \
		http://localhost:${AMBASSADOR_PORT}/seldon/seldon/seldon-mock-model-019-snapshot-engine/api/v1.0/predictions \
		| jq .
	curl -s -X POST -H 'Content-Type: application/json' \
		-d '{"meta": {"foo":"bar", "tags": {"a": -1}}, "data": {"names": ["input"], "ndarray": ["data"]}}' \
		http://localhost:${AMBASSADOR_PORT}/seldon/seldon/seldon-mock-model-018-executor/api/v1.0/predictions \
		| jq .
	curl -s -X POST -H 'Content-Type: application/json' \
		-d '{"meta": {"foo":"bar", "tags": {"a": -1}}, "data": {"names": ["input"], "ndarray": ["data"]}}' \
		http://localhost:${AMBASSADOR_PORT}/seldon/seldon/seldon-mock-model-018-engine/api/v1.0/predictions \
		| jq .
	curl -s -X POST -H 'Content-Type: application/json' \
		-d '{"meta": {"foo":"bar", "tags": {"a": -1}}, "data": {"names": ["input"], "ndarray": ["data"]}}' \
		http://localhost:${AMBASSADOR_PORT}/seldon/seldon/seldon-mock-model-017-executor/api/v1.0/predictions \
		| jq .
	curl -s -X POST -H 'Content-Type: application/json' \
		-d '{"meta": {"foo":"bar", "tags": {"a": -1}}, "data": {"names": ["input"], "ndarray": ["data"]}}' \
		http://localhost:${AMBASSADOR_PORT}/seldon/seldon/seldon-mock-model-017-engine/api/v1.0/predictions \
		| jq .
	curl -s -X POST -H 'Content-Type: application/json' \
		-d '{"meta": {"foo":"bar", "tags": {"a": -1}}, "data": {"names": ["input"], "ndarray": ["data"]}}' \
		http://localhost:${AMBASSADOR_PORT}/seldon/seldon/seldon-mock-model-016-executor/api/v1.0/predictions \
		| jq .
	curl -s -X POST -H 'Content-Type: application/json' \
		-d '{"meta": {"foo":"bar", "tags": {"a": -1}}, "data": {"names": ["input"], "ndarray": ["data"]}}' \
		http://localhost:${AMBASSADOR_PORT}/seldon/seldon/seldon-mock-model-016-engine/api/v1.0/predictions \
		| jq .
	curl -s -X POST -H 'Content-Type: application/json' \
		-d '{"meta": {"foo":"bar", "tags": {"a": -1}}, "data": {"names": ["input"], "ndarray": ["data"]}}' \
		http://localhost:${AMBASSADOR_PORT}/seldon/seldon/seldon-mock-model-015-executor/api/v1.0/predictions \
		| jq .
	curl -s -X POST -H 'Content-Type: application/json' \
		-d '{"meta": {"foo":"bar", "tags": {"a": -1}}, "data": {"names": ["input"], "ndarray": ["data"]}}' \
		http://localhost:${AMBASSADOR_PORT}/seldon/seldon/seldon-mock-model-015-engine/api/v1.0/predictions \
		| jq .
	curl -s -X POST -H 'Content-Type: application/json' \
		-d '{"meta": {"foo":"bar", "tags": {"a": -1}}, "data": {"names": ["input"], "ndarray": ["data"]}}' \
		http://localhost:${AMBASSADOR_PORT}/seldon/seldon/seldon-mock-model-014-executor/api/v1.0/predictions \
		| jq .
	curl -s -X POST -H 'Content-Type: application/json' \
		-d '{"meta": {"foo":"bar", "tags": {"a": -1}}, "data": {"names": ["input"], "ndarray": ["data"]}}' \
		http://localhost:${AMBASSADOR_PORT}/seldon/seldon/seldon-mock-model-014-engine/api/v1.0/predictions \
		| jq .
	curl -s -X POST -H 'Content-Type: application/json' \
		-d '{"meta": {"foo":"bar", "tags": {"a": -1}}, "data": {"names": ["input"], "ndarray": ["data"]}}' \
		http://localhost:${AMBASSADOR_PORT}/seldon/seldon/seldon-mock-model-013-executor/api/v1.0/predictions \
		| jq .
	curl -s -X POST -H 'Content-Type: application/json' \
		-d '{"meta": {"foo":"bar", "tags": {"a": -1}}, "data": {"names": ["input"], "ndarray": ["data"]}}' \
		http://localhost:${AMBASSADOR_PORT}/seldon/seldon/seldon-mock-model-013-engine/api/v1.0/predictions \
		| jq .
	curl -s -X POST -H 'Content-Type: application/json' \
		-d '{"meta": {"foo":"bar", "tags": {"a": -1}}, "data": {"names": ["input"], "ndarray": ["data"]}}' \
		http://localhost:${AMBASSADOR_PORT}/seldon/seldon/seldon-mock-model-012-executor/api/v1.0/predictions \
		| jq .
	curl -s -X POST -H 'Content-Type: application/json' \
		-d '{"meta": {"foo":"bar", "tags": {"a": -1}}, "data": {"names": ["input"], "ndarray": ["data"]}}' \
		http://localhost:${AMBASSADOR_PORT}/seldon/seldon/seldon-mock-model-012-engine/api/v1.0/predictions \
		| jq .
	curl -s -X POST -H 'Content-Type: application/json' \
		-d '{"meta": {"foo":"bar", "tags": {"a": -1}}, "data": {"names": ["input"], "ndarray": ["data"]}}' \
		http://localhost:${AMBASSADOR_PORT}/seldon/seldon/seldon-mock-model-011-executor/api/v1.0/predictions \
		| jq .
	curl -s -X POST -H 'Content-Type: application/json' \
		-d '{"meta": {"foo":"bar", "tags": {"a": -1}}, "data": {"names": ["input"], "ndarray": ["data"]}}' \
		http://localhost:${AMBASSADOR_PORT}/seldon/seldon/seldon-mock-model-011-engine/api/v1.0/predictions \
		| jq .
	curl -s -X POST -H 'Content-Type: application/json' \
		-d '{"meta": {"foo":"bar", "tags": {"a": -1}}, "data": {"names": ["input"], "ndarray": ["data"]}}' \
		http://localhost:${AMBASSADOR_PORT}/seldon/seldon/seldon-mock-model-010-executor/api/v1.0/predictions \
		| jq .
	curl -s -X POST -H 'Content-Type: application/json' \
		-d '{"meta": {"foo":"bar", "tags": {"a": -1}}, "data": {"names": ["input"], "ndarray": ["data"]}}' \
		http://localhost:${AMBASSADOR_PORT}/seldon/seldon/seldon-mock-model-010-engine/api/v1.0/predictions \
		| jq .
