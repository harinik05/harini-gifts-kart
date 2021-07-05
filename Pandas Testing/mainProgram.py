# Import the required libraries
import PySimpleGUI as sg
import pandas as pd

#Defining Global Constants
FILE_PATH_USERS ="C:\\GitHub\\HaltonSchool\\final-project-awesomebunny155\\user.csv" 
FILE_PATH_INVENTORY = "C:\GitHub\HaltonSchool\final-project-awesomebunny155\inventoryList.csv.xlsx"

# Define a function for the passcodes
def loginInformation(username, password):
    pwd = RetrieveCsvData(FILE_PATH_USERS, "username", username, "pwd")
    if pwd == password:
        print("Login Success!")
    else:
        print("Login Failed")

# Retrieving the CSV Data
def RetrieveCsvData(sFileName, SearchCol, SearchData, RetrieveCol):
    try:
        colList = [SearchCol, RetrieveCol]
        myData = pd.read_csv(sFileName, usecols=colList)
        for i, row in myData.iterrows():
            if row[SearchCol] == SearchData:
                return row[RetrieveCol]
        return ""
    except FileNotFoundError:
        print("The File is not found "+ sFileName)
        return ""
    except KeyError:
        print('The column is not found ')
        return False
    except ValueError:
        print("Incorrect Data used for Col name ")
        return False


# Check Product Qty
def GetProdQty(sIDorDesc, Search):
    #Retrieving the product available Qty from the Inventory  
    if sIDorDesc.lower() == 'id':
        qty = RetrieveCsvData(FILE_PATH_INVENTORY, "Prod_ID", int(Search), "Qty")
    else:
        qty = RetrieveCsvData(FILE_PATH_INVENTORY, "Product_Name", Search, "Qty")
    #if the product is not available, then return 0
    if qty == "":
        return 0
    else:
        return int(qty)


# Check Product Available
def CheckProdAvailable(sIDorDesc, SearchProd, QtyRequired):
    # validate if the product qty is sufficient for the purchase
    nQty = GetProdQty(sIDorDesc, SearchProd)
    if nQty>QtyRequired:
        return True
    else:
        return False


# update Col data in CSV
def UpdateCsvFile(sFileName, SearchCol, SearchData, UpdateCol, UpdateData):
    try:
        #colList = [SearchCol, UpdateCol]
        myData = pd.read_csv(sFileName)
        for i, row in myData.iterrows():
            if row[SearchCol] == SearchData:
                myData.loc[i, UpdateCol] = UpdateData
                myData.to_csv(sFileName, index=False)
                return True
        return False
    except FileNotFoundError:
        print("The file does not exists")
        return False
    except KeyError:
        print('The column is not found ')
        return False
    except ValueError:
        print("Incorrect Data used for Col name ")
        return False


  






    

#loginInformation('admin', 'karthik')
#print(CheckProdAvailable('DESC', "Child Pancake Breakfast", 6))
#print(CheckProdAvailable('id', "4", 2))
print(UpdateCsvFile(FILE_PATH_USERS, 'Product_Name', "Child Pancake Breakfast", "Qty", "3"))