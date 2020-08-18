import logging


class ModelB():

    def predict(self, X, feature_names=[]):
        logging.warning(X)
        logging.warning(feature_names)
        return ["model-B"]
