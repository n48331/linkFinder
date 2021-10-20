from tkinter import *
from tkinter.ttk import Progressbar
import requests
from bs4 import BeautifulSoup
import time


def findLink():
    links = []
    url = urle.get()
    website = requests.get(url, verify=False)
    website_text = website.text
    soup = BeautifulSoup(website_text)
    c = 0
    for link in soup.find_all('a'):
        href = link.get('href')
        links.append(href)
    ll = len(links)
    if 500 > ll:
        for href in links:
            p = 1/(ll)*100
            bar['value'] += (p)
            c += 1
            htmlp.insert(INSERT, f'>>> {href}\n')
            l = f'{c} / {ll} links found'
            server.set(l)
            pl = int((c/ll)*100)
            percent.set(str(pl)+'%')
            time.sleep(0.12)

            root.update_idletasks()
    else:
        server.set(
            f"Can load all {ll} links.The no of Links Should be less than 500 to load here")


root = Tk()
root.config(bg='powderblue')
root.option_add('verdana', '19')
root.title('Link Finder')
root.iconbitmap('./link.ico')
root.geometry('800x600')

server = StringVar()
# input link
Label(root, text='Enter Website link', bg="powderblue").pack()
urle = Entry(root, width=80)
urle.insert(INSERT, 'https://google.com')
urle.pack()

# button
findButton = Button(root, text='Find Links',
                    command=findLink)
findButton.pack(pady=10)

# progressbar
bar = Progressbar(root, orient=HORIZONTAL, length=600)
bar.pack()
percent = StringVar()
percentLabel = Label(root, textvariable=percent).pack()

# no of links
Label(root, text='', textvariable=server, bg="powderblue").pack()

# textbox with links
htmlp = Text(root, font=("Arial Bold", 10), width=100, height=80)
htmlp.pack(padx=10, pady=5)


root.mainloop()
