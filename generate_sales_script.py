from datetime import date
import os
import shutil
from class_sales import Sales
from class_config_reader import ConfigReader

today_date = date.today()
config = ConfigReader()
dirname = os.path.dirname(__file__)

if today_date.weekday() < 6:
  #проверяем наличие папки - создаем если её нет или удаляем всё содержимое, если она есть
  try:
    if os.path.exists(config.folder_path):
      shutil.rmtree(config.folder_path)
      os.mkdir(config.folder_path) 
    else: 
      os.mkdir(config.folder_path)  
  except Exception as err:
    print('Ошибка: ', err)


  #генерируем наши датасеты
  for key, val in config.shops().items():
    for i in range(1,val+1):
      #создаем объект прайса и работаем с ним
      df_shop = Sales(config.reciepts)
      df_shop.generate_sales()
      df_shop.new_column(shop_id = key, till_id = i)
      df_shop.get_shops_price().to_csv(os.path.join(dirname, f'{config.folder_path}/{key}_{i} {today_date}.csv'), index= False)


# try:
#     if os.path.exists(os.path.join(dirname, config.folder_path)):
#       shutil.rmtree(os.path.join(dirname, config.folder_path))
#       os.mkdir(os.path.join(dirname, config.folder_path)) 
#     else: 
#       os.mkdir(os.path.join(dirname, config.folder_path))  
#   except Exception as err:
#     print('Ошибка: ', err)