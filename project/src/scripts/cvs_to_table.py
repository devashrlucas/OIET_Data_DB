from sqlalchemy import create_engine
import pandas as pd
from dotenv import load_dotenv
import psycopg2
import os


load_dotenv()


DATABASE_NAME=os.getenv("DATABASE_NAME")
DATABASE_LOGIN=os.getenv("DATABASE_LOGIN")
DATABASE_PASSWORD=os.getenv("DATABASE_PASSWORD")
DATABASE_HOST=os.getenv("DATABASE_HOST")
DATABASE_PORT=os.getenv("DATABASE_PORT")
PATH_TO_DATA=os.getenv("PATH_TO_DATA")
URL=os.getenv("URL") #ValueErrors when trying to use environmental variables in create_engine

city_keyword = 'City'
county_keyword = 'County'
state_keyword = 'State'
national_keyword = 'National'

data_directory = os.listdir(PATH_TO_DATA)

for i in range(len(data_directory)):
    filename = sorted(data_directory)[i]
    data_file = pd.read_csv(PATH_TO_DATA+filename, sep=',')
    if national_keyword in sorted(data_directory)[i]:
       data_file = pd.read_csv(PATH_TO_DATA+filename, sep=',')
       if 'countrycode' not in data_file:
        data_file.insert(0, 'countrycode', '1000')
    engine = create_engine(URL)
    data_file.to_sql(filename,engine,if_exists="replace",index=True)

   
'''
if data_file == f'ACS Demographic And Housing Estimates - National - 2019.csv':
    column = "countrycode"
    parent = 'ACS Demographic And Housing Estimates - National - 2019.csv'
    query = f'ALTER TABLE "{sorted(data_directory)[i]}" ADD CONSTRAINT country FOREIGN KEY ({column}) REFERENCES parent ({column}) MATCH FULL'
    cursor.execute(query)
    connection.commit()
    connection.close()
'''
