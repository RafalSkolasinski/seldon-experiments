import logging
import platform
import os

import numpy as np
import time

import ray


def reshape(x):
    if len(x.shape) < 2:
        return x.reshape(1, -1)
    else:
        return x


def get_info():
    return {
        "hostname": platform.node(),
        "pid": os.getpid(),
    }


@ray.remote
def remote_predict(x):
    logging.info(f"OS pid is {os.getpid()}")
    return {"input": x.tolist(), "info": get_info()}


class Model:
    def __init__(self):
        ray.init(num_cpus=4)

    def predict(self, features, names=[], meta=[]):
        logging.info(f"My id is {id(self)}")
        logging.info(f"OS pid is {os.getpid()}")
        logging.info(f"model features: {features}")

        data = reshape(features)

        t1 = time.time()
        object_ids = [remote_predict.remote(x) for x in data]
        results = [ray.get(object_id) for object_id in object_ids]
        t2 = time.time()

        return {"info": get_info(), "time-taken": t2 - t1, "results": results}
