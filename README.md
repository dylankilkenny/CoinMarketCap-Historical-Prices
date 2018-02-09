# CoinMarketCap-Historical-Prices
This script scrapes data from the [historical data](https://coinmarketcap.com/currencies/ethereum/historical-data/) tab on coinmarketcap.com

## Install & Run

#### Download and install   
```
$ git clone https://github.com/dylankilkenny/CoinMarketCap-Historical-Prices.git
$ cd CoinMarketCap-Historical-Prices
$ virtualenv . 
$ source bin/activate
$ pip3 install -r requirements.txt
```

#### Running
To run the script and gather data for all listed cryptocurrencys on coinmarketcap you need to pass the start date and end date in YYYYMMDD format

```    
$ python run.py 20170101 20180201
``` 
you can also specify a cryptocurrency with a third argument

```    
$ python run.py 20170101 20180201 ethereum
``` 


