# JoesAutomotiveQuotingSystem
A Quoting System for Joe's Automotive

## Entities
### Part
id : Integer <br/>
name : String <br/>
cost : Integer <br/>
laborCost : Integer <br/>
salesTax : Integer <br/>
totalCost : Integer <br/>
carMakeModel : String <br/>
### Car
id : Integer <br/>
make : String <br/>
model : String <br/>
year : String <br/>
parts : List of Part <br/>
### User
id : Integer <br/>
fullName : String <br/>
address : String <br/>
telephone : String <br/>
cars : List of Car <br/>
isManager : Boolean <br/>
isEmployee : Boolean <br/>
isCustomer : Boolean <br/>
canGenerateQuoet : Boolean <br/>
canLookupCustomer : Boolean <br/>
### Quote
id : Integer <br/>
customer : User <br/>







