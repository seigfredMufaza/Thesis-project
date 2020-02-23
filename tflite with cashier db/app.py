from tkinter import *
import tkinter.messagebox
from tkinter import Tk
from db import Database
import os
from db import *
import functools

# db.reset_all()

# Instanciate database object
db = Database('jsj.db')


# **** Functions ****

def addorange():
    db.updateorange()
    populate_list()
    populate_totalp()
    populate_totalw()


def addapple():
    db.updateapple()
    populate_list()
    populate_totalp()
    populate_totalw()


def addbanana():
    db.updatebanana()
    populate_list()
    populate_totalp()
    populate_totalw()


def addtocart():
    top = Toplevel()
    top.title("Products")
    top.geometry("300x300+730+280")

    # Orange
    #photo_orange = PhotoImage(file="ui/Orange.png")
    button_orange = Button(top, text="Orange", relief="raised",
                           bd="3", height=2, width=4, command=addorange)
    button_orange.bind("<Button-1>")
    button_orange.place(x=15, y=15)

    # Apple
    button_apple = Button(top, text="Apple", relief="raised",
                          bd="3", height=2, width=4, command=addapple)
    button_apple.bind("<Button-1>")
    button_apple.place(x=85, y=15)

    # Banana
    button_banana = Button(top, text="Banana", relief="raised",
                           bd="3", height=2, width=4, command=addbanana)
    button_banana.bind("<Button-1>")
    button_banana.place(x=155, y=15)

    #tkinter.messagebox.showinfo('JSJ marketing by Group 10', 'An item is added to your Cart :)')


def checkout():
    tkinter.messagebox.showinfo('JSJ Marketing by Group 10',
                                'Make sure to double check your items and thank you for shopping :)')
    question = tkinter.messagebox.askquestion(
        'Warning', 'Are sure you want to checkout?')
    if question == 'yes':
        os.system("sudo chmod a+w /dev/usb/lp0")
        populate_list()
        populate_totalp()
        populate_totalw()

        pro = db.fetch_orange()
        proo = ''.join(str(e) for e in pro)

        pra = db.fetch_apple()
        praa = ''.join(str(e) for e in pra)

        prb = db.fetch_banana()
        prbb = ''.join(str(e) for e in prb)

        prp = db.display_price()
        prpp = ''.join(str(e) for e in prp)

        prw = db.display_weight()
        prww = ''.join(str(e) for e in prw)

        os.system(
            "sudo echo -e '    Item Qty Price(P) Weight(g) \n' > /dev/usb/lp0")
        os.system("sudo echo -e '" + proo + "' > /dev/usb/lp0")
        os.system("sudo echo -e '" + praa + "' > /dev/usb/lp0")
        os.system("sudo echo -e '" + prbb + "\n' > /dev/usb/lp0")
        os.system("sudo echo -e 'Total Price(P)" + prpp + "' > /dev/usb/lp0")
        os.system("sudo echo -e 'Total Weight(g)" +
                  prww + "\n\n' > /dev/usb/lp0")
        os.system(
            "sudo echo -e 'Thank you for Shopping! \nJSJ Marketing \n\n\n' > /dev/usb/lp0")

        #print("asd" +pre+ "dsa")
        """db.reset_all()"""
        populate_list()
        populate_totalp()
        populate_totalw()
    if question == 'no':
        print('Enjoy shopping')


def populate_list():
    parts_list.delete(0, END)
    for row in db.fetch():
        parts_list.insert(END, row)


def populate_totalp():
    displaytotalp.delete(0, END)
    for roww in db.display_price():
        displaytotalp.insert(END, roww)


def populate_totalw():
    displaytotalw.delete(0, END)
    for rowww in db.display_weight():
        displaytotalw.insert(END, rowww)


def select_item(event):
    try:
        global selected_item
        index = parts_list.curselection()[0]
        selected_item = parts_list.get(index)
        print(selected_item)

        item_entry.delete(0, END)
        quantity_entry.delete(0, END)
        price_entry.delete(0, END)
        weight_entry.delete(0, END)
    except IndexError:
        pass


def remove_item():
    db.remove(selected_item[0])
    populate_list()
    populate_totalp()
    populate_totalw()


def resetbox():
    tkinter.messagebox.showinfo('JSJ Marketing by Group 10',
                                'Make sure to double check your items')
    question = tkinter.messagebox.askquestion(
        'Warning', 'Are sure you want to reset all items?')
    if question == 'yes':
        db.reset_all()
        populate_list()
        populate_totalp()
        populate_totalw()
    if question == 'no':
        print('Enjoy shopping')


def refresh():
    populate_list()
    populate_totalp()
    populate_totalw()


# Main Window
root = Tk()
root.title('JSJ Marketing by Group 10')

# **** Calling an image from the project file ****
# **** The simplest form, using PhotoImage() class ****
# **** You can only do this if you copy a file then paste it inside the project ****
logoPhoto = PhotoImage(file="ui/logoz.png")
logophotolabel = Label(root, image=logoPhoto)
logophotolabel.place(x=15, y=15, anchor=NW)

# **** Picture button. ADD TO CART. DELETE ITEM. PRINT ALL ITEM ****
photoadd = PhotoImage(file="ui/addsz.png")
button_1 = Button(root, image=photoadd, relief="raised",
                  bd="3", command=addtocart)
button_1.bind("<Button-1>", addtocart)
button_1.place(x=40, y=550)

photodel = PhotoImage(file="ui/delete.png")
button_2 = Button(root, image=photodel, relief="raised",
                  bd="3", command=remove_item)
button_2.bind("<Button-1>")
button_2.place(x=160, y=550)

photoprint = PhotoImage(file="ui/print.png")
button_3 = Button(root, image=photoprint, relief="raised",
                  bd="3", command=checkout)
button_3.bind("<Button-1>", checkout)
button_3.place(x=420, y=550)

photores = PhotoImage(file="ui/reset.png")
button_4 = Button(root, image=photores, relief="raised",
                  bd="3", command=resetbox)
button_4.bind("<Button-1>")
button_4.place(x=310, y=550)

button_5 = Button(root, text="refresh", relief="raised",
                  bd="3", command=refresh)
button_5.bind("<Button-1>")
button_5.place(x=400, y=400)

"""TEXTS"""
item_text = StringVar()
itemlabel = Label(root, text='ITEM')
itemlabel.place(x=120, y=120)
item_entry = Entry(root, textvariable=item_text)

quantity_text = StringVar()
quantitylabel = Label(root, text='QTY')
quantitylabel.place(x=200, y=120)
quantity_entry = Entry(root, textvariable=quantity_text)

price_text = StringVar()
pricelabel = Label(root, text='PRICE(₱)')
pricelabel.place(x=230, y=120)
price_entry = Entry(root, textvariable=price_text)

weight_text = StringVar()
weightlabel = Label(root, text='WEIGHT(g)')
weightlabel.place(x=310, y=120)
weight_entry = Entry(root, textvariable=weight_text)

# Parts List (Listbox)
parts_list = Listbox(root, relief="raised", height=5,
                     width=20, border=0, font=('Roboto', 30))
# columnspan=3, rowspan=6, pady=10, padx=20)
parts_list.grid(padx=40, pady=138, columnspan=3, rowspan=6)
parts_list.bind('<<ListboxSelect>>', select_item)

# Parts List (Listbox)
displaytotalp = Listbox(root, relief="raised", height=1,
                        width=10, border=0, font=('Roboto', 14))
displaytotalp.place(x=280, y=420)
displaytotalp.bind('<<ListboxSelect>>', select_item)

totalprice = StringVar()
totalpricelabel = Label(root, text='Total Price(₱)', font=('Roboto', 13))
totalpricelabel.place(x=135, y=420)
totalprice_entry = Entry(root, textvariable=totalprice)

# Parts List (Listbox)
displaytotalw = Listbox(root, relief="raised", height=1,
                        width=10, border=0, font=('Roboto', 14))
displaytotalw.place(x=280, y=440)
displaytotalw.bind('<<ListboxSelect>>', select_item)

totalweight = StringVar()
totalweightlabel = Label(root, text='Total Weight(g)', font=('Roboto', 13))
totalweightlabel.place(x=135, y=440)
totalweight_entry = Entry(root, textvariable=totalweight)

# Create scrollbar
scrollbar = Scrollbar(root, width=20, border=0)
scrollbar.place(x=509, y=280, anchor=W)

# Set scroll to listbox
parts_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=parts_list.yview)
# Bind select
parts_list.bind('<<ListboxSelect>>', select_item)


populate_list()
populate_totalp()
populate_totalw()


root.geometry('560x680+600+3')
root.mainloop()
