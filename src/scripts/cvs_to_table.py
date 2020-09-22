from sqlalchemy import create_engine
import pandas as pd
from dotenv import load_dotenv
import fnmatch, re
import os


load_dotenv()


DATABASE_NAME=os.getenv("DATABASE_NAME")
DATABASE_LOGIN=os.getenv("DATABASE_LOGIN")
DATABASE_PASSWORD=os.getenv("DATABASE_PASSWORD")
DATABASE_HOST=os.getenv("DATABASE_HOST")
DATABASE_PORT=os.getenv("DATABASE_PORT")
PATH_TO_DATA=os.getenv("PATH_TO_DATA")
URL=os.getenv("URL") #ValueErrors when trying to use environmental variables in create_engine

keyword = 'National'

data_directory = os.listdir(PATH_TO_DATA)
for i in range(len(data_directory)):
    filename = sorted(data_directory)[i]
    if keyword in sorted(data_directory)[i]:
       print(sorted(data_directory)[i])
    data_file = pd.read_csv(PATH_TO_DATA+filename, sep=',')
    engine = create_engine(URL)
    data_file.to_sql(filename,engine,if_exists="replace",index=True)

   

 
