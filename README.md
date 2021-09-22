# JoesAutomotiveQuotingSystem
A Quoting System for Joe's Automotive

## Application Entry Point
### App.py (Located at Root Directory)

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
## Controllers
### Base Controller
Description:  <br/>
A Controller containing functions that are used by all other controllers and serves as RAM fors used objects/entities. <br/><br/>
Parameters: <br/>
path : String <br/>
partId : Integer <br/>
carId : Integer <br/>
quoteId : Integer <br/>
userId : Integer <br/>
users : List of User<br/>
parts : List of Part<br/>
cars : List of Car<br/>
quotes : List of Quote<br/><br/>
Methods: <br/>
generatePartId() : null -> Integer <br/>
generateCarId() : null -> Integer <br/>
generateQuoteId() : null -> Integer <br/>
generateUserId() : null -> Integer <br/><br/>







