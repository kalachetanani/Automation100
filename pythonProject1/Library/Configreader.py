import configparser
from configparser import ConfigParser

def readconfigdata(section,key):
    cfg=configparser.ConfigParser()
    cfg.read("C:/Softwares/Python/pythonProject1/configurationfiles/config.cfg")
    return cfg.get(section,key)






