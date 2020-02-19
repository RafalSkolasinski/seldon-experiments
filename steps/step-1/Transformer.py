import logging

class Transformer():

    def __init__(self):
        self._tags = {}

    def predict(self, X, feature_names, meta):
        logging.warning(X)
        logging.warning(feature_names)
        logging.warning(meta)
        self._tags["value_at_one"] = X.tolist()
        self._tags["current"] = "one"
        self._tags["one"] = "yes"
        return ["one"]

    def tags(self):
        return self._tags
