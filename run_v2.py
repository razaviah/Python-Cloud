#!/usr/bin python3
"""
This is the main file for the py_cloud project. It can be used at any situation
"""
import requests
import json
import toml
import pandas as pd
from collections import ChainMap
from dotenv import load_dotenv
import os
import subprocess


# main function
if __name__=='__main__':
    app_config = toml.load('config.toml')
    url = app_config['api']['url']

    # read the API
    print('Reading the API...')
    response_API = requests.get(url)

    # getting the response status code and showing it to the user w/ its' definition
    response_defi = {200 : "The request was successful.", \
                 400 : "An error occurred in your request.", \
                 403 : "The request was forbidden - usually because you hit a rate limit.", \
                 404 : "The resource could not be found."}
    print("Response Code:", response_API.status_code)
    print("Response Code meaning:", response_defi[response_API.status_code])
    print('API Reading Done!')

    # the company name
    print('Building the dataframe...')
    company_list = [data['results'][i]['company']['name'] for i in range(len(data['results']))]
    company_name = {'company':company_list}

    # the locations
    location_list = [data['results'][i]['locations'][0]['name'] for i in range(len(data['results']))]
    location_name = {'locations':location_list}
    
    # the job name
    job_list = [data['results'][i]['name'] for i in range(len(data['results']))]
    job_name = {'job':job_list}

    # the job type
    job_type_list = [data['results'][i]['type'] for i in range(len(data['results']))]
    job_type = {'job_type':job_type_list}

    # the publication date
    publication_date_list = [data['results'][i]['publication_date'] for i in range(len(data['results']))]
    publication_date = {'publication_date':publication_date_list}

    # merge the dictionaries with ChainMap and dict "from collections import ChainMap"
    data = dict(ChainMap(company_name, location_name, job_name, job_type, publication_date))
    df=pd.DataFrame.from_dict(data)

    # Cut publication date to date
    df['publication_date'] = df['publication_date'].str[:10]

    # split location to city and country and drop the location column
    df['city'] = df['locations'].str.split(',').str[0]
    df['country'] = df['locations'].str.split(',').str[1]
    df.drop('locations', axis=1, inplace=True)

    # save the dataframe to a csv file locally first
    df.to_csv('jobs2.csv', index=False)
    print('datafrme saved to local')

    # use linux command to upload file to S3
    subprocess.run(['aws', 's3', 'cp', 'jobs2.csv', 's3://de-exercise-data-bucket/input/job2.csv'])
  
    # Success.
    print('File uploading Done!')





    


    
