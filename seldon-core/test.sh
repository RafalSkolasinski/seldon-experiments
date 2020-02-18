#!/usr/bin/env bash

helm install seldon-core seldon-core-operator \
--repo https://storage.googleapis.com/seldon-charts \
--set ambassador.enabled=true \
--set executor.enabled=true \
--namespace seldon-system
