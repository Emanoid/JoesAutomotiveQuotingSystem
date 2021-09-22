PATH = input("Enter path to Program's root directory: ")
PATHBACKUP = r"C:\Users\olatunem\OneDrive - Seton Hall University\Bachelors Degree Program\4 Year\4 Yr 1 Sem\Software Engineering\JoesAutomotive"
import sys
sys.path.insert(0,PATHBACKUP)
from Models.Car import *
from Models.Part import *
from Models.Quote import *
from Models.User import *
from Controllers.BaseController import BaseController
from Controllers.UsersController import *
from Controllers.CarsController import *
from Controllers.PartsController import *
from Controllers.QuotesController import *
from Views.CarView import *
from Views.PartView import *
from Views.QuoteView import *
from Views.UserView import *
baseController = BaseController(PATHBACKUP)
##############################################################

####################USABLE OBJECTS####################
#You can add more objects, Reference README
#Users
user1 = UsersController(baseController).createUser("Emmanuel","New York","993-923-0324",True,False,False)
user2 = UsersController(baseController).createUser("Micheal","New York","349-922-0432",False,False,True)
#Parts
hondaWheels = PartsController(baseController).createPart("Wheels",120,50,10,"Honda Civic")
hondaWindShield = PartsController(baseController).createPart("WindShield",500,100,20,"Honda Civic")
hondaBumper = PartsController(baseController).createPart("Bumper",150,40,15,"Honda Civic")
hondaRadiator = PartsController(baseController).createPart("Radiator",300,120,25,"Honda Civic")
bmwWheels = PartsController(baseController).createPart("Wheels",150,70,12,"BMW NextGen")
bmwWindShield = PartsController(baseController).createPart("WindShield",700,100,19,"BMW NextGen")
bmwBumper = PartsController(baseController).createPart("Bumper",200,45,20,"BMW NextGen")
bmwRadiator = PartsController(baseController).createPart("Radiator",500,150,27,"BMW NextGen")
#Cars
honda = CarsController(baseController).createCar("Honda","Civic","2018")
bmw = CarsController(baseController).createCar("BMW","NextGen","2009")
#Adding Parts to Cars
CarsController(baseController).addPart(honda,hondaWheels)
CarsController(baseController).addPart(honda,hondaWindShield)
CarsController(baseController).addPart(honda,hondaBumper)
CarsController(baseController).addPart(honda,hondaRadiator)
CarsController(baseController).addPart(bmw,bmwWheels)
CarsController(baseController).addPart(bmw,bmwWindShield)
CarsController(baseController).addPart(bmw,bmwBumper)
CarsController(baseController).addPart(bmw,bmwRadiator)
#Assigning Cars to Users
UsersController(baseController).addCar(user2, honda)
UsersController(baseController).addCar(user2, bmw)

##############################################################
#Reference README to run functions/tasks on Objects here






##############################################################
#UsersController(baseController).removeCar(user2, honda)

#UsersController(baseController).lookupCustomer(user1,"349-922-0432")
#UsersController(baseController).lookupCustomer(user2,"349-922-0432")

#UsersController(baseController).generateQuote(user1,"349-922-0432")
#UsersController(baseController).generateQuote(user2,"349-922-0432")
#UsersController(baseController).printQuote(user1,"993-923-0324")
# enerateQuote(user2,"349-922-0432")

#print(user1.id)
#print(user2.id)

