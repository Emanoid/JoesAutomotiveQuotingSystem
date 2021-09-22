class UserView:
    def __init__(self, user):
        self.user = user

    def display(self):
        print("User Information")
        print("User ID: ",self.user.id)
        print("Name: ",self.user.fullName)
        print("Address: ",self.user.address)
        print("Telephone: ",self.user.telephone)
        print("Is Manager: ",self.user.isManager)
        print("Is Employee: ",self.user.isEmployee)
        print("Is Customer: ",self.user.isCustomer)
        print("Owned Car(s):")
        for car in self.user.cars:
            print("Car ID: ",car.id)
            print("Make: ",car.make)
            print("Model: ",car.model)
            print("Year: ",car.year)
            print()
        print()
            


