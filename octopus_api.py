import csv, json, sys
import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

url_tarif = os.getenv("url_tarif")
api_key = os.getenv("api_key")
url_meter = os.getenv("url_meter")
datename = datetime.now().strftime("%y%m%d")
csvdir = '/www/data/octopus/'

def get_api_data(url):
    response = requests.get(url, auth=(api_key, ''))
    data = response.json()
    results = data['results']
    return results


def write_data_csv(dataname, filename):
    csvfile = csvdir + filename + datename + '.csv'
    # open a file for writing
    jason_data = open(csvfile, 'w', newline='')

    # create the csv writer object
    csvwriter = csv.writer(jason_data)
    count = 0
    for emp in dataname:
        if count == 0:
            header = emp.keys()
            csvwriter.writerow(header)
            count += 1
        csvwriter.writerow(emp.values())
    jason_data.close()


tarif_data = get_api_data(url_tarif)
write_data_csv(tarif_data, "tarif")

meter_data = get_api_data(url_meter)
write_data_csv(meter_data, 'meter')
