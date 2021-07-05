#-----------------------------------------------------------------------------
# Name:        Adding Product (add_product.py)
# Purpose:     The purpose of this program is to add the products into the products table
# in Harini's Gifts Kart Database. It adds details such as the product name, cost, 
# threshold quantity (for buying product later), quantity available currently. 
# Author:      Harini Karthik
# Created:     26-March-2021
# Updated:     2-April-2021
#-----------------------------------------------------------------------------
'''
#################################################################################
Class Name - add_product
Dependencies - DB - products, messagebox
Input - productname, cost per product, quantity, threshold
Output - Messagebox display with success (added product), and the product will be added to the products table
GUI - Add Product Window
Functionality - This program is used for adding the product and its corresponding details to the products
table in the database

Change Control:
-----------------------------------------------------------------------------------------------
26-Mar-2021     Harini Karthik          Initial Program created
28-Mar-2021     Harini Karthik          Integrated DB and fixed issues
02-Apr-2021     Harini Karthik          Updated the UI design
-----------------------------------------------------------------------------------------------
'''
# Import the required libraries
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error 


#Declare the environmental constants
myPassword = 'root'
myDatabase = 'harinigiftkartfinal'

# Connect to the database
connection = mysql.connector.connect(host='localhost', user=myPassword, password='', database = myDatabase)
cursor = connection.cursor()

# Enter the table name 
myTable = 'products'

# Define a class for adding the product (selling products/adding to the database created)
class add_product(Tk):
    # Pass arguments to Tk and give multiple arguments
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.title("Harini's Gifts Kart")
        self.minsize(800,600)
        self.iconbitmap('Assets\\surprise.ico')
        self.geometry("800x600")
        # Set the background image  (Photocredit: Unsplash)
        self.backgroundImage = Image.open('Assets\\mostafa-meraji-X0yKdR_F9rM-unsplash.jpg')
        [self.imageSizeWidth, self.imageSizeHeight] = self.backgroundImage.size 
        self.newImageSizeWidth = int(self.imageSizeWidth * 0.25)
    
        if True:
            self.newImageSizeHeight = int(self.imageSizeHeight * 0.25)
        else:
            self.newImageSizeHeight = int(self.imageSizeHeight/0.25)
        
        # Set the provided image as the background
        self.backgroundImage = self.backgroundImage.resize((self.newImageSizeWidth, self.newImageSizeHeight), Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(self.backgroundImage)

        self.backgroundCanvas = Canvas(self)
        self.backgroundCanvas.create_image(300,340,image=self.image)
        self.backgroundCanvas.pack(expand = True, fill = BOTH) 
        '''
        relx and rely = offset horizontally or vertically between 0 and 1

        '''
        # Define the layout using addLayout class    
        def addLayout():
                # Heading for adding products
                self.headingLabel = Label(self, text="ADD PRODUCT", bg='#52fff9', fg='black', font=('Times New Roman',30,'bold'))
                self.headingLabel.place(x=260, y = 100)

                # Frame installed to hold all of the entries
                self.labelFrame = Frame(self,bg='#ff57f4')
                self.labelFrame.place(relx=0.1,rely=0.35,relwidth=0.8,relheight=0.4)
                    
                # Name of the product label annd entry
                self.productName = Label(self.labelFrame,text="PRODUCT NAME: ", bg='#ff57f4', fg='black', font=("Times New Roman", 13,'bold'))
                self.productName.place(relx=0.05,rely=0.2, relheight=0.08)
                    
                self.ProdName = Entry(self.labelFrame)
                self.ProdName.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)
                    
                # Stocks to add label and entry
                self.stocks = Label(self.labelFrame,text="STOCKS TO ADD: ", bg='#ff57f4', fg='black',font=("Times New Roman", 13,'bold'))
                self.stocks.place(relx=0.05,rely=0.35, relheight=0.08)
                    
                self.qty = Entry(self.labelFrame)
                self.qty.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)
                    
                # Cost per product label and entry
                self.costPer = Label(self.labelFrame,text="COST PER PRODUCT: ", bg='#ff57f4', fg='black',font=("Times New Roman", 13,'bold'))
                self.costPer.place(relx=0.02,rely=0.50, relheight=0.08)
                    
                self.Cost = Entry(self.labelFrame)
                self.Cost.place(relx=0.3,rely=0.50, relwidth=0.62, relheight=0.08)
                    
                # Least Qty for trigger Order
                self.thresholdQty = Label(self.labelFrame,text="MIN QTY ALLOWED : ", bg='#ff57f4', fg='black',font=("Times New Roman", 13,'bold'))
                self.thresholdQty.place(relx=0.02,rely=0.65, relheight=0.08)
                    
                self.LeastQty = Entry(self.labelFrame)
                self.LeastQty.place(relx=0.3,rely=0.65, relwidth=0.62, relheight=0.08)
                    
                #Submit Button
                self.SubmitBtn = Button(self,text="SUBMIT",bg='#52fff9', fg='black',font=("Times New Roman", 13),command=addToList)
                self.SubmitBtn.place(relx=0.28,rely=0.8, relwidth=0.2,relheight=0.05)
                
                # Quit button
                self.quitBtn = Button(self,text="QUIT",bg='#52fff9', fg='black', font=("Times New Roman", 13),command=self.destroy)
                self.quitBtn.place(relx=0.53,rely=0.8, relwidth=0.2,relheight=0.05)

# Take the maximum of PID and keep adding it for every product
        def addToList():
                # The first id is 1
                self.id = 1
                try:
                    # Get the maxmum through the SELECT
                    cursor.execute("SELECT Max(PID) from products")
                    # Execute this as the result in all of the rows
                    result = cursor.fetchall()
                    # Treat that initial one as the index 0
                    for r in result:
                        self.id=r[0]
                    # Add one to it to find the new id and convert to str
                    if self.id != 1:
                        self.id = str(int(self.id)+1)

                    # Use self.insertSQL to insert values in the database table
                    self.insertSQL = "insert into "+myTable+" values('"+self.id+"','"+self.ProdName.get()+"','"+self.qty.get()+"','"+self.Cost.get()+"','"+self.LeastQty.get()+"')"
                    cursor.execute(self.insertSQL)
                    connection.commit()
                    messagebox.showinfo('Success',"Product added successfully")
                except:
                    messagebox.showinfo("Error","Can't add data into Database")
                self.destroy()
# This runs the program        
        addLayout()
add_product().mainloop()