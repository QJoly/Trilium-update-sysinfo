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

    def get_auth(self):
       return self.url, self.token

if __name__ == "__main__":
    logging.basicConfig(filename='debug.log', encoding='utf-8', level=logging.DEBUG)
    logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))
    obj = config()
    print(obj.get_auth())
