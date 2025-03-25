import psycopg2 
import pandas as pd
from io import StringIO

class DatabaseConnection:
    def __init__(self, basename, host, user, password):
        self.basename = basename
        self.host = host
        self.user = user
        self.password = password

        self.connection = psycopg2.connect(
            host = host,
            database = basename,         
            user = user,
            password = password,
        )       
        
    #метод загрузки данных в БД
    def load (self, filepath):
        cursor = self.connection.cursor()
        df_loaded = pd.read_csv(filepath, sep=',')
        # создаем буфер обмена и копируем туда данные из считанного датафрейма
        clipboard = StringIO()
        df_loaded.to_csv(clipboard, index= None, header= None, encoding= 'utf-8') 

        clipboard.seek(0)

        with cursor as sc:
            sc.copy_expert(
                sql = """
                COPY sales (
                    doc_id,
                    item,
                    category,	
                    amount,	
                    discount, 
                    price,	
                    date,
                    shop_id,
                    till_id) FROM STDIN WITH CSV""",
                    file = clipboard
            )
        self.connection.commit()

    #добавление магазина
    def update_shops(self, *args):
        cursor = self.connection.cursor()
        query = f"insert into shops (shop_name, shop_city, shop_street) values (%s, %s, %s)"
        try:
            cursor.execute(query, args)
        except Exception as err:
            print("Не удалось обновить таблицу shops", err)
        finally: self.connection.commit()

    # получение информации из БД
    def get_info (self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()

        


