import json
# import urllib2
import requests
import pandas as pd
from credentials import alphavantage_api_key as api_key

stock = "GOOGL"
url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={}&interval=1min&apikey={}".format(stock, api_key)
url_csv = "https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol={}&apikey={}&datatype=csv".format(stock, api_key)
# json_file = json.loads(urllib2.request.urlopen(url).decode  )
json_file = json.loads(requests.get(url).text)
pd_data = pd.read_csv(url_csv)
print(pd_data.values)
# print(json_file)
