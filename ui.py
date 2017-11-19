import Tkinter as tk
import tkMessageBox as tkm

base = tk.Tk()
base.title("StockPlot");
base.geometry("600x800")

title_text = 'StockPlot';
title_label = tk.Label(base,text=title_text,font=("Helvetica",20,"bold"))
title_label.pack(pady=30)
	
addstock_entry = tk.Entry()
addstock_default = 'Enter Stock Name'
addstock_entry.insert(0,addstock_default)
addstock_entry.pack()

stocks = ['GOOG']

def addStock():
	stockname = addstock_entry.get()
	if stockname==addstock_default:
		tkm.showinfo("Info","Please insert a stock name!")
		#print "Please insert a stock name!"
	else:
		if stockname in stocks:
			tkm.showinfo("Info","Stock "+stockname+" already present in Database!")
		else:
			fetchStockData()	

addstock_button = tk.Button(base,text="Add",command=addStock)
addstock_button.pack()

bg = tk.PhotoImage(file="bg.png")
bg_label = tk.Label(base,image=bg)
bg_label.pack(pady=200)

base.mainloop()

