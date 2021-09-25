class PartView:
    def __init__(self, part):
        self.part = part

    def display(self):
        print("Part Information:")
        print("ID:",self.part.id)
        print("Name:",self.part.name)
        print("Main Supplier Name:",self.part.mainSupplierName)
        print("Cost: $",self.part.cost)
        print()


