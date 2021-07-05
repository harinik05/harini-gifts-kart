#-----------------------------------------------------------------------------
# Name:        Sales Reports (sales_report.py)
# Purpose:     The sales report will show the amount of money that has been earned 
# in daily, monthly, and yearly basis. 
# Author:      Harini Karthik
# Created:     31-Mar-2021
# Updated:     2-April-2021
#-----------------------------------------------------------------------------
'''
#################################################################################
Class Name - sales_report
Dependencies - DB - transactions,  messagebox, datetime
Input - Buttons
Output - The final amount of the transactions will be added for the provided time frames and displayed in
the label frame
GUI - Sales Report Window
Functionality - This program is meant to show the amount of money that has been earned by 
the business in daily, monthly, and yearly basis

Change Control:
-----------------------------------------------------------------------------------------------
31-Mar-2021     Harini Karthik          Created the sales_report
02-Apr-2021     Harini Karthik          Updated the UI design
-----------------------------------------------------------------------------------------------
'''
# Import the required libraries
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
import datetime
import os
py=sys.executable

# Define the dates for year, month and day
date=datetime.datetime.now().date()
month=datetime.datetime.now().month
year=datetime.datetime.now().year

# Define the database and pass as the environmental constants
mypass = "root"
mydatabase="harinigiftkartfinal"

# Connect to the database
con = mysql.connector.connect(host='localhost',user=mypass,password='',database=mydatabase)
cur = con.cursor()

# Define a class for sales_report
class sales_report(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__()
        # Define the window layout
        self.title("Harini's Gifts Kart")
        self.minsize(width=800,height=600)
        self.iconbitmap('Assets\\surprise.ico')
        self.geometry("800x600")

        # Set the background image  (Photocredit: Unsplash)
        self.backgroundImage = Image.open('Assets\\luke-chesser-JKUTrJ4vK00-unsplash.jpg')
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

        # Define a class for the layouy
        def layout():
            # Define heafing 
            self.headingLabel = Label(self, text="SALES REPORTS", bg='#52fff9', fg='black', font=('Times New Roman',30,'bold'))
            self.headingLabel.place(x=245, y = 100)

            # Define for daily report
            self.dailyReportPic = PhotoImage(file=f"Assets\\calendar.png")
            self.dailyReportPicResize = self.dailyReportPic.subsample(6, 6)
            self.daily = Button(self, text = "     DAILY REPORT", font=("Times New Roman", 18),width = 300, command = dailyReport,image = self.dailyReportPicResize,
                    compound = LEFT).place(x=250, y=180)

            # Define for the monthly report
            self.monthlyReportPic = PhotoImage(file=f"Assets\\next-week.png")
            self.monthlyReportPicResize = self.monthlyReportPic.subsample(6, 6)
            self.month = Button(self, text = "   MONTHLY REPORT", font=("Times New Roman", 18),width = 300, command = monthReport,image = self.monthlyReportPicResize,
                    compound = LEFT).place(x=250, y=295)

            # Define buttons for yearly reports
            self.yearlyReportPic = PhotoImage(file=f"Assets\\year.png")
            self.yearlyReportPicResize = self.yearlyReportPic.subsample(6, 6)
            self.year = Button(self, text = "   ANNUAL REPORT", font=("Times New Roman", 18),width = 300, command = yearReport,image = self.yearlyReportPicResize,
                    compound = LEFT).place(x=250, y=410)


            #Quit Btn
            self.quitBtn = Button(self,text="QUIT",bg='#ff57f4', fg='black', font=("Times New Roman", 13),command=self.destroy)
            self.quitBtn.place(relx=0.4,rely=0.9, relwidth=0.2,relheight=0.05)
        
        # Define a function for the daily report
        def dailyReport():
            # This is the sum of the reports in the current date
            self.SQL1 = "SELECT SUM(Amount) from transactions where InvDate = '"+str(date)+"' GROUP BY InvDate"
            # Show the result in dollars
            try:
                cur.execute(self.SQL1)
                result = cur.fetchall()
                for r in result:
                    self.id="CAD $ "+str(r[0]) 

            # Show error message if there are any issues 
            except:
                print(f'{Error} - the error')
                messagebox.showinfo("Failed to get data from database")            

            # Define the frame and label with the number
            self.headingFrame2 = Frame(self,bg="#ff57f4",bd=5)
            self.headingFrame2.place(relx=0.25,rely=0.65,relwidth=0.5,relheight=0.13)

            self.headingLabel2 = Label(self.headingFrame2, text=self.id, bg='#52fff9', fg='black', font=('Times New Roman',15))
            self.headingLabel2.place(relx=0,rely=0, relwidth=1, relheight=1)

        # Define a function for the monthly report
        def monthReport():
            # Group by month and find the sum
            self.SQL1 = "SELECT SUM(Amount) from transactions where MONTH(InvDate) = '"+str(month)+"' GROUP BY MONTH(InvDate)"
            # Show the message of total amount in dollars
            try:
                cur.execute(self.SQL1)
                result = cur.fetchall()
                for r in result:
                    self.id="CAD $ "+str(r[0])  
            # If there is an issue with the database, there will be an error message
            except:
                print(f'{Error} - the error')
                messagebox.showinfo("Failed to get data from database")            
            # Define a frame and label for displaying the information
            self.headingFrame2 = Frame(self,bg="#ff57f4",bd=5)
            self.headingFrame2.place(relx=0.25,rely=0.65,relwidth=0.5,relheight=0.13)

            self.headingLabel2 = Label(self.headingFrame2, text=self.id, bg='#52fff9', fg='black', font=('Times New Roman',15))
            self.headingLabel2.place(relx=0,rely=0, relwidth=1, relheight=1)

        # Define a function for the annual report
        def yearReport():
            # Grab the details from the transactions and add amounts in a year
            self.SQL1 = "SELECT SUM(Amount) from transactions where YEAR(InvDate) = '"+str(year)+"' GROUP BY YEAR(InvDate)"

            # Display the final amount
            try:
                cur.execute(self.SQL1)
                result = cur.fetchall()
                for r in result:
                    self.id="CAD $ "+str(r[0])  
            except:
                print(f'{Error} - the error')
                messagebox.showinfo("Failed to get data from database")            
            # Define the layout of the final amount display
            self.headingFrame2 = Frame(self,bg="#ff57f4",bd=5)
            self.headingFrame2.place(relx=0.25,rely=0.65,relwidth=0.5,relheight=0.13)

            self.headingLabel2 = Label(self.headingFrame2, text=self.id, bg='#52fff9', fg='black', font=('Times New Roman',15))
            self.headingLabel2.place(relx=0,rely=0, relwidth=1, relheight=1)
      
# This is used to run the program
        layout()


sales_report().mainloop()