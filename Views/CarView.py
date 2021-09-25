class CarView:
    def __init__(self,car):
        self.car = car

    def display(self):
        print("Car Information")
        print("ID: ",self.car.id)
        print("Make: ",self.car.make)
        print("Model: ",self.car.model)
        print("Year: ",self.car.year)
        print()
            

