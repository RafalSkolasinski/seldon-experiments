import logging


class ModelA():

    def predict(self, X, feature_names=[]):
        logging.warning(X)
        logging.warning(feature_names)
        return [0]

    def tags(self):
        return {"uri": "model-a"}
