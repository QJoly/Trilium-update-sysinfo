#!/usr/bin/env python3

import sys, logging
from trilium_py.client import ETAPI

class triliuminstance:
    def __init__(self, url, token):
       logging.info("Instance initialization")
       assert url is not "", "Can't be empty"
       assert url is not None, "Can't be None"
       assert token is not "", "Can't be empty"
       assert token is not None, "Can't be None"
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
        " Not used rn but maybe in future "
        self.mapNotes = []
        try:
            res = self.ea.search_note(search=research,)
        except KeyError:
            logging.error("Can't search (Empty or invalid string)")
            import sys
            sys.exit(1)
        for x in res['results']:
            try:
                logging.debug("---------------------------------------------------")
                logging.info(f"id: {x['noteId']} title: {x['title']} parentId: {x['parentNoteIds']} parentTitle: {self.ea.get_note(x['parentNoteIds'][0])['title']}")
                self.mapNotes.append(x['noteId'])
                logging.debug("---------------------------------------------------")
            except :
                logging.error("Can't print result : Encoding (?)")
        logging.info(f"There is {len(self.mapNotes)} entries for the keyword '{research}'")
        # not finished, just a draft

    def read_note(self, noteId):
        logging.info(self.ea.get_note_content(noteId))

    def update_note(self, config):
        noteId = config.get_noteId()
        ifUpdatetitle = config.get_updatetitle()
        logging.info(f"Will update the following note : {noteId}")
        logging.debug(f"Can update title ? {ifUpdatetitle}")

        from pathlib import Path
        try:
            notej2=Path('note.tmpl').read_text()
        except FileNotFoundError:
            logging.error("The template file does not exist.")
            sys.exit(1)
        except:
            logging.error("Can't open template file")
            sys.exit(1)

        from jinja2 import Template
        import datetime
        import metrics
        format_data = "%d/%m/%y %H:%M:%S.%f"
        data = {"hostname" : config.get_nodeName().upper(),
                "datetime" : datetime.datetime.now().strftime("%d-%m-%Y-%H.%M.%S"),
                "ramusage" : metrics.get_ramusage(),
                "cpuusage" : metrics.get_cpupercent(),
                "kernelversion" : metrics.get_kernelversion(),
                }

        tm = Template(notej2)
        noteValue = tm.render(data)
        logging.debug(f"Note after update :\n--------------------- {noteValue}\n---------------------")

        try:
           self.ea.update_note_content(noteId, noteValue)
        except:
           logging.warning("Can't update note.. retrying after 2min")
           import time
           time.sleep(120)
           try:
               self.ea.update_note_content(noteId, noteValue)
           except:
               logging.error("Can't update note.. dying..")
               sys.exit(1)

    def get_instance(self):
        return self
