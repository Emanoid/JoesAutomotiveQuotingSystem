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
### Base Controller : BaseController(path:String) -> Access to Methods
Description:  <br/>
A Controller containing functions that are used by all other controllers and serves as RAM for used objects/entities. <br/><br/>

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
generatePartId() -> Integer <br/>
generateCarId() -> Integer <br/>
generateQuoteId() -> Integer <br/>
generateUserId() -> Integer <br/><br/>

### Cars Controller : CarsController(BaseController) -> Access to Methods
Description:  <br/>
A Controller containing functions that can be used by any Car. <br/><br/>

Parameters: <br/>
baseController : BaseController <br/><br/>

Methods: <br/>
createCar(make:String, model:String, year:String) -> Car <br/>
removeCar(make:String, model:String, year:String) -> Void <br/>
removeCarById(carId:Integer) -> Void <br/>
addPart(car:Car, part: Part) -> Void <br/>
addPartById(car:Car, partId:Integer) -> Void <br/>
removePartById(car:Car, partId:Integer) -> Void <br/>
getParts(car:Car) -> List of Part <br/><br/>







