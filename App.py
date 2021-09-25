#PATH = input("Enter path to Program's root directory: ")
PATHBACKUP = r"C:\Users\olatunem\OneDrive - Seton Hall University\Bachelors Degree Program\4 Year\4 Yr 1 Sem\Software Engineering\JoesAutomotive"
import sys
sys.path.insert(0,PATHBACKUP)
from Models.Car import *
from Models.Part import *
from Models.Service import *
from Models.Quote import *
from Models.User import *
from Controllers.BaseController import BaseController
from Controllers.UsersController import *
from Controllers.CarsController import *
from Controllers.PartsController import *
from Controllers.ServicesController import *
from Controllers.QuotesController import *
from Views.CarView import *
from Views.PartView import *
from Views.ServiceView import *
from Views.QuoteView import *
from Views.UserView import *
baseController = BaseController(PATHBACKUP)
##############################################################

####################USABLE OBJECTS####################
#You can add more objects, Reference README
#Managers
managerJohn = UsersController(baseController).createUser("John","Charles","NA","NA","NA","NA","973-221-2300",True,False,False)
managerDavid = UsersController(baseController).createUser("David","Mathers","NA","NA","NA","NA","973-435-9856",True,False,False)
#Customers
customerZack = UsersController(baseController).createUser("Zachary","Hite","98 Pyongyang Boulevard","South Orange","NJ","07079","908-234-908",False,False,True)
customerRichard = UsersController(baseController).createUser("Richard","McCrary","913 Coacalco de Berriozbal Loop","Arlington","NJ","08108","856-123-8976",False,False,True)
customerDiana = UsersController(baseController).createUser("Diana","Alexander","1308 Arecibo Way","Augusta-Richmond County","NJ","08043","646-212-9645",False,False,True)
customerScott = UsersController(baseController).createUser("Scott","Shelley","587 Benguela Manor","Aurora","NJ","07050","646-254-6754",False,False,True)
customerClinton = UsersController(baseController).createUser("Clinton","Buford","43 Vilnius Manor","Aurora","NJ","07050","973-543-8967",False,False,True)
customerWilma = UsersController(baseController).createUser("Wilma","Richards","660 Jedda Boulevard","Bellevue","NJ","07042","973-678-0934",False,False,True)
customerValarie = UsersController(baseController).createUser("Valarie","Black","782 Mosul Street","Brockton","NJ","07043","973-258-0674",False,False,True)
customerKarl = UsersController(baseController).createUser("Karl","Seal","1427 Tabuk Place","Cape Coral","NJ","08102","215-347-7129",False,False,True)
#Add Cars to Customer
UsersController(baseController).addCustomerCar(customerZack,"BWM","325","2015")
UsersController(baseController).addCustomerCar(customerRichard,"Mercedes","CL500","2013")
UsersController(baseController).addCustomerCar(customerDiana,"BWM","X5","2016")
UsersController(baseController).addCustomerCar(customerScott,"Mercedes","C350","2018")
UsersController(baseController).addCustomerCar(customerClinton,"Porche","Cayene","2020")
UsersController(baseController).addCustomerCar(customerWilma,"Porche","Cayene","2017")
UsersController(baseController).addCustomerCar(customerValarie,"BWM","325","2014")
UsersController(baseController).addCustomerCar(customerKarl,"Mercedes","M500","2019")
#Parts
brakeLining = PartsController(baseController).createPart("Brake Lining","General Supplies Ltd",100)
offSideMirror = PartsController(baseController).createPart("Off-Side Mirror","General Supplies Ltd",150)
rearViewMirror = PartsController(baseController).createPart("Rear-View Mirror","General Supplies Ltd",200)
tire = PartsController(baseController).createPart("Continental 2055 Tire","Continental Tires",400)
brakePad = PartsController(baseController).createPart("Break Pad","General Supplies Ltd",150)
#Services
liningReplacement = ServicesController(baseController).createService("Lining Replacement","Brake Lining Replacement",300)
mirrorReplacement = ServicesController(baseController).createService("Mirror Replacement","Mirror Replacement",200)
tireRepair = ServicesController(baseController).createService("Tire Repair","Tire Repair",150)
tireReplacement = ServicesController(baseController).createService("Tire Replacement","Tire Replacement",200)
#Mapping Services to Appropriate Parts
ServicesController(baseController).addPart(liningReplacement,brakeLining)
ServicesController(baseController).addPart(mirrorReplacement,offSideMirror)
ServicesController(baseController).addPart(mirrorReplacement,rearViewMirror)
ServicesController(baseController).addPart(tireRepair,tire)
ServicesController(baseController).addPart(tireRepair,brakePad)
ServicesController(baseController).addPart(tireReplacement,tire)
ServicesController(baseController).addPart(tireReplacement,brakePad)
#Have Managers Create some Quote for Customers and add requested services
UsersController(baseController).generateQuote(managerJohn,"908-234-908",liningReplacement)
UsersController(baseController).generateQuote(managerDavid,"856-123-8976",mirrorReplacement)
UsersController(baseController).generateQuote(managerDavid,"973-543-8967",tireRepair)
UsersController(baseController).generateQuote(managerJohn,"973-678-0934",tireReplacement)
##############################################################
#Reference README to run functions/tasks on Objects here

##To Test Customer Search
#*Only Managers and Employees can Lookup Customers, Customers can't lookup Customers
#UsersController(baseController).lookupCustomer(managerJohn,"646-254-6754") 
#UsersController(baseController).lookupCustomer(managerDavid,"215-347-7129") 
#UsersController(baseController).lookupCustomer(customerKarl,"856-123-8976")

##To Test Quote Search
#*Only Managers and Employees can search for Quotes, Customers can't lookup Customers
#UsersController(baseController).displayQuote(managerJohn,"973-543-8967")
#UsersController(baseController).displayQuote(managerDavid,"856-123-8976")
#UsersController(baseController).displayQuote(customerValarie,"856-123-8976")

##To Test Quote Print
#*Only Managers and Employees can Print Quotes, Customers can't lookup Customers
#UsersController(baseController).printQuote(managerJohn,"973-543-8967")
#UsersController(baseController).printQuote(managerDavid,"856-123-8976")
#UsersController(baseController).printQuote(customerValarie,"856-123-8976")

















#------------OTHER UNREALTED TESTS---------------------------------------------
#####Users Controller Tests
#To test getCustomerCars
#UsersController(baseController).getCustomerCars(customerKarl)

#To test removeUser [Richard]
#UsersController(baseController).removeUser(managerDavid,"856-123-8976")
#UsersController(baseController).removeUser(customerClinton,"856-123-8976")
#for user in baseController.users.values():
#    UserView(user).displayAll()

##########################################################
#####Quotes Controller Tests
##To Test Finding & Viewing Quote [all quotes created]
#QuoteView(QuotesController(baseController).getQuote("908-234-908")).display()
#QuoteView(QuotesController(baseController).getQuote("856-123-8976")).display()
#QuoteView(QuotesController(baseController).getQuote("973-678-0934")).display()
#QuoteView(QuotesController(baseController).getQuote("973-678-0934")).display()

##To test removeQuote
#QuoteView(QuotesController(baseController).getQuote("973-678-0934")).display()
#QuotesController(baseController).removeQuote("973-678-0934")
#QuotesController(baseController).getQuote("973-678-0934")

##########################################################
#####Services Controller Test
#To test getService and removeService
#ServicesController(baseController).getService("Mirror Replacement")
#ServicesController(baseController).removeService("Mirror Replacement")
#ServicesController(baseController).getService("Mirror Replacement")

#To test getServices
#ServicesController(baseController).getServices()

##########################################################
#####Parts Controller Test
#To test getPartCost
#PartsController(baseController).getPartCost("Rear-View Mirror","General Supplies Ltd")

#To test getParts & removePart
#PartsController(baseController).getParts()
#PartsController(baseController).removePart("Rear-View Mirror","General Supplies Ltd")
#print("############################")
#PartsController(baseController).getParts()
##############################################################
#####Cars Controller Test
#To test getCars
#CarsController(baseController).getCars()