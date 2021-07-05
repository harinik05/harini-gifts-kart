#-----------------------------------------------------------------------------
# Name:        Shopping Products (cart_shopping.py)
# Purpose:     The purpose of cart shopping is to allow the user to buy products by looking up
# the product name. This captures the data from the database table 'products' and adds the 
# shopping details to transactions and updates the sticks. Time feature was implemented to 
# show the date in the header. When they are buying the product, multiple products can be selected 
# and they can choose to enter different quantities and donation money. The total amount is calculated
# and entered into the transactions with the corresponding dates 
# Author:      Harini Karthik
# Created:     30-March-2021
# Updated:     2-April-2021
#-----------------------------------------------------------------------------
'''
#################################################################################
Class Name - cart_shopping
Dependencies - DB - products and transactions, datetime, messagebox, math
Input - Product No, Quantity, Donation, buttons-add to cart and generate bill
Output - The products will be added to the cart and quantity is reduced from the database. In the transactions, 
the final amount is stored along with the date and product details.
GUI - Shopping Cart Window
Functionality - This program incorporates an add to cart feature wherin the products are added based
on the quantity and donations. Once all of the products are added, generate bill is clicked and the change will be 
calculated. All the purchases are recorded in the transactions table

Change Control:
-----------------------------------------------------------------------------------------------
30-Mar-2021     Harini Karthik          Initial Program created
31-Mar-2021     Harini Karthik          Finished the shopping cart module
02-Apr-2021     Harini Karthik          Updated the UI design
-----------------------------------------------------------------------------------------------
'''
#import all of the libraries needed for the program
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image

# Import mysql connectors
import mysql.connector
from mysql.connector import Error
import tkinter.messagebox
import datetime
import math
import os
py=sys.executable

# Figure out the time using datetime
currentDate=datetime.datetime.now().date()

# Connect to the database
connection = mysql.connector.connect(host='localhost', 
                        database='harinigiftkartfinal',
                        user='root',
                        password='')

mycursor = connection.cursor()
                    
# Create temporary lists to hold all of the products, prices, quantities, and thresholds
products_list=[]
product_price=[]
product_quantity=[]
product_id=[]
r = []

# Define a class for cart shopping
class cart_shopping(Tk):
    def __init__(self):
        super().__init__()
        # Define the window layout 
        self.title("Harini's Gift Kart")            # Window Title
        self.minsize(800,600)                       # Window size
        self.geometry('800x600')
        # Photocredit: Flaticon
        self.iconbitmap('Assets\\surprise.ico')  # Company logo (must be type ico)


        def layout():
            # Split the window into two sides dedicating it to left and right and color them differently
            self.left=Frame(self,width=400,height=800,bg='#52fff9')
            self.left.pack(side=LEFT)

            self.right = Frame(self, width=400, height=800, bg='#f8ff6b')
            self.right.pack(side=RIGHT)


            # Define the heading and which category (self.right or self.left)
            self.heading=Label(self.left,text="MY SHOPPING CART",font=('Times New Roman', 25, 'bold'),fg='black',bg='#52fff9')
            self.heading.place(x=20,y=10)

            self.currentDateLabel=Label(self.right,text="Today's Date: "+str(currentDate),font=('Times New Roman', 20, 'bold'),bg='#f8ff6b',fg='black')
            self.currentDateLabel.place(x=50,y=13)

            # Create a table that collects a list of all of the products and its corresponding details that is purchased by the customer
            self.productTable=Label(self.right,text="PRODUCT NAME",font=('Times New Roman', 12, 'bold'),bg='#f8ff6b',fg='black')
            self.productTable.place(x=0,y=75)

            self.quantityTable = Label(self.right, text="QTY", font=('Times New Roman', 12, 'bold'), bg='#f8ff6b', fg='black')
            self.quantityTable.place(x=200, y=75)

            self.costTable = Label(self.right, text="COST", font=('Times New Roman', 12, 'bold'), bg='#f8ff6b', fg='black')
            self.costTable.place(x=350, y=75)

            self.borderTable = Label(self.right, text="-------------------------------------------------------------------------------", bg='#f8ff6b', fg='black')
            self.borderTable.place(x=0, y=100)

            # Entry Data for the product number and look up
            self.enterId=Label(self.left,text="ENTER PRODUCT ID:",font=('Times New Roman', 12, 'bold'),fg='black',bg='#52fff9')
            self.enterId.place(x=10,y=75)


            self.enterIdEntry=Entry(self.left,width=25,font=('Times New Roman', 12, 'bold'))
            self.enterIdEntry.place(x=180,y=75)
            self.enterIdEntry.focus()

            # Search Button to look up the id and get the appropriate data
            self.searchButtonPic = PhotoImage(file=f"Assets\\loupe.png")
            self.searchButtonResize = self.searchButtonPic.subsample(15,15)
            self.searchButton = Button(self, text = "  Search Product", font=("Times New Roman", 12),width = 200,bg='#ff57f4',command=ajax,image = self.searchButtonResize,
                    compound = LEFT).place(x=100, y=110)

            # Define all of the styles of the entries
            self.productName=Label(self.left,text="",font=('Times New Roman', 15,'bold'),fg='black',bg='#52fff9')
            self.productName.place(x=70,y=200)

            self.priceCalculate = Label(self.left, text="", font=('Times New Roman', 15,'bold'), bg='#52fff9', fg='black')
            self.priceCalculate.place(x=150, y=250)

            # Define the total amount on the right 
            self.totalAmount=Label(self.right,text="",font=('Times New Roman', 15, 'bold'),bg='#f8ff6b',fg='black')
            self.totalAmount.place(x=20,y=480)

        def ajax():
            self.get_id=self.enterIdEntry.get()
            #get the product info with that id and fill i the labels above
            mycursor.execute("SELECT * FROM products WHERE PID= %s",[self.get_id])
            self.pc = mycursor.fetchall()
            # Loop due to multiple fields in the results set through a nested list
            if self.pc:
                # Break the nested list
                for self.r in self.pc:
                    self.get_id=self.r[0]
                    self.get_name=self.r[1]
                    self.get_price=self.r[3]
                    self.get_stock=self.r[2]
                self.productName.configure(text="Product's Name: " +str(self.get_name),fg='black',bg='#52fff9')
                self.priceCalculate.configure(text="Price:$ "+str(self.get_price),fg='black',bg='#52fff9')


                #create the quantity and the donation label
                self.quantityLabel=Label(self.left,text="Enter Quantity:",font=("Times New Roman", 15, 'bold'),fg='black',bg='#52fff9')
                self.quantityLabel.place(x=40,y=312)

                self.quantityLabelEntry=Entry(self.left,width=15,font=("Times New Roman", 12),fg='black')
                self.quantityLabelEntry.place(x=200,y=315)
                self.quantityLabelEntry.focus()

                # Donation
                self.donationLabel = Label(self.left, text="Enter Donation:", font=("Times New Roman", 15, 'bold'),fg='black',bg='#52fff9')
                self.donationLabel.place(x=40, y=370)


                self.donationLabelEntry = Entry(self.left, width=15, font=("Times New Roman", 12), fg='black')
                self.donationLabelEntry.place(x=200, y=373)
                self.donationLabelEntry.insert(END,0)


                # add to cart button
                self.addtocartPic = PhotoImage(file=f"Assets\\online-shopping.png")
                self.addtocartPicResize = self.addtocartPic.subsample(15,15)
                self.addtocartButton = Button(self, text = "  Add to Cart", font=("Times New Roman", 12),width = 150,bg='#ff57f4',command=add_to_cart,image = self.addtocartPicResize,
                    compound = LEFT).place(x=130, y=410)
                

                # Generate bill and change
                self.changeMoneyLabel=Label(self.left,text="Given Amount",font=("Times New Roman", 15, 'bold'),fg='black',bg='#52fff9')
                self.changeMoneyLabel.place(x=40,y=460)

                self.changeMoneyLabelEntry=Entry(self.left,width=15,font=("Times New Roman", 12),fg='black')
                self.changeMoneyLabelEntry.place(x=200,y=463)

                self.changeMoneyPic = PhotoImage(file=f"Assets\dollar.png")
                self.changeMoneyResize = self.changeMoneyPic.subsample(15,15)
                self.changeMoneyButton = Button(self, text = "  Calculate Change", font=("Times New Roman", 12),width = 150,bg='#ff57f4',command=change_func,image = self.changeMoneyResize,
                    compound = LEFT).place(x=130, y=490)
                

                #geneerate bill button
                self.billButton = Button(self.left, text="Generate Bill", width=15, height=1,font=("Times New Roman", 12), bg='#ff57f4',fg='black',command=generate_bill)
                self.billButton.place(x=10, y=550)

                # Quit button
                self.quitButton = Button(self.left, text="Quit", width=15, height=1, font=("Times New Roman", 12),bg='#ff57f4',fg='black',command=self.destroy)
                self.quitButton.place(x=220, y=550)
            else:
                messagebox.showinfo("Error", "Please try again")

        def add_to_cart():
            self.quantity_value=int(self.quantityLabelEntry.get())
            # If the quantity is greater than the stocks, then it will not be available
            if  self.quantity_value >int(self.get_stock):
                tkinter.messagebox.showinfo("Error","Not in stock")
            else:
                #calculate the price first
                self.final_price=(float(self.quantity_value) * float(self.get_price))+(float(self.donationLabelEntry.get()))
                # Append all of the purchased products to the list (temporary ones) defined above for the name, prices, quantity and identification
                products_list.append(self.get_name)
                product_price.append(self.final_price)
                product_quantity.append(self.quantity_value)
                product_id.append(self.get_id)

                # Define the x and y coordinates so that the text can move through
                self.x_index=0
                self.y_index=120
                # Print out the first product in the list by starting at 0 as the counter
                self.counter=0

                # Put up a for loop for inserting more products and iterate for each of the counters that are in the list 
                for self.p in products_list:
                    self.tempname=Label(self.right,text=str(products_list[self.counter]),font=('Times New Roman', 12),bg='#f8ff6b',fg='black')
                    self.tempname.place(x=0,y=self.y_index)
                    self.tempqt = Label(self.right, text=str(product_quantity[self.counter]), font=("Times New Roman", 12), bg='#f8ff6b', fg='black')
                    self.tempqt.place(x=200, y=self.y_index)
                    self.tempprice = Label(self.right, text=str(product_price[self.counter]), font=("Times New Roman", 12), bg='#f8ff6b', fg='black')
                    self.tempprice.place(x=340, y=self.y_index)
# Increase the y index inside of the loop and the counter so that it goes to the next counter and skips spaces down 
                    self.y_index+=65
                    self.counter+=1


                    # Add all of the orices in the list sum(product-price)
                    #total confugure
                    self.totalAmount.configure(text="Total : $. "+str(sum(product_price)),bg='#f8ff6b',fg='black')

                    #delete and refreshes to the "" in order to incorporate the next product
                    self.productName.configure(text="")
                    self.priceCalculate.configure(text="")

                    #autofocus to the enter id
                    # Delete and focus on the entry id. Focus on the quantity label as well
                    self.enterIdEntry.focus()
                    self.quantityLabel.focus()
                    self.enterIdEntry.delete(0,END)

        # Define a function for finding the amount to give to the person (change)
        def change_func():
            # Amount to give = totalamount - given
            self.amount_given=float(self.changeMoneyLabelEntry.get())
            self.our_total=float(sum(product_price))

            self.to_give=self.amount_given-self.our_total

            #label change
            self.amountToGive=Label(self.left,text="Change: $ "+str(self.to_give),font=("Times New Roman", 12),fg='black',bg='#52fff9')
            self.amountToGive.place(x=286 ,y=490)
 
        # Generate bill and reduce the quantity by how much is purchased
        def generate_bill():
            # Get the product number
            mycursor.execute("SELECT * FROM products WHERE PID=%s",[self.get_id])
            # Fetch all of the information
            self.pc = mycursor.fetchall()

            # Define a variable for the old stocks (one that is already in the database)
            for r in self.pc:
                self.old_stock=r[2]

            # Iterate the value through the entire products list
            for i in products_list:
                for r in self.pc:
                    self.old_stock = r[2]
                
                #The new stock is the old minus the quantity value purchses
                self.new_stock=int(self.old_stock) - int(self.quantity_value)
                # Updating the stock 
                mycursor.execute("UPDATE products SET Qty=%s WHERE PID=%s",[self.new_stock,self.get_id])
                connection.commit()

            #Insert into the transactions
            mycursor.execute("INSERT INTO transactions(ProductName,Qty,Amount,InvDate) VALUES(%s,%s,%s,%s)",[self.get_name,self.quantity_value,self.our_total,currentDate])
            connection.commit()
            #print("Decreased")

            tkinter.messagebox.showinfo("success","Please tell about your experience")
            #self.destroy()
# Run the program
        layout()
cart_shopping().mainloop()

