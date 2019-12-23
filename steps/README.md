# Test multiple step pipeline

Inspired by Alejandro's [seldon-experiments](https://github.com/axsaucedo/seldon_experiments/tree/master/test_metadata_tags) example.



# Minikube

To run execute:

    make build_images_minikube
    make deploy
    make send_request

To reload:

    make build_images_minikube
    make reload


# Kind

To run execute:

    make build_images
    make load_kind

    make deploy
    make send_request

Every time there is a change you can just run

    make build_images
    make load_kind
    make reload
