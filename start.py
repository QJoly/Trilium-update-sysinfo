#!/usr/bin/env python3
import sys, logging
from yaml_parser import config
from trilium import triliuminstance

logging.basicConfig(filename='debug.log', encoding='utf-8', level=logging.DEBUG)
logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))

def main():
    url, token = config().get_auth()
    instance = triliuminstance(url, token).get_instance()
    instance.read_note("VL4p6pb83Yya")
    instance.update_note(config())
#    instance.search_note("Python")

if __name__ == "__main__":
    main()
