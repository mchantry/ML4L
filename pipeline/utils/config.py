# -*- coding: utf-8 -*-
"""Config class"""

import json


class Config:
    """Config class which contains data, train and model hyperparameters"""

    def __init__(self, data, train, prep,model):
        self.data = data
        self.prep = prep
        self.train = train
        self.model = model

    @classmethod 
    def from_json(cls, cfg):
        """Creates config from json"""
        params = json.loads(json.dumps(cfg), object_hook=HelperObject)
        return cls(params.data,params.prep,params.train, params.model)


class HelperObject(object):
    """Helper class to convert json into Python object"""
    def __init__(self, dict_):
        self.__dict__.update(dict_)