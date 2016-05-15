#! /usr/bin/python
# -*- coding: utf-8 -*-

import os
import random
from hashlib import md5


CONFIG_PATH = "./token"

def generate_token():
    config = open(CONFIG_PATH, 'w')
    token = md5(str(hash(random.random()))).hexdigest()
    config.write(token)
    config.close()
    return token

def load_token():
    if os.path.isfile(CONFIG_PATH) and os.path.getsize(CONFIG_PATH) > 0:
        config = open(CONFIG_PATH, 'r')
        token = config.read().strip()
        return token
    else:
        return generate_token()
