import configparser
import os

class ConfigReader:
    def __init__(self):
        config = configparser.ConfigParser()
        dirname = os.path.dirname(__file__)
        config.read(os.path.join(dirname, "config.ini"))
        #файлы
        self._folder_path = config["Files"]["FOLDER_PATH"]
        self._price = config["Files"]["PRICE_PATH"]
        #продажи        
        self._reciepts = int(config["Sales_data"]["RECIEPTS"])
        self._shops= config["Sales_data"]["SHOPS"]
        #БД
        self._base = config["DATABASE"]["BASE"]
        self._host = config["DATABASE"]["HOST"]
        self._user = config["DATABASE"]["USER"]
        self._password = config["DATABASE"]["PASSWORD"]
    
    @property
    def folder_path(self):
        return self._folder_path
    
    @property
    def price(self):
        return self._price
    
    @property
    def reciepts(self):
        return self._reciepts
       
    @property
    def base(self):
        return self._base
    
    @property
    def host(self):
        return self._host
    
    @property
    def user(self):
        return self._user
    
    @property
    def password(self):
        return self._password

    def shops(self):
        dct_SHOPS = dict((int(key.strip()), int(val.strip()))
                        for key, val in (el.split(':') 
                                        for el in self._shops.strip('{,}').split(',')))
        # поскольку в БД установлено ограниение первичного ключа для id магазина, радикальное решение чтоб значения ключей словаря шли по порядку
        dont_mess_with_me = {(i+1):el for i, el in enumerate(dct_SHOPS.values())}
        return dont_mess_with_me 