import logging
import json
import numpy as np


class Combiner(object):
    def aggregate(self, X, features_names=[]):
        logging.warning(X)
        return [x.tolist() for x in X]


    def tags(self):
        return {"combiner": "tag"}
