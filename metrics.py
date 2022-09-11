#!/usr/bin/env python3
import psutil,logging,sys,platform,time

def get_cpupercent():
   try:
      cpupercent = str(psutil.cpu_percent())
      logging.debug(f"The usage of CPU is {cpupercent}%")
      if cpupercent == "0.0":
         logging.debug("Value is 0.0 retry in 1s..")
         count = 1
         while cpupercent == "0.0" and count < 10:
            logging.debug(f"reload cpu_percent, got {cpupercent}")
            time.sleep(1)
            cpupercent = str(psutil.cpu_percent())
            count += 1
   except:
      cpupercent = "N/A"
   return cpupercent

def get_ramusage():
   try:
      ramusage = psutil.virtual_memory().percent
   except:
      ramusage = "N/A"
   logging.debug(f"The usage of RAM is {ramusage}%")
   return ramusage

def get_kernelversion():
   try:
      kernelversion = platform.version()
   except:
      kernelversion = "N/A"
   return kernelversion

def main():
   get_cpupercent()
   get_ramusage()

if __name__ == "__main__":
    logging.basicConfig(filename='debug.log', encoding='utf-8', level=logging.DEBUG)
    logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))
    main()
