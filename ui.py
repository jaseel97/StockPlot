import Tkinter as tk
from ttk import *
import tkMessageBox as tkm

base = tk.Tk()
base.title("StockPlot");
base.geometry("600x700")

title_text = 'StockPlot';
title_label = tk.Label(base,text=title_text,font=("Helvetica",20,"bold"))
title_label.pack(pady=30)

header1_text="Collect Stock Data"
header1_label = tk.Label(base,text = header1_text,font=("Helvetica,15,bold"))
header1_label.pack(pady=(5,2))

addstock_entry = tk.Entry()
addstock_default = 'Enter Stock Name'
addstock_entry.insert(0,addstock_default)
addstock_entry.pack()

stocks = ['GOOG','YHOO'," "] # replace with all stocks preent in db + append a  " " at the end
stocks.sort()

def addStock():
	stockname = addstock_entry.get()
	if stockname==addstock_default:
		tkm.showinfo("Info","Please insert a stock name!")
	else:
		if stockname in stocks:
			tkm.showinfo("Info","Stock "+stockname+" already present in Database!")
		else:
			tkm.showinfo("Info","Added Successfully!")
			fetchStockData(stockname)

def fetchStockData(stockname):
	print("fetching")
	updateList(stockname)
	addstock_entry.delete(0,'end')
	addstock_entry.insert(0,addstock_default)

def updateList(stockname):
	stocks.append(stockname)
	print(stocks)
	stock_dropdown.set_menu(stocks[0],*stocks)
	stock_dropdown2.set_menu(stocks[0],*stocks)


addstock_button = tk.Button(base,text="Add",command=addStock)
addstock_button.config(width=17)
addstock_button.pack()

header2_text="Pick Stock"
header2_label = tk.Label(base,text = header2_text,font=("Helvetica,15,bold"))
header2_label.pack(pady=(20,2))

stock1 = tk.StringVar(base)
stock1.set(stocks[0])
stock_dropdown = OptionMenu(base,stock1,*stocks) ####
stock_dropdown.config(width=14)
stock_dropdown.pack()

stock2 = tk.StringVar(base)
stock2.set(stocks[0])
stock_dropdown2 = OptionMenu(base,stock2,*stocks)
stock_dropdown2.config(width=14)
stock_dropdown2.pack(pady=(5,1))

def plotPress():
	s1 = stock1.get()
	s2 = stock2.get()
	if s1==' ' and s2==' ':
		tkm.showinfo("Info","Select atleast one stock to plot!")
	elif s2==' ':
		print("Plot only stock1")
	elif s1==' ':
		print("Plot only stock2")
	elif s1==s2:
		print("PLot only stock1")
	else:
		print("Plot stock1 and stock2")


plot_button = tk.Button(base,text="Plot",command=plotPress)
plot_button.config(width=17)
plot_button.pack(pady=(20,1))

bg = tk.PhotoImage(file="bg.png")
bg_label = tk.Label(base,image=bg)
bg_label.pack()

base.mainloop()
