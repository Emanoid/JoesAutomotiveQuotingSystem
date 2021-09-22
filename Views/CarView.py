class CarView:
    def __init__(self,car):
        self.car = car

    def display(self):
        print("Car Information")
        print("ID: ",self.car.id)
        print("Make: ",self.car.make)
        print("Model: ",self.car.model)
        print("Year: ",self.car.year)
        print("-----PART(S)-----")
        for part in self.car.parts:
            print("Name: ",part.name)
            print("Cost: $",part.cost)
            print("Labor Cost: $",part.laborCost)
            print("Sales Cost: $",part.salesTax)
            print("Total Cost: $",part.totalCost)
            print("---------------------------------")
        print()
            

