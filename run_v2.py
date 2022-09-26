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
    aws_output_dest_s3 = 's3://' + app_config['aws']['bucket'] + app_config['aws']['folder']

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
    
    data = response_API.text
    print('API Reading Done!')

    # building the dataframe
    print('Building the dataframe...')
    data_json = json.loads(data)

    # converting the json file to a dataframe
    df = pd.json_normalize(data_json["results"])

    # taking certain columns which are in our interest
    df = df[["company.name", "locations", "name", "type", "publication_date"]]

    # renaming those columns to have better headers for our table
    df.rename(columns = {"company.name" : "company", "name" : "job", "type" : "job_type", "publication_date" : "date"}, inplace=True)

    # split location to city and country and drop the location column
    df["locations"] = df["locations"].apply(lambda x : x[0]["name"])
    df[['city','country']] = df.locations.str.split(", ", expand=True)
    df.drop('locations', axis=1, inplace=True)

    # reordering the columns to be in the requested order
    df = df[['date', 'job_type', 'job', 'company', 'city', 'country']]
    
    # Cut publication date (date and time) to date
    df["date"] = df["date"].apply(lambda x : x[:10])

    # filling the "null" values in our table
    df['country'] = df['country'].fillna(value=df['city'])

    # save the dataframe to a csv file locally first
    df.to_csv('jobs2.csv', index=False)
    print('datafrme saved to local')

    # use linux command to upload file to S3
    subprocess.run(['aws', 's3', 'cp', 'jobs2.csv', aws_output_dest_s3])
  
    # Success.
    print('File uploading Done!')





    


    
