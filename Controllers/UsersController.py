from Models.User import User
from Views.QuoteView import QuoteView
from Views.UserView import UserView
from Views.CarView import CarView
from Controllers.QuotesController import QuotesController

class UsersController:
    def __init__(self, baseController):
        self.baseController = baseController
        import sys
        sys.path.insert(0,baseController.path)        

    def createUser(self, fullName, address, telephone, isManager, isEmployee, isCustomer):
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
        newUser = User(userId, fullName, address, telephone, cars, isManager, isEmployee, isCustomer, canGenerateQuote, canLookupCustomer)
        self.baseController.users.append(newUser)
        return newUser

    def lookupCustomer(self, user, customerTelephone):
        if user.canLookupCustomer:
            for customer in self.baseController.users:
                if customer.telephone == customerTelephone:
                    UserView(customer).display()
                    return customer
            print("Customer not found")
        else:
            print("User",user.fullName,"does not have permission to Lookup Customer")

    def generateQuote(self, user, customerTelephone):
        if user.canGenerateQuote:
            for customer in self.baseController.users:
                if customer.telephone == customerTelephone:
                    newQuote = QuotesController(self.baseController).createQuote(customer)
                    QuoteView(newQuote).display()
                    return newQuote
            print("Customer not found")            
        else:
            print("User",user.fullName,"does not have permission to Generate Quote")

    def printQuote(self, user, customerTelephone):
        newQuote = self.generateQuote(user,customerTelephone)
        if newQuote is not None:
            QuoteView(newQuote).print()

    def removeUser(self, user):
        if user in self.baseController.users:
            self.baseController.users.remove(user)
        else:
            print("User",user,"not found")

    def removeUserById(self, userId):
        for user in self.baseController.users:
            if user.id == userId:
                self.baseController.users.remove(user)
                return
        print("User",user,"not found")

    def addCar(self, user, car):
        user.cars.append(car)

    def removeCar(self, user, car):
        user.cars.remove(car)

    def removeCarById(self, user, carId):
        for car in user.cars:
            if carId == car.id:
                user.cars.remove(car)
                return
        print("Car Id",carId,"not found")

    def getCars(self, user):
        for car in user.cars:
            CarView(car).display()
        return user.cars

    def getCarsById(self, user, carId):
        for car in user.cars:
            if carId == car.id:
                CarView(car).display()
                return car
        print("Car Id",carId,"not found")






    


