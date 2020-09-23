import pandas as pd
import os

PATH_TO_DATA = os.getenv("PATH_TO_DATA")

data_directory = os.listdir(PATH_TO_DATA)

city_keyword = 'City'
county_keyword = 'County'
state_keyword = 'State'
national_keyword = 'National'

for i in range(len(data_directory)):
    filename = sorted(data_directory)[i]
    '''
    if city_keyword in sorted(data_directory)[i]:
        print(sorted(data_directory)[i])
    elif county_keyword in sorted(data_directory)[i]:
        print(sorted(data_directory)[i])
    elif city_keyword in sorted(data_directory)[i]:
       print(sorted(data_directory)[i])
    elif state_keyword in sorted(data_directory)[i]:
       print(sorted(data_directory)[i])
'''
    elif national_keyword in sorted(data_directory)[i]:
       data_file = pd.read_csv(PATH_TO_DATA+filename, sep=',')
       if 'countrycode' not in data_file:
        data_file.insert(0, 'countrycode', '1000')
        print(data_file.head())
