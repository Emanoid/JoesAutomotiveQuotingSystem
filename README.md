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
carMakeModel : String 

### Car
id : Integer <br/>
make : String <br/>
model : String <br/>
year : String <br/>
parts : List of Part 

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
canLookupCustomer : Boolean 

### Quote
id : Integer <br/>
customer : User 

## Controllers
### Base Controller : BaseController(path:String) -> Access to Methods
Description:  <br/>
A Controller containing functions that are used by all other controllers and serves as RAM for used objects/entities. <br/>

Parameters: <br/>
path : String <br/>
partId : Integer <br/>
carId : Integer <br/>
quoteId : Integer <br/>
userId : Integer <br/>
users : List of User<br/>
parts : List of Part<br/>
cars : List of Car<br/>
quotes : List of Quote<br/>

Methods: <br/>
generatePartId() -> Integer <br/>
generateCarId() -> Integer <br/>
generateQuoteId() -> Integer <br/>
generateUserId() -> Integer 

### Cars Controller : CarsController(BaseController) -> Access to Methods
Description:  <br/>
A Controller containing functions that can be used by any Car. <br/>

Parameters: <br/>
baseController : BaseController <br/>

Methods: <br/>
createCar(make:String, model:String, year:String) -> Car <br/>
removeCar(make:String, model:String, year:String) -> Void <br/>
removeCarById(carId:Integer) -> Void <br/>
addPart(car:Car, part: Part) -> Void <br/>
addPartById(car:Car, partId:Integer) -> Void <br/>
removePartById(car:Car, partId:Integer) -> Void <br/>
getParts(car:Car) -> List of Part 







