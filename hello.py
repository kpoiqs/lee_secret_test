from mycons import Constants
from configparser import ConfigParser

config = ConfigParser()
config.read('conf.ini')
print(config['1st_section']['1st_key']) # value_1
print("hello")
print(Constants.hello)