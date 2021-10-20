from tkinter import *
from tkhtmlview import HTMLLabel
import requests
from bs4 import BeautifulSoup
import whois


def url_info():
    url = whois.whois(str(e1.get()))
    url = 'https://www.geeksforgeeks.org/sorting-algorithms/'
    website = requests.get(url)
    website_text = website.text
    soup = BeautifulSoup(website_text)
    for link in soup.find_all('a'):
        href = link.get('href')
        links.append(href)
    for i in range(len(links)):
        server[i].set(links[i])


links = []
# object of tkinter
# and background set for aqua
master = Tk()
master.configure(bg='aqua')
master.title('Link Finder')
master.iconbitmap('./link.ico')
master.geometry('800x600')

# Variable Classes in tkinter
server = [i for i in range(600)]
for i in range(len(server)):
    server[i] = StringVar()

# Creating label for each information
# name using widget Label
Label(master, text="Website URL : ", bg="aqua").grid(row=0, sticky=W)
Label(master, text="Server Name :", bg="aqua").grid(row=3, sticky=W)


# Creating lebel for class variable
# name using widget Entry
Label(master, text="", textvariable=server,
      bg="aqua").grid(row=3, column=1, sticky=W)


e1 = Entry(master)
e1.insert(INSERT, 'https://www.geeksforgeeks.org/python-setting-and-retrieving-values-of-tkinter-variable/')
e1.grid(row=0, column=1)

# creating a button using the widget
# Button that will call the submit function
b = Button(master, text="Show", command=url_info, bg="powderblue")
b.grid(row=0, column=2, columnspan=2, rowspan=2, padx=5, pady=5,)

mainloop()
