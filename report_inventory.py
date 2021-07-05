#-----------------------------------------------------------------------------
# Name:        Inventory Reports (report_inventory.py)
# Purpose:     The inventory reports will consist of all of the products that have quantities less
# than the thresholds. Once the quantity is low, an email can be sent to the stakeholders in pdf format
# to update them to purchase the product
# Author:      Harini Karthik
# Created:     30-Mar-2021
# Updated:     2-April-2021
#-----------------------------------------------------------------------------
'''
#################################################################################
Class Name - cart_shopping
Dependencies - DB - products, message box, mailserver
Input - Email address
Output - If the product quantity is less than the threshold, then it will be added to the table. 
This can be emailed as the pdf to the given address
GUI - Report Inventory
Functionality - This program generates a list of products that have quantities below the threshold. 
Then this will be emailed to the given address in pdf format

Change Control:
-----------------------------------------------------------------------------------------------
30-Mar-2021     Harini Karthik          Program Created
02-Apr-2021     Harini Karthik          Email Feature added and UI updated
-----------------------------------------------------------------------------------------------
'''
#  Import the libraries
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
from fpdf import FPDF
# Do pip install wheel before
from pdf_mail import sendpdf 
import smtplib
from pathlib  import Path
PROJECT_ROOT = Path(__file__).parents[0]

# Define environmental constants
mypass = "root"
mydatabase="harinigiftkartfinal"

# Add connection to the database
con = mysql.connector.connect(host='localhost',user=mypass,password='',database=mydatabase)
cur = con.cursor()

# Define a class for the report inventory
class report_inventory(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__()
        # Define the window layout
        self.title("Harini's Gifts Kart")
        self.minsize(800,600)
        self.iconbitmap('Assets\\surprise.ico')
        self.geometry("800x600")

        # Set the background image  (Photocredit: Unsplash)
        self.backgroundImage = Image.open('Assets\\isaac-smith-AT77Q0Njnt0-unsplash.jpg')
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

        # Define a function for the generate reports that has all the UI and captures the details from the database
        def generateInventoryReports():
            # Heading of the window
            self.headingLabel = Label(self, text="GENERATE INVENTORY REPORTS", bg='#52fff9', fg='black', font=('Times New Roman',30,'bold'))
            self.headingLabel.place(x=85, y = 100)
            # Label frame is where all the information is held in
            self.labelFrame = Frame(self,bg='#ff57f4')
            self.labelFrame.place(relx=0.1,rely=0.35,relwidth=0.8,relheight=0.4)
            # All of the table titles are defined in here
            y = 0.25
            # Below declaration is for the pdf report
            self.txt = 'PID,Product,Current Qty,Cost ($)\n'
            self.txt = self.txt + '________________________________________________________\n'

            Label(self.labelFrame, text="%-10s%-40s%-30s%-20s"%('PID','PRODUCT','CURRENT QTY','COST ($)'),bg='#ff57f4',fg='black', font=('Times New Roman',12,'bold')).place(relx=0.07,rely=0.1)
            Label(self.labelFrame, text="------------------------------------------------------------------------------------------------------------",bg='#ff57f4',fg='black').place(relx=0.05,rely=0.2)
            self.getProducts = "SELECT PID, ProductName, Qty, Cost from products WHERE Qty<=Threshold"
            # Get the product details from the database and print in the label frame
            try:
                cur.execute(self.getProducts)
                result = cur.fetchall()
                for i in result:
                    Label(self.labelFrame, text="%-10s%-40s%-30s%-20s"%(i[0],i[1],i[2],i[3]),bg='#ff57f4',fg='black',font=('Times New Roman',12,'bold')).place(relx=0.07,rely=y)
                    self.txt = self.txt+str(i[0])+","+str(i[1])+","+str(i[2])+","+str(i[3])+" \n"
                    y += 0.1
            # Failed to get data if there are issues
            except:
                print(f'{Error} - the error')
                messagebox.showinfo("Failed to get data from database")
            
            #Enter Email
            self.email = Label(self.labelFrame,text="EMAIL REPORT : ", bg='#ff57f4', fg='black', font=('Times New Roman',12,'bold'))
            self.email.place(relx=0.05,rely=0.85, relheight=0.08)
                
            self.Email = Entry(self.labelFrame)
            self.Email.place(relx=0.3,rely=0.85, relwidth=0.62, relheight=0.08)

            #Submit Button
            self.SubmitBtn = Button(self,text="SEND MAIL",bg='#52fff9', fg='black',font=("Times New Roman", 13),command=SendEmail)
            self.SubmitBtn.place(relx=0.28,rely=0.8, relwidth=0.2,relheight=0.05)
                
            self.quitBtn = Button(self,text="QUIT",bg='#52fff9', fg='black', font=("Times New Roman", 13),command=self.destroy)
            self.quitBtn.place(relx=0.53,rely=0.8, relwidth=0.2,relheight=0.05)
        
        # Define a function for generating the pdf and sending the email
        def SendEmail():
            #generate PDF Report
            generate_pdf()
            # Get the information from the database
            self.getUserInfo = "SELECT Email, Pwd, smtp, port from mailserver"

            # Add the entry information into the database
            try:
                cur.execute(self.getUserInfo)
                result = cur.fetchall()
                for r in result:
                   sender_email =r[0]
                   sender_password = r[1]
                   smtp=r[2]
                   port=r[3]

            # If error, then there is error message  
            except:
                print(f'{Error} - the error')
                messagebox.showinfo("Failed to get data from database")
            # Recepient Email
            address_info = self.Email.get()
            
            email_body_info = "The Inventory Report"
            print(address_info,email_body_info)
            
            # Go to manage google account and set as "turn on access for less secure apps"
            server = smtplib.SMTP(smtp,port)
            # conn to smtp server
            server.starttls()
            
            server.login(sender_email,sender_password)
            
            messagebox.showinfo("Success", "Login is Successful!")
            
            emailInformation = sendpdf(sender_email, address_info, sender_password, "Inventory Report", email_body_info, 'report', self.pathPdfNo)
            emailInformation.email_send()
            
            messagebox.showinfo("Success", "Message is sent")
            
           
        # The pdf is generated and placed in the project root
        def generate_pdf():
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            self.tx = str.split(self.txt, '\n')
            for i in self.tx:
                pdf.cell(200, 10, txt=i, ln=1, align="C")
            # Defined two paths- one for the project directory and other with the file (report.pdf)
            self.pathPdfNo = PROJECT_ROOT
            self.pathPdf = PROJECT_ROOT / 'report.pdf'
            pdf.output(self.pathPdf)

# This is used to run the program
        generateInventoryReports()
report_inventory().mainloop()
