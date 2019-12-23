# Seldon Experiments

This repository contains various experiments and is considered to be my playground.
You're free to take the inspiration from codes you find here but for official examples
please refer to Seldon [documentation](https://docs.seldon.io/en/latest/).

All comments are welcomed! ;-)


# Requirements

This section need to be expended. Rough list of requirements is as follows:

* helm v3
* kind
* kubectl
* s2i


# Playground environment

If not specified otherwise, I use [Kubernetes](https://kubernetes.io/) cluster v1.15.6.

An easy way to get it up and running is [Kind](https://kind.sigs.k8s.io/):

    kind create cluster --image kindest/node:v1.15.6 --name experiments

This will automatically set your `kubectl` context to work with kind cluster.
You can now provision cluster with help of provided [Makefile](./Makefile)

    make provision

or by following official documentation [here](https://docs.seldon.io/projects/seldon-core/en/latest/workflow/install.html).

To gain access to cluster execute in separate terminal

    kubectl port-forward svc/ambassador 8003:80
