class PartView:
    def __init__(self, part):
        self.part = part

    def display(self):
        print("Part Information:")
        print("ID:",self.part.id)
        print("Name:",self.part.name)
        print("Cost: $",self.part.cost)
        print("Labor Cost: $",self.part.laborCost)
        print("Sales Cost: $",self.part.salesTax)
        print("Total Cost: $",self.part.totalCost)
        print("Car Make & Model:",self.part.carMakeModel)
        print()


