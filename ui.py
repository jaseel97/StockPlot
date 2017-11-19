import Tkinter as tk
from ttk import *
import tkMessageBox as tkm

base = tk.Tk()
base.title("StockPlot");
base.geometry("600x800")

title_text = 'StockPlot';
title_label = tk.Label(base,text=title_text,font=("Helvetica",20,"bold"))
title_label.pack(pady=30)

header1_text="Add Stock Data to Database"
header1_label = tk.Label(base,text = header1_text,font=("Helvetica,15,bold"))
header1_label.pack(pady=(5,2))
	
addstock_entry = tk.Entry()
addstock_default = 'Enter Stock Name'
addstock_entry.insert(0,addstock_default)
addstock_entry.pack()

stocks = ['GOOG','YHOO']

def addStock():
	stockname = addstock_entry.get()
	if stockname==addstock_default:
		tkm.showinfo("Info","Please insert a stock name!")
	else:
		if stockname in stocks:
			tkm.showinfo("Info","Stock "+stockname+" already present in Database!")
		else:
			fetchStockData(stockname)

def fetchStockData(stockname):
	print "fetching"
	updateList(stockname)
	addstock_entry.delete(0,'end')
	addstock_entry.insert(0,addstock_default)
	
def updateList(stockname):
	stocks.append(stockname)
	print stocks
	stock_dropdown.set_menu(stocks[0],*stocks)
				

addstock_button = tk.Button(base,text="Add",command=addStock)
addstock_button.config(width='17')
addstock_button.pack()

header2_text="Pick Stock"
header2_label = tk.Label(base,text = header2_text,font=("Helvetica,15,bold"))
header2_label.pack(pady=(20,2))
	
stockdefault = tk.StringVar(base)
stockdefault.set(stocks[0])
stock_dropdown = OptionMenu(base,stockdefault,*stocks)
stock_dropdown.pack()

bg = tk.PhotoImage(file="bg.png")
bg_label = tk.Label(base,image=bg)
bg_label.pack(pady=20)

base.mainloop()

