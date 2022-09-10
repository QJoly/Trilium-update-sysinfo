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
       logging.info("Success !")

    def connect(self):
        try:
            self.ea = ETAPI(self.url, self.token)
        except:
            logging.error("Can't login to trilium instance")
            sys.exit(1)

    def search_note(self, research):
        res = self.ea.search_note(search=research,)
        for x in res['results']:
            try:
                logging.info("---------------------------------------------------")
                logging.info("id: {} title: {}".format(x['noteId'], x['title']))
                logging.info("parent id : ".format(self.ea.get_note(x['noteId'])['parentNoteIds']))
                logging.info("---------------------------------------------------")
            except :
                logging.error("Can't print result : Encoding (?)")
         # print(x['noteId'], x['title'])



    def get_instance(self):
        return self
