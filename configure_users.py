#-----------------------------------------------------------------------------
# Name:        Configure User Information (configure_users.py)
# Purpose:     This program is to change the settings of the user information and email credentials. 
# It asks for 4 vital information: email, password, SMTP, and port. Once those are filled
# they don't need to be changed anymore. The user can just email to the stakeholders and companies
# to purchase the product
# Author:      Harini Karthik
# Created:     1-April-2021
# Updated:     2-April-2021
#-----------------------------------------------------------------------------
'''
#################################################################################
Class Name - configure_users
Dependencies - DB - mailserver, messagebox
Input - Email address, password, SMTP, and Port
Output - The information will be stored in the database table (mailserver) and this can be used for emailing the 
pdf versions of the report inventory 
GUI - Configure Users
Functionality - This program is used for settings of user information stored in the database. This will be 
used for emailing reports

Change Control:
-----------------------------------------------------------------------------------------------
01-Apr-2021     Harini Karthik          Initial Program created
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
con = mysql.connector.connect(host='localhost',user=mypass,password='',database=mydatabase)
cur = con.cursor()

# Enter Table Name here
TableName = "mailserver"

# Define a class for configuring the user information
class configure_users(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__()
        # Define the window layout
        self.title("Harini's Gifts Kart")
        self.minsize(800,600)
        self.iconbitmap('Assets\\surprise.ico')
        self.geometry("800x600")

        # Set the background image  (Photocredit: Unsplash)
        self.backgroundImage = Image.open('Assets\\christian-wiediger-WkfDrhxDMC8-unsplash.jpg')
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

        # Create a class for adding the user
        def addUsers():   
            # Define the heading title       
            self.headingLabel = Label(self, text="CONFIGURE USER INFO", bg='#52fff9', fg='black', font=('Times New Roman',30,'bold'))
            self.headingLabel.place(x=180, y = 100)
            
            # Define the label frame to have all of the entries and labels
            self.labelFrame = Frame(self,bg='#ff57f4')
            self.labelFrame.place(relx=0.1,rely=0.35,relwidth=0.8,relheight=0.4)
                
            # Email
            self.email = Label(self.labelFrame,text="EMAIL: ", bg='#ff57f4', fg='black', font=("Times New Roman", 13,'bold'))
            self.email.place(relx=0.05,rely=0.2, relheight=0.08)
                
            self.Email = Entry(self.labelFrame)
            self.Email.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)
                
            # Password
            self.passkey = Label(self.labelFrame,text="PASSWORD: ", bg='#ff57f4', fg='black',font=("Times New Roman", 13,'bold'))
            self.passkey.place(relx=0.05,rely=0.35, relheight=0.08)
                
            self.Password = Entry(self.labelFrame)
            self.Password.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)
                
            # SMTP
            self.smtpInfo = Label(self.labelFrame,text="    SMTP: ", bg='#ff57f4', fg='black',font=("Times New Roman", 13,'bold'))
            self.smtpInfo.place(relx=0.02,rely=0.50, relheight=0.08)
                
            self.smtp = Entry(self.labelFrame)
            self.smtp.place(relx=0.3,rely=0.50, relwidth=0.62, relheight=0.08)
                
            # PORT
            self.portInfo = Label(self.labelFrame,text="    PORT: ", bg='#ff57f4', fg='black',font=("Times New Roman", 13,'bold'))
            self.portInfo.place(relx=0.02,rely=0.65, relheight=0.08)
                
            self.port = Entry(self.labelFrame)
            self.port.place(relx=0.3,rely=0.65, relwidth=0.62, relheight=0.08)

            #Submit Button
            self.SubmitBtn = Button(self,text="SUBMIT",bg='#52fff9', fg='black',font=("Times New Roman", 13),command=InsertUser)
            self.SubmitBtn.place(relx=0.28,rely=0.8, relwidth=0.2,relheight=0.05)
            
            # Quit button
            self.quitBtn = Button(self,text="QUIT",bg='#52fff9', fg='black', font=("Times New Roman", 13),command=self.destroy)
            self.quitBtn.place(relx=0.53,rely=0.8, relwidth=0.2,relheight=0.05)
            
        # Define a class to insert the user when the submit button is clicked on 
        def InsertUser():
            # Insert into the table all of the entered details
            try:
                
                self.insertSQL = "insert into "+TableName+" values('"+self.Email.get()+"','"+self.Password.get()+"','"+self.smtp.get()+"','"+self.port.get()+"')"
                cur.execute(self.insertSQL)
                con.commit()
                messagebox.showinfo('Success',"user added successfully")
            # Else: error means don't add
            except:
                messagebox.showinfo("Error","Can't add user into Database")


            self.destroy()
# Run the program
        addUsers()
configure_users().mainloop()

