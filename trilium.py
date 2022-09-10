#!/usr/bin/env python3

import sys, logging
from trilium_py.client import ETAPI

class triliuminstance:
    def __init__(self, url, token):
       logging.info("Instance initialization")
       assert url != "", "Can't be empty"
       assert url != None, "Can't be None"
       assert token != "", "Can't be empty"
       assert token != None, "Can't be None"
       self.url = url
       self.token = token
       logging.info("Will use {} as trilium instance".format(url))
       logging.info("Trying to login...")
       self.connect()

    def connect(self):
        try:
            self.ea = ETAPI(self.url, self.token)
        except:
            logging.error("Can't login to trilium instance")
            sys.exit(1)
