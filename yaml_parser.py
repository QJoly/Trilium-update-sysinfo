import yaml, logging, sys
from yaml.loader import SafeLoader

class config:
   "Parser of the yaml config file"
   def __init__(self):
       logging.info("Trying to open config.yml")
       try:
           with open('config.yml') as f:
               data = yaml.load(f, Loader=SafeLoader)
       except:
           logging.error("Unable to open file")
           sys.exit(1)
       logging.debug(data)
       logging.info("Successfuly opened config.yml")
       self.url = data["server"]["url"]
       self.token = data["server"]["token"]
       self.noteId = data["noteId"]
       self.updatetitle = data["update_title"]
       if data["nodeName"] is None or data["nodeName"] == "" :
           logging.info("nodename is not specified")
           import platform
           self.nodeName = platform.node()
       else:
           logging.info("nodeName is available")
           self.nodeName = data["nodeName"]

   def get_auth(self):
       return self.url, self.token

   def get_nodeName(self):
       return self.nodeName

   def get_noteId(self):
       return self.noteId

   def get_updatetitle(self):
       return self.updatetitle
