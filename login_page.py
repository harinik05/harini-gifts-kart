#-----------------------------------------------------------------------------
# Name:        Main Program  (login_page.py)
# Purpose:     This program is the login program wherin the user name and pass word
# purpose: The login is implemented for authentication purpose to allow only the employees of the organization. The validations is 
# performed through the user inputs (username and pwd) against the database configuration.
# input has to match the ones in the database to enter into the main menu (options_menu.py). 
# Author:      Harini Karthik
# Created:     22-Mar-2021
# Updated:     2-April-2021
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
'''
#################################################################################
Class Name - Login
Dependencies - DB - LoginDetails, OptionsMenu
Input - UserName, Password
Output - Navigation to OptionsMenu
GUI - Login Window
Functionality - The Program loads the Login page requesting for the User Inputs. Based on the User Inputs, the program validates
authenticity against the DB. The program allows to navigate to the Options Menu only through successful authentication

Change Control:
-----------------------------------------------------------------------------------------------
22-Mar-2021     Harini Karthik          Initial Program created
28-Mar-2021     Harini Karthik          Integrated DB
02-Apr-2021     Harini Karthik          Updated the UI design
-----------------------------------------------------------------------------------------------
'''
'''
Import the libraries and packages
* means all of the classes
Image Tk and Image are specific classes
Error is for displaying any connectivity issues
os is operating system and py=sys.executable is for executing the os
'''
# STEP 1: Import the required libraries for the program
from tkinter import *           # Import Tkinter library
from PIL import ImageTk, Image  # Import pillow library for displaying images
from tkinter import messagebox  # Import messagebox from tkinter 
import mysql.connector          # Import mysql.connector
from mysql.connector import Error
import os                       # Import os for transitioning to the next window

# STEP 2: Define a variable for py for the os library (use later)
py=sys.executable

'''
Define a class for login wherin it inherits the widgets from Tkinter class
super().__init__() is to establish the inheritance
Define a constructor and self just states that all of the variables are part of the class
self.userName and password is defined as type StringVar()
screen settings defined with the dimensions and the asset for icon bitmap has to be ico
'''
 
# STEP 2: Define a class to execute the functions of the login program
class login(Tk):
    # STEP 3: Initiate a function that can hold the variables for the username and password and overall layout of the screen
    def __init__(self):
        super().__init__()
        self.userName = StringVar()                 # Define a variable for username with stringvar type
        self.passWord = StringVar()                 # Define a variable for password with stringvar type
        self.title("Harini's Gift Kart")            # Window Title
        self.minsize(800,600)                       # Window size
        self.geometry('800x600')
        # Photocredit: Flaticon
        self.iconbitmap('Assets\\surprise.ico')  # Company logo (must be type ico)

        '''
        Open the image and collect the dimensions 
        Resize the width by enlarging it by 0.25
        If this resizes to the width, then it will automatically shrink the width and then go to if true 
        it will resize to the height as well to fit into the background
        if not it will enlarge
        it will be layed out as high quality downsamplinf filer
        Adding the image as background through tkinter and use of Canvas
        Create a small pic and then enlarge it on both ends
        '''

        # Set the background image  (Photocredit: Unsplash)
        self.backgroundImage = Image.open('Assets\\mel-poole-dsTVwp376kc-unsplash.jpg')
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
        #self.backgroundCanvas.config(bg='white', width = self.newImageSizeWidth, height = self.newImageSizeHeight)
        self.backgroundCanvas.pack(expand = True, fill = BOTH) 

        '''
        - Procedures or subroutines that has no return
        layout defined
        entry boxes saved in the text variables string vars
        '''              
        
        # STEP 4: Define the login screen UI
        def userLoginScreen():
                    # Define heading label and location
                    self.heading = Label(self,text="WELCOME TO HARINI'S GIFTS KART", bg = '#52fff9',fg='black',font=("Times New Roman", 30, 'bold'))
                    self.heading.place(x=36, y=120)

                    # Define title of the window
                    self.title = Label(self, text="Administration Login", bg = '#ff57f4' , fg = 'black', font=("Times New Roman", 24,'italic'))
                    self.title.place(x=270, y=200)

                    # Define the username entry and label
                    self.usernameText = Label(self, text="Enter your username:" , bg = '#52fff9' , fg = 'black', font=("Times New Roman", 18, 'bold'))
                    self.usernameText.place(x=95, y=280)
                    self.enterUsernameText = Entry(self, textvariable=self.userName, width=45)
                    self.enterUsernameText.place(x=350, y=287)

                    # Define the password entry and label
                    self.passwordText = Label(self, text="Enter your password:" , bg = '#52fff9' , fg = 'black', font=("Times New Roman", 18, 'bold'))
                    self.passwordText.place(x=95, y=350)
                    self.enterPasswordText = Entry(self, show='*', textvariable=self.passWord, width=45)
                    self.enterPasswordText.place(x=350, y=357)

                    # Click on the enter button to login and this will go to the verification command
                    self.enterButton = Button(self, text="Login",font=("Times New Roman", 18, 'bold'),bg ='#ff57f4', fg = 'black',width=8, command=verification)
                    self.enterButton.place(x=350, y=420)
                    self.endingText = Label(self, text='✨Made by Harini Karthik✨' , bg = '#52fff9' , fg = 'black', font=("Times New Roman", 12))
                    self.endingText.place(x=310, y=530)
                    
        '''
        subroutines
        if there is nothing in the username or password it will say invalid login
        or else it will connect to the database
        Host: Machine in which the program is running
        Database name and root is the super user (first user) that will have access to everything
        No password
        It will connect and grapb th user and password from the entry
        It will get username and password from the table login details. If that matches the entry, then success
        or error
        if connection is an issue then there will be a error message that prints out
        '''
        # Define the verification process (see the code written for the previous program)
        def verification():
            # If the login doesn't match, then it will say that it is invalid
            if len(self.userName.get()) == 0: 
                messagebox.showinfo("Your login is invalid. Please try again")
            elif len(self.passWord.get()) == 0:
                messagebox.showinfo("Your login is invalid. Please try again")
            else:
                # Connect to the database and grab and user details
                try:
                    connection = mysql.connector.connect(host='localhost',
                                         database='harinigiftkartfinal',
                                         user= 'root',
                                         password= '')
                    cursor = connection.cursor()
                    user = self.userName.get()
                    password = self.passWord.get()
                    cursor.execute("SELECT * FROM logindetails WHERE UserName= %s AND PWD= %s",[user,password])
                    pc = cursor.fetchone()
                    # If everything is correct and submit button is clicked, go to the options menu
                    if pc:
                        self.destroy()
                        os.system('%s %s' % (py,'options_menu.py'))
                    # If it is not correct, login is incorrect messagebox is shown
                    else:
                        print(pc)
                        messagebox.showinfo('Error', 'Your login is invalid. Please try again.')
                except Error:
                    messagebox.showinfo('Error',f"{Error} /n Your login is invalid. Please try again.")
#This runs the program                   
        userLoginScreen()
login().mainloop()

