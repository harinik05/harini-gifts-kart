#-----------------------------------------------------------------------------
# Name:        Options Menu  (options_menu.py)
# Purpose:     TThis program shows all of the options for the program. This window will always remain
# open in case the person wants to return back to this window. The os library was used
# Author:      Harini Karthik
# Created:     23-Mar-2021
# Updated:     2-April-2021
#-----------------------------------------------------------------------------
'''
#################################################################################
Class Name - mainMenu
Dependencies - n/a
Input - 6 buttons for each file navigation through os
Output - Whenever the button is clicked, it will navigate to a new window that corresponds to one of the program 
features
GUI - Options Menu
Functionality - This program is the main program after the login page for the navigation of pages 
that include add product, update product, inventory reports, configuration, sales reports, and 
cart shopping

Change Control:
-----------------------------------------------------------------------------------------------
23-Mar-2021     Harini Karthik          Initial Program created
26-Mar-2021     Harini Karthik          Use of Os library for navigations
02-Apr-2021     Harini Karthik          Updated the UI design
-----------------------------------------------------------------------------------------------
'''
# Import the required libraries for the program
from tkinter import *
from PIL import ImageTk,Image
import os
py=sys.executable

# Define a class for the main menu
class mainMenu(Tk):
    def __init__(self):
        super().__init__()
        # Define the window layout
        self.title("Harini's Gift Kart")            # Window Title
        self.minsize(800,600)                       # Window size
        self.geometry('800x600')
        # Photocredit: Flaticon
        self.iconbitmap('Assets\\surprise.ico')  # Company logo (must be type ico)

        # Set the background image  (Photocredit: Unsplash)
        self.backgroundImage = Image.open('Assets\\aaron-lee-fN0ZbcCXewM-unsplash.jpg')
        [self.imageSizeWidth, self.imageSizeHeight] = self.backgroundImage.size 
        self.newImageSizeWidth = int(self.imageSizeWidth * 0.25)
    
        if True:
            self.newImageSizeHeight = int(self.imageSizeHeight * 0.25)
        else:
            self.newImageSizeHeight = int(self.imageSizeHeight/0.25)
        
        self.backgroundImage = self.backgroundImage.resize((self.newImageSizeWidth, self.newImageSizeHeight), Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(self.backgroundImage)
        # Create the image and save it as canvas
        self.backgroundCanvas = Canvas(self)
        self.backgroundCanvas.create_image(300,340,image=self.image)
        self.backgroundCanvas.pack(expand = True, fill = BOTH) 
        
        # Define the layout
        def mainPage():
                # Define heading 
                self.headingLabel = Label(self, text="HARINI'S GIFTS KART", bg='#52fff9', fg='black', font=('Times New Roman',30))
                self.headingLabel.place(x=220, y = 100)

                # Upload all of the pictures through PhotoImage
                self.shoppingPic = PhotoImage(file = r"Assets\\shopping-cart.png")
                self.addingPic = PhotoImage(file = r"Assets\\add.png")
                self.updatePic = PhotoImage(file = r"Assets\\updated.png")
                self.inventoryPic = PhotoImage(file = r"Assets\\inventory.png")
                self.salesPic = PhotoImage(file = r"Assets\\business-and-finance.png")
                self.configurePic = PhotoImage(file=f"Assets\\settings.png")

                # Resize the image in order to fit into the button
                self.shoppingPicResize = self.shoppingPic.subsample(6, 6)
                self.addingPicResize = self.addingPic.subsample(6,6)
                self.updatePicResize = self.updatePic.subsample(6,6)
                self.inventoryPicResize = self.inventoryPic.subsample(6,6)
                self.salesPicResize = self.salesPic.subsample(6,6)
                self.configurePicResize = self.configurePic.subsample(6,6)

                # Define the buttons below
                self.shopping = Button(self, text = "     Shopping Cart", font=("Times New Roman", 18),width = 300, command = cart_shopping,image = self.shoppingPicResize,
                    compound = LEFT).place(x=80, y=180)
                self.adding = Button(self, text = "     Add Product", font=("Times New Roman", 18),width = 300, command = add_product,image = self.addingPicResize,
                    compound = LEFT).place(x=420, y=180)
                self.updating = Button(self, text = "     Update Product", font=("Times New Roman", 18),width = 300, command = update_product,image = self.updatePicResize,
                    compound = LEFT).place(x=80, y=300)
                self.inventory = Button(self, text = "   Inventory Reports", font=("Times New Roman", 18),width = 300,command = report_inventory,image = self.inventoryPicResize,
                    compound = LEFT).place(x=420, y=300)
                self.sales = Button(self, text = "     Sales Reports", font=("Times New Roman", 18),width = 300,command = sales_report,image = self.salesPicResize,
                    compound = LEFT).place(x=80, y=420)
                self.configuring = Button(self, text = "     Configure Setting", font=("Times New Roman", 18),width = 300,command =configure_user,image = self.configurePicResize,
                    compound = LEFT).place(x=420, y=420)
                self.endingText = Label(self, text='✨Made by Harini Karthik✨' , bg = '#ff57f4' , fg = 'black', font=("Times New Roman", 12))
                self.endingText.place(x=310, y=530)  
        # Define functions for each of the command to head to the corresponding page
        def cart_shopping():
                os.system('%s %s' % (py,'cart_shopping.py'))
        def add_product():
                os.system('%s %s' % (py,'add_product.py'))
        def update_product():
                os.system('%s %s' % (py,'update_product.py'))
        def report_inventory():
                os.system('%s %s' % (py,'report_inventory.py'))
        def sales_report():
                os.system('%s %s' % (py,'sales_report.py'))
        def configure_user():
                os.system('%s %s' % (py,'configure_users.py'))

# This will run the program

        mainPage()
mainMenu().mainloop()