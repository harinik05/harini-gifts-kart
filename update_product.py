#-----------------------------------------------------------------------------
# Name:        Update Product (update_product.py)
# Purpose:     The update product features provides two entries: product id and new quantity. Everything 
# is updated in the products table.
# Author:      Harini Karthik
# Created:     25-Mar-2021
# Updated:     2-April-2021
#-----------------------------------------------------------------------------
'''
#################################################################################
Class Name - update_product
Dependencies - DB - products, messagebox
Input - Product No and Qty
Output - The quantity will be updated in the products table
GUI - Update Product Window
Functionality - This program will use the product no and updated quantity and update the 
stocks on the database

Change Control:
-----------------------------------------------------------------------------------------------
25-Mar-2021     Harini Karthik          Initial Program created
30-Mar-2021     Harini Karthik          Updated Program and fixed errors
02-Apr-2021     Harini Karthik          Updated the UI design
-----------------------------------------------------------------------------------------------
'''
# Import the required libraries for the program
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error 

#Declaring the Environment Constants
mypass = "root"
mydatabase="harinigiftkartfinal"

# Connect to the database
connection = mysql.connector.connect(host='localhost',user=mypass,password='',database=mydatabase)
mycursor = connection.cursor()

# Enter Table Names here
TableName = "products"

# Define a class for the update product
class update_product(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__()
        # Define the window layout
        self.title("Harini's Gifts Kart")
        self.minsize(width=800,height=600)
        self.iconbitmap('Assets\\surprise.ico')
        self.geometry("800x600")

        # Set the background image  (Photocredit: Unsplash)
        self.backgroundImage = Image.open('Assets\\freja-saurbrey-34ux0EA-URA-unsplash.jpg')
        [self.imageSizeWidth, self.imageSizeHeight] = self.backgroundImage.size 
        self.newImageSizeWidth = int(self.imageSizeWidth * 0.25)
    
        if True:
            self.newImageSizeHeight = int(self.imageSizeHeight * 0.25)
        else:
            self.newImageSizeHeight = int(self.imageSizeHeight/0.25)
        
        self.backgroundImage = self.backgroundImage.resize((self.newImageSizeWidth, self.newImageSizeHeight), Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(self.backgroundImage)

        self.backgroundCanvas = Canvas(self)
        self.backgroundCanvas.create_image(300,340,image=self.image)
        self.backgroundCanvas.pack(expand = True, fill = BOTH) 

        # Uodate the product layout
        def UpdateProduct():
            # Heading label and label frame
            self.headingLabel = Label(self, text="UPDATE PRODUCT", bg='#52fff9', fg='black', font=('Times New Roman',30,'bold'))
            self.headingLabel.place(x=260, y = 100)


            self.labelFrame = Frame(self,bg='#ff57f4')
            self.labelFrame.place(relx=0.1,rely=0.35,relwidth=0.8,relheight=0.4)
                
            # Product ID to update
            self.productID = Label(self.labelFrame,text="PRODUCT ID : ", bg='#ff57f4', fg='black',font=('Times New Roman',12,'bold'))
            self.productID.place(relx=0.05,rely=0.3, relheight=0.08)
                
            self.productNo = Entry(self.labelFrame)
            self.productNo.place(relx=0.3,rely=0.3, relwidth=0.62, relheight=0.08)

            # Qty to update
            self.qtyButton = Label(self.labelFrame,text="QUANTITY: ", bg='#ff57f4', fg='black',font=('Times New Roman',12,'bold'))
            self.qtyButton.place(relx=0.05,rely=0.55, relheight=0.08)
                
            self.QTY = Entry(self.labelFrame)
            self.QTY.place(relx=0.3,rely=0.55, relwidth=0.62, relheight=0.08)
            
            #Submit Button
            self.SubmitBtn = Button(self,text="SUBMIT",bg='#52fff9', fg='black',font=("Times New Roman", 13),command=updatestock)
            self.SubmitBtn.place(relx=0.28,rely=0.8, relwidth=0.2,relheight=0.05)
            
            # Quit button
            self.quitBtn = Button(self,text="QUIT",bg='#52fff9', fg='black', font=("Times New Roman", 13),command=self.destroy)
            self.quitBtn.place(relx=0.53,rely=0.8, relwidth=0.2,relheight=0.05)

        # Define a function for the up0dates stock
        def updatestock():
            # Get the quantity and add the stocks 
            try:
                self.updateSQL = "Update "+TableName+ " SET Qty ='"+self.QTY.get()+"' where PID = '"+ self.productNo.get()+"'"
                mycursor.execute(self.updateSQL)
                connection.commit()
                messagebox.showinfo('Success',"Stock updated Successfully")
            except:
                messagebox.showinfo("Please check Product ID")
            
            self.destroy()
# This is used to run the program       
        UpdateProduct()
update_product().mainloop()

