import configparser
import os

class ConfigReader:
    def __init__(self):
        self._config = configparser.ConfigParser()
        self._dirname = os.path.dirname(__file__)
        self._config.read(os.path.join(self._dirname, 'self._config.ini'))
        #файлы
        self._folder_path = self._config["Files"]["FOLDER_PATH"]
        self._price = self._config["Files"]["PRICE_PATH"]
        #продажи        
        self._reciepts = int(self._config["Sales_data"]["RECIEPTS"])
        self._shops= self._config["Sales_data"]["SHOPS"]
        #БД
        self._base = self._config["DATABASE"]["BASE"]
        self._host = self._config["DATABASE"]["HOST"]
        self._user = self._config["DATABASE"]["USER"]
        self._password = self._config["DATABASE"]["PASSWORD"]
    
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