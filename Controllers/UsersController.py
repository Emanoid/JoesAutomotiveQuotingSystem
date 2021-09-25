from Models.User import User
from Views.QuoteView import QuoteView
from Views.UserView import UserView
from Views.CarView import CarView
from Controllers.QuotesController import QuotesController
from Controllers.CarsController import CarsController

class UsersController:
    def __init__(self, baseController):
        self.baseController = baseController
        import sys
        sys.path.insert(0,baseController.path)        

    #To Create a New User
    def createUser(self, firstName,lastName,street,city,state,zip, telephone, isManager, isEmployee, isCustomer):
        userId = self.baseController.generateUserId()
        canGenerateQuote = False
        canLookupCustomer = False
        if(isManager):
            canGenerateQuote = True
            canLookupCustomer = True
        if(isEmployee):
            canGenerateQuote = False
            canLookupCustomer = True
        if(isCustomer):
            canGenerateQuote = False
            canLookupCustomer = False
        cars = []
        newUser = User(userId, firstName, lastName,street,city,state,zip, telephone, cars, isManager, isEmployee, isCustomer, canGenerateQuote, canLookupCustomer)
        self.baseController.users[telephone] = newUser
        return newUser

    #Enables adding a Car to a given Customer 
    def addCustomerCar(self,customer,make,model,year):
        newCar = CarsController(self.baseController).createCar(make,model,year)
        customer.cars.append(newCar)

    #To get a view of all the Cars a Customer has
    def getCustomerCars(self,customer):
        for car in customer.cars:
            CarView(car).display()
    
    #Enables a user to lookup the name address and phone number of a given customer
    def lookupCustomer(self, user, customerTelephone):
        if user.canLookupCustomer:
            if customerTelephone in self.baseController.users:
                UserView(self.baseController.users[customerTelephone]).display()
            else: print("Customer with Telephone",customerTelephone,"not found")
        else:
            print("Customer",user.fullName,"does not have permission to Lookup Customer")

    #Enables a user to generate a Quote for a given customer
    def generateQuote(self, user, customerTelephone, service):
        if user.canGenerateQuote:
            if customerTelephone in self.baseController.users:
                newQuote = QuotesController(self.baseController).createQuote(self.baseController.users[customerTelephone])        
                QuotesController(self.baseController).addService(newQuote,service)
            else: print("Customer with Telephone",customerTelephone,"not found")
        else:
            print("User",user.fullName,"does not have permission to Generate Quote")

    #Enables a user to display a Saved Quote for a given customer
    def displayQuote(self, user, customerTelephone):
        if user.canLookupCustomer:
            if customerTelephone in self.baseController.quotes:
                QuoteView(self.baseController.quotes[customerTelephone]).display()     
            else: print("Customer with Telephone",customerTelephone,"has no Quote")   
        else:
            print("User",user.fullName,"does not have permission to Display Quote")

    #Enables a user to display & print a Saved Quote for a given customer
    def printQuote(self, user, customerTelephone):
        if user.canLookupCustomer:
            if customerTelephone in self.baseController.quotes:
                QuoteView(self.baseController.quotes[customerTelephone]).displayAll() 
                QuoteView(self.baseController.quotes[customerTelephone]).print()  
            else: print("Customer with Telephone",customerTelephone,"not found")        
        else:
            print("User",user.fullName,"does not have permission to Print Quote")

    #Enables a user to remove a user with user telephone
    def removeUser(self, user, userTelephone):
        if user.canGenerateQuote:
            if userTelephone in self.baseController.users:
                self.baseController.users.pop(userTelephone)    
            else: print("Customer with Telephone",userTelephone,"not found")    
        else:
            print("User",user.fullName,"does not have permission to Remove User")







    


