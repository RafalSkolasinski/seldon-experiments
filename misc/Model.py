import logging
import numpy as np
import os

name = os.environ.get("NAME", "unkown")

class Model():

    def predict(self, X, feature_names=[]):
        logging.warning(X)
        logging.warning(feature_names)
        return np.append(X, [name])

    def aggregate(self, X, feature_names=[]):
        logging.warning(X)
        logging.warning(feature_names)
        return np.append(np.concatenate(X), [name])
