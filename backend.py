import pandas as pd
import requests
import json
from credentials import alphavantage_api_key as api_key

def get_time_series(time):
    time = time.lower()
    if time="day":
        return "TIME_SERIES_DAILY"
    elif time="week":
        return "TIME_SERIES_WEEKLY"
    elif time="month":
        return "TIME_SERIES_MONTHLY"
    else:
        print("INFO : Wrong Time Series. Resetting to Day")
        return "TIME_SERIES_DAILY"

def get_data_frame(stock_name="GOOGL", time="month"):
    time_series = get_time_series(time)
    url_csv = "https://www.alphavantage.co/query?function={}&symbol={}&interval=15min&outputsize=full&apikey={}&datatype=csv".format(time_series, stock_name, api_key)
    pd_data = pd.read_csv(url_csv)
    return pd_data
