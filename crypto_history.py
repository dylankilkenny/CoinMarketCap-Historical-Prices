#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Script to gather historical cryptocurrency data from coinmarketcap.com (cmc) """

import json
import requests
from bs4 import BeautifulSoup
import csv
import sys
from time import sleep


def CoinNames():
    """Gets ID's of all coins on cmc"""

    names = []
    response = requests.get("https://api.coinmarketcap.com/v1/ticker/?limit=0")
    respJSON = json.loads(response.text)
    for i in respJSON:
        names.append(i['id'])
    return names

def gather(startdate, enddate, names):
    historicaldata = []
    counter = 1

    if len(names) == 0:
        names = CoinNames()

    for coin in names:
        sleep(10)
        r  = requests.get("https://coinmarketcap.com/currencies/{0}/historical-data/?start={1}&end={2}".format(coin, startdate, enddate))
        data = r.text
        soup = BeautifulSoup(data, "html.parser")
        table = soup.find('table', attrs={ "class" : "table"})

        #Add table header to list
        if len(historicaldata) == 0:
            headers = [header.text for header in table.find_all('th')]
            headers.insert(0, "Coin")

        for row in table.find_all('tr'):
            currentrow = [val.text for val in row.find_all('td')]
            if(len(currentrow) != 0):
                currentrow.insert(0, coin)
            historicaldata.append(currentrow)

        print("Coin Counter -> " + str(counter), end='\r')
        counter += 1
    return headers, historicaldata

def _gather(startdate, enddate):
    """ Scrape data off cmc"""

    if(len(sys.argv) == 3):
        names = CoinNames()
    else:
        names = [sys.argv[3]]

    headers, historicaldata = gather(startdate, enddate, names)

    Save(headers, historicaldata)

def Save(headers, rows):

    if(len(sys.argv) == 3):
        FILE_NAME = "HistoricalCoinData.csv"
    else:
        FILE_NAME = sys.argv[3] + ".csv"

    with open(FILE_NAME, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(row for row in rows if row)
    print("Finished!")

if __name__ == "__main__":

    startdate = sys.argv[1]
    enddate = sys.argv[2]

    _gather(startdate, enddate)

