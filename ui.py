import tkinter as tk
from tkinter.ttk import *
import tkinter.messagebox as tkm

from backend import load_data, plot_data, plot_two_data

base = tk.Tk()					# bottommost/base/root window definition
base.title("StockPlot");
base.geometry("600x800")

title_text = 'StockPlot';       # heading inside window
title_label = tk.Label(base,text=title_text,font=("Helvetica",20,"bold"))
title_label.pack(pady=15)

header1_text="Collect Stock Data"
header1_label = tk.Label(base,text = header1_text,font=("Helvetica,15,bold"))
header1_label.pack(pady=(5,2))

addstock_entry = tk.Entry()
addstock_default = 'Enter Stock Name'
addstock_entry.insert(0,addstock_default)
addstock_entry.pack()

stocks = ['GOOGL','TSLA'," "] # replace with all stocks present in db + append a  " " at the end
stocks.sort()

def addStock():         # when add button is pressed, this fuction is executed
	stockname = addstock_entry.get()
	if stockname==addstock_default:
		tkm.showinfo("Info","Please insert a stock name!")
	else:
		if stockname in stocks:
			tkm.showinfo("Info","Stock "+stockname+" already present in Database!")
		else:
			fetchStockData(stockname)
			tkm.showinfo("Info","Added Successfully!")

def fetchStockData(stockname):    # put fetching stock data and storing in db here
	# print("fetching")              # replace print statement with you know what B-)
	updateList(stockname)
	addstock_entry.delete(0,'end')
	addstock_entry.insert(0,addstock_default)

def updateList(stockname):
	stocks.append(stockname)
	# print(stocks)                  # you dont really need this. just checking if it actually works
	stock_dropdown.set_menu(stocks[0],*stocks)      #update dropdown list
	stock_dropdown2.set_menu(stocks[0],*stocks)     #update dropdown list


addstock_button = tk.Button(base,text="Add",command=addStock)
addstock_button.config(width=17)
addstock_button.pack()

header2_text="Pick Stock"
header2_label = tk.Label(base,text = header2_text,font=("Helvetica,15,bold"))
header2_label.pack(pady=(15,2))

stock1 = tk.StringVar(base)
stock1.set(stocks[0])
stock_dropdown = OptionMenu(base,stock1,*stocks)
stock_dropdown.config(width=14)
stock_dropdown.pack()

stock2 = tk.StringVar(base)
stock2.set(stocks[0])
stock_dropdown2 = OptionMenu(base,stock2,*stocks)
stock_dropdown2.config(width=14)
stock_dropdown2.pack(pady=(5,1))

header3_text="Pick Timescale"
header3_label = tk.Label(base,text = header3_text,font=("Helvetica,15,bold"))
header3_label.pack(pady=(15,2))

timescale1 = tk.StringVar(base)
timescale = [' ','Daily','Weekly','Monthly']
timescale1.set(timescale[0])
timescale_dropdown = OptionMenu(base,timescale1,*timescale)
timescale_dropdown.config(width=14)
timescale_dropdown.pack()

header4_text="Pick Datapoint Count"
header4_label = tk.Label(base,text = header4_text,font=("Helvetica,15,bold"))
header4_label.pack(pady=(15,2))

datapoint1 = tk.StringVar(base)
datapoint = [' ','5','10','15','20','25','30','50','75','100']   # type cast to str to get datapoint value. values given as strings to avoid problems while making dropdown
datapoint1.set(datapoint[0])
datapoint_dropdown = OptionMenu(base,datapoint1,*datapoint)
datapoint_dropdown.config(width=14)
datapoint_dropdown.pack()

def onPlotPress():
    s1 = stock1.get() #stock1 name as str
    s2 = stock2.get() #stock2 name as str
    t1 = timescale1.get() # timescale 'Daily' 'Weekly' or 'Monthly'
    d1 = datapoint1.get() # datapoint count as str
    if t1 == ' ':
        tkm.showinfo('Info','Select a Timescale!')
    if d1 == ' ':
        tkm.showinfo('Info','Select number of data points!')
    if s1==' ' and s2==' ':
        tkm.showinfo("Info","Select at least one stock to plot!")
    elif s2==' ':   #Stock 1
        con = load_data(s1, t1)
        plot_data(s1, con, int(d1))
    elif s1==' ':
        con = load_data(s2, t1)
        plot_data(s1, con, int(d1))
    elif s1==s2:
        con = load_data(s1, t1)
        plot_data(s1, con, int(d1))
    else:
        con = load_data(s1, t1)
        load_data(s2, t1)
        plot_two_data(s1, s2, con, int(d1))



plot_button = tk.Button(base,text="Plot",command=onPlotPress)
plot_button.config(width=17)
plot_button.pack(pady=(15,1))

bg = tk.PhotoImage(file="bg.png")
bg_label = tk.Label(base,image=bg)
bg_label.pack()

base.mainloop()
