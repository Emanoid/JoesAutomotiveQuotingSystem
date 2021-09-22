class User:
    def __init__(self, id, fullName, address, telephone, cars,isManager, isEmployee, isCustomer,canGenerateQuote,canLookupCustomer):
        self.id = id
        self.fullName = fullName
        self.address = address
        self.telephone = telephone
        self.cars = cars
        self.isManager = isManager
        self.isEmployee = isEmployee
        self.isCustomer = isCustomer
        self.canGenerateQuote = canGenerateQuote
        self.canLookupCustomer = canLookupCustomer

