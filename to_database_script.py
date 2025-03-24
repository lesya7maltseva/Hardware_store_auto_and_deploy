import os
import re
from datetime import date
from class_DB_connection import DatabaseConnection
from class_config_reader import ConfigReader

today_date = date.today()
config = ConfigReader()

if 0 <= today_date.weekday() <= 6:
    db_connection = DatabaseConnection(config.base, config.host, config.user, config.password)

    query = """select count(id) from shops"""
    shops_in_DB = db_connection.get_info(query)[0][0]
    shops = config.shops()
    #на случай если магазинов завели больше чем их есть в БД
    if (len(shops)) > shops_in_DB:
        i = shops_in_DB
        while i < len(shops):
            shop_name = input("Введите название магазина: ")
            shop_city = input("Введите город, где находится магазин: ")
            shop_street = input("Введите улицу, где находится магазин: ")
            db_connection.update_shops(shop_name,shop_city,shop_street)
            i += 1

    lst_files = os.listdir(config.folder_path)
    regexp = r'\d+_\d+\s\d{4}-\d{2}-\d{2}.csv'

    for file in lst_files:
        if re.match(regexp, file):
            db_connection.load(f'{config.folder_path}/{file}')

