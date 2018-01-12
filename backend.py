import pandas as pd
import requests
import json
import pymysql
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
from credentials import alphavantage_api_key as api_key
from credentials import db_username, db_password, db_name

def get_time_series(time):
    time = time.lower()
    if time=='daily':
        return "TIME_SERIES_DAILY"
    elif time=='weekly':
        return "TIME_SERIES_WEEKLY"
    elif time=='monthly':
        return "TIME_SERIES_MONTHLY"
    else:
        print("INFO : Wrong Time Series. Resetting to Day")
        return "TIME_SERIES_DAILY"

def create_temp_csv(data_frame, stock_name):
        file_name = stock_name+".csv"
        data_frame.to_csv(file_name)

def insert_into_db(df, table_name):
    con_str = 'mysql+pymysql://{}:{}@localhost:3306/mysql'.format(db_username, db_password)
    con = create_engine(con_str, echo=False)
    df.to_sql(name=table_name, con=con, if_exists='replace')
    print("INFO : DataBase Created for table {}".format(table_name))
    return con

def get_data_frame(stock_name, time):
    time_series = get_time_series(time)

    print("INFO : Downloading Data for {}".format(stock_name))
    url_csv = "https://www.alphavantage.co/query?function={}&symbol={}&interval=15min&outputsize=compact&apikey={}&datatype=csv".format(time_series, stock_name, api_key)
    pd_data = pd.read_csv(url_csv)
    print("INFO : Download Complete")

    create_temp_csv(pd_data, stock_name)
    return pd_data



def plt_plot(data, plot_name, num_items):
    x_axis_real = [i[0] for i in data[:num_items]][::-1]    #Reversed the data
    y_axis = [i[1] for i in data[:num_items]][::-1]         #Reversed the data

    x_axis = range(len(x_axis_real))
    plt.xticks(x_axis, x_axis_real, rotation='vertical')

    plt.plot(x_axis, y_axis)
    plt.title(plot_name)
    plt.xlabel('Time Stamp')
    plt.ylabel('Values')
    plt.show()


def plt_two_plot(table_name1, table_name2, data1, data2, plot_name, num_items):
    x_axis_real1 = [i[0] for i in data1[:num_items]][::-1]  #Reversed
    y_axis1 = [i[1] for i in data1[:num_items]][::-1]       #Reversed

    x_axis_real2 = [i[0] for i in data2[:num_items]][::-1]  #Reversed
    y_axis2 = [i[1] for i in data2[:num_items]][::-1]       #Reversed

    x_axis = range(len(x_axis_real1))
    plt.xticks(x_axis, x_axis_real1, rotation='vertical')
    plt.xticks(x_axis, x_axis_real2, rotation='vertical')

    plt.plot(x_axis, y_axis1, label=table_name1)
    plt.plot(x_axis, y_axis2, label=table_name2)
    plt.title(plot_name)
    plt.xlabel('Time Stamp')
    plt.ylabel('Values')
    plt.legend()
    plt.show()


def plot_two_data(table_name1, table_name2, con, num_items):
    df1 = pd.read_sql_table(table_name1, con)
    df2 = pd.read_sql_table(table_name2, con)
    df1 = df1[['timestamp', 'close']]
    df2 = df2[['timestamp', 'close']]
    data1 = df1.values
    data2 = df2.values
    plot_name = table_name1+" vs "+table_name2
    plt_two_plot(table_name1, table_name2, data1, data2, plot_name, num_items)

#PLOT DATA
def plot_data(table_name, con, num_items):
    df = pd.read_sql_table(table_name, con)
    df = df[['timestamp', 'close']]
    data = df.values
    plt_plot(data, table_name, num_items)
    # print(df.head())

# LOAD DATA
def load_data(stock_name, time):
    df = get_data_frame(stock_name, time)
    # df = df[['timestamp','open', 'high', 'low', 'close', 'volume']]
    con = insert_into_db(df, stock_name)
    return con

# con = load_data("GOOGL", "day")
# plot_data("GOOGL", con)
