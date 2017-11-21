import pandas as pd
import requests
import json
import MySQLdb
from credentials import alphavantage_api_key as api_key
from credentials import db_username, db_password, db_name

def get_time_series(time):
    time = time.lower()
    if time=="day":
        return "TIME_SERIES_DAILY"
    elif time=="week":
        return "TIME_SERIES_WEEKLY"
    elif time=="month":
        return "TIME_SERIES_MONTHLY"
    else:
        print("INFO : Wrong Time Series. Resetting to Day")
        return "TIME_SERIES_DAILY"

def create_temp_csv(data_frame, stock_name):
        file_name = stock_name+".csv"
        data_frame.to_csv(file_name)

def insert_into_db(df, table_name):
    db = MySQLdb.connect(host="localhost",
                        user=db_username,
                        passwd=db_password)
                        # db=db_name)
                        # port=3306)
    df.to_sql(con=db, name=table_name, if_exists='replace', flavor='sqlite')
    print("INFO : DataBase Created.")

def get_data_frame(stock_name="GOOGL", time="month"):
    time_series = get_time_series(time)
    url_csv = "https://www.alphavantage.co/query?function={}&symbol={}&interval=15min&outputsize=full&apikey={}&datatype=csv".format(time_series, stock_name, api_key)
    pd_data = pd.read_csv("GOOGL.csv")
    return pd_data
    # create_temp_csv(pd_data, stock_name)
    # insert_into_db(pd_data, stock_name)

def load_data(stock_name, time):
    df = get_data_frame(stock_name, time)
    insert_into_db(df, stock_name)

load_data("GOOGL", "month")
