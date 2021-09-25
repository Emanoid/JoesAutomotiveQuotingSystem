from Views.CarView import CarView


class UserView:
    def __init__(self, user):
        self.user = user

    def display(self):
        print("User Information:")
        print("Name: ",self.user.fullName)
        print("Address: ",self.user.address)
        print("Phone Number: ",self.user.telephone)
        print()

    def displayAll(self):
        print("User Information")
        print("User ID: ",self.user.id)
        print("Name: ",self.user.fullName)
        print("Address: ",self.user.address)
        print("Phone Number: ",self.user.telephone)
        if(self.user.isManager):
            print("Role: Manager")
        if(self.user.isEmployee):
            print("Role: Employee")
        if(self.user.isCustomer):
            print("Role: Customer")
        print("Owned Car(s):")
        for car in self.user.cars:
            CarView(car).display()
        print()
            


