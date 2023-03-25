#PROGRAM TO GET DESKTOP NOTIFICATION ABOUT COVID CASES AND DEATHS COUNTRYWISE

#from plyer module import notification
from plyer import notification
#import requests module
import requests
#from bs4 module import beautifulsoup method
from bs4 import BeautifulSoup
#from time module to get notification at regular times
import time
#importing tkinter for gui part
import tkinter as tk
from tkinter.ttk import *

#Function to notify required message with icon and title
def notifyMe(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = r'Desktop\covid.ico',
        timeout = 6
    )
#Function to access data from specified url using get method in requests module
def getData(url):
    r = requests.get(url)
    return r.text

#creating GUI using tkinter module
app = tk.Tk()
app.geometry('400x500')
app.title('countries')
#img=tk.PhotoImage(file=r'Desktop\covid1.png')
#photoimage = img.subsample(3, 3)
l=Label(master=app,text='select the countries and close')
l.place(x=20,y=20)
lb=Label(app,text='covid updates',font=("Arial", 25))
lb.pack()

la=Label(app,text='select countries')
la.pack()

con=[]
def clicked():
    selected = box.curselection()  # returns a tuple
    for idx in selected:
        con.append(box.get(idx))
    

box = tk.Listbox(app, selectmode=tk.MULTIPLE, height=16,width=20)
countries = ['India','United States', 'Italy','Pakistan','Nepal','Switzerland',
             'France','Russia','Spain','Turkey','Germany','Poland','Japan','Sri Lanka','Egypt','Myanmar']
for val in countries:
    box.insert(tk.END, val)

box.pack()

button = tk.Button(app, text='Show', width=25, command=clicked)
button.pack()

exit_button = tk.Button(app, text='Close', width=25, command=app.destroy)
exit_button.pack()

app.mainloop()


if __name__ == "__main__":
    while True:
        #call getData method providing the url from which you want the data
        myHtmlData = getData('https://www.worldometers.info/coronavirus/countries-where-coronavirus-has-spread/')
        #Beautiful Soup is a Python library for pulling data out of HTML and XML files.
        soup = BeautifulSoup(myHtmlData, 'html.parser')
        print(soup)
        #create a empty string myDataStr into which we further add required data from the data we got from BeautifulSoup
        myDataStr = ""
        
        for tr in soup.find_all('tbody')[0].find_all('tr'):
            myDataStr += tr.get_text()   
        myDataStr = myDataStr[1:]
        itemList = myDataStr.split("\n\n")
        
        #select different countries from the list displayed on gui for which you want the notification
        
        
        for item in itemList[0:100]:
            dataList = item.split('\n')
            if dataList[0] in con: 
                nTitle = 'Cases of COVID-19'
                nText = f"COUNTRY: {dataList[0]}\ncases : {dataList[1]} & deaths : {dataList[2]}\n"
                #Calling notifyMe function
                notifyMe(nTitle, nText)
                #Using sleep method so that the notification will be in our view for 2 seconds
                time.sleep(2)
        #using time.sleep method again to get notified every 1hr
        time.sleep(1)

