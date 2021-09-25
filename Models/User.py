class User:
    def __init__(self, id, firstName,lastName, street, city, state, zip, telephone, cars, isManager, isEmployee, isCustomer,canGenerateQuote,canLookupCustomer):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.fullName = firstName+" "+lastName
        self.street = street
        self.city = city
        self.state = state
        self.zip = zip
        self.address = street+", "+city+", "+state+", "+zip+"."
        self.telephone = telephone
        self.cars = cars
        self.isManager = isManager
        self.isEmployee = isEmployee
        self.isCustomer = isCustomer
        self.canGenerateQuote = canGenerateQuote
        self.canLookupCustomer = canLookupCustomer

