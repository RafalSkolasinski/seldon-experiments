import logging
import json
import os


class Model02:
    def predict(self, features, names=[], meta=[]):
        logging.info(f"My id is {id(self)}")
        logging.info(f"OS pid is {os.getpid()}")
        logging.info(f"model features: {features}")
        logging.info(f"model names: {names}")
        logging.info(f"model meta: {meta}")
        return features.tolist()

    def tags(self):
        return {"a": 1, "b": 2}

    def metrics(self):
        return [
            {"type": "COUNTER", "key": "mycounter", "value": 1, "tags": {"foo": "bar"}},
            {"type": "GAUGE", "key": "mygauge", "value": 100},
            {"type": "TIMER", "key": "mytimer", "value": 20.2},
        ]

    def metadata(self):
        meta = json.loads(os.environ.get("MODEL_METADATA", "{}"))
        meta["platform"] = "my-awesome-platform"
        return meta