import pandas as pd
import random
import string
from datetime import date
from class_config_reader import ConfigReader

today_date = date.today()

config = ConfigReader()

df_price = pd.read_csv(config.price)
df_price['price']  = df_price.apply(lambda x: float(x['price']), axis= 1)

def create_reciept(sales):
  for i in range(sales):
    doc_id = "".join(random.choices(string.ascii_lowercase + string.digits, k = 20))
    n = random.randint(1,10)
    dict_df = {'doc_id': [doc_id for el in range(n)],
          'amount': [random.randint(1,7) for el in range(n)],
          'discount':[random.randint(0,16) for el in range(n)],
          'id': [random.randint(1,2473) for el in range(n)]
          }
    yield dict_df

class Sales:
  def __init__(self, length):
    self._shop = list(create_reciept(length))
    self._shops_price = pd.DataFrame()

  def generate_sales(self):
    for i, el in enumerate(self._shop):
      if i == 0:
        start = pd.DataFrame(el)
      else:
        new_df = pd.concat([start,pd.DataFrame(el)], ignore_index = True)
        start = new_df
    new_df['date'] = today_date
    new_df = new_df.merge(df_price, on ='id')
    new_df = new_df.reindex(columns = ['doc_id', 'name', 'category', 'amount', 'discount', 'price', 'id', 'date'])
    new_df = new_df.drop(['id'], axis=1)
    self._shops_price =  new_df
  
  def new_column (self, **kwargs):
    for key, val in kwargs.items():
      self._shops_price[key] = val

  def get_shops_price(self):
    return self._shops_price
