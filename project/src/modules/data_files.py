from sqlalchemy import create_engine
import pandas as pd
from dotenv import load_dotenv
import os
import re
from project.src.modules.database import db

load_dotenv()


class DataFiles:
    def __init__(self):
        self

    path_to_data = os.getenv("PATH_TO_DATA")
    data_directory = os.listdir(path_to_data)

    def alter_files(self):
        for i in range(len(self.data_directory)):
            filename = sorted(self.data_directory)[i]
            data_file = pd.read_csv(self.path_to_data + filename, sep=",")
            if "National" in sorted(self.data_directory)[i]:
                data_file = pd.read_csv(self.path_to_data + filename, sep=",")
                if "countrycode" not in data_file:
                    data_file["countrycode"] = 1000
                    data_file.to_csv(self.path_to_data + filename, sep=",")

    def export_to_table(self):
        for i in range(len(self.data_directory)):
            filename = sorted(self.data_directory)[i]
            data_file = pd.read_csv(self.path_to_data + filename, sep=",")
            engine = create_engine(db.url)
            if ".csv" in filename:
                filename = re.sub(r".csv$", "", filename)
            data_file.to_sql(filename, engine, if_exists="replace", index=True)


DATA = DataFiles()
DATA.alter_files()
DATA.export_to_table()
print("d_f.py done")
