# Test multiple step pipeline

Inspired by Alejandro's [seldon-experiments](https://github.com/axsaucedo/seldon_experiments/tree/master/test_metadata_tags) example.



# Minikube

To run execute:

    make minikube_images
    make deploy
    make send_request

To reload:

    make minikube_images
    make restart


# Kind

To run execute:

    make kind_images
    make deploy
    make send_request

Every time there is a change you can just run

    make kind_images
    make reload
