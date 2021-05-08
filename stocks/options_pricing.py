import requests
import json
import time
import pandas as pd
import matplotlib.pyplot as plt

class Options():
    def __init__(self, ticker):
        self.baseURL = 'https://query2.finance.yahoo.com/v7/finance/options/'
        self.ticker = ticker
        self.option = self.baseURL+ticker

        raw = requests.get(self.option) 
        processed_data = json.loads(raw.text)
        self.chain = processed_data['optionChain']['result'][0]
    
    def quote(self):
        dictionary = self.chain['quote']
        for key in dictionary:
            print(key, ' : ', dictionary[key])
    
    def processedExpirationDates(self): 
        dates = []
        expirationDates = self.chain['expirationDates']
        for key in expirationDates:
            dates.append(time.strftime('%m-%d-%Y' , time.localtime(key+43200))) # 43200s (12 hrs) added to raw date to round up day 
        return dates 
    
    def rawExpirationDates(self): 
        return self.chain['expirationDates']

    def calls(self, strike, raw_date):
        
        raw = requests.get(self.option+'?date='+str(raw_date)) 
        processed_data = json.loads(raw.text)
        self.chain = processed_data['optionChain']['result'][0]
        
        price = -1
        options = self.chain['options'][0]
        for i in options['calls']:

            if int(i['strike']) == int(strike):
                price = i['lastPrice']
        return price

    def puts(self):
        options = self.chain['options'][0]
        print(options['puts'])



if __name__ == '__main__':
    stock = Options('AAPL')
    colors = ['green', 'red', 'blue', 'orange', 'yellow']
    count = 0
    plt.figure()
    for date in stock.processedExpirationDates():
        prices = []
        for i in stock.rawExpirationDates():
            prices.append(stock.calls(127, i))
        plt.plot(stock.processedExpirationDates(), prices, color=colors[ (count+1)%len(colors) ])

    plt.xlabel('Countries')
    plt.xticks(rotation = 90)
    plt.ylabel('Population in million')
    plt.title('Pakistan India Population till 2010')
    plt.show()
    