# JoesAutomotiveQuotingSystem
A Quoting System for Joe's Automotive

## Application Entry Point
### App.py (Located at Root Directory)

## Models/Entities
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
removeCar(car:Car) -> Void <br/>
removeCarById(carId:Integer) -> Void <br/>
addPart(car:Car, part: Part) -> Void <br/>
addPartById(car:Car, partId:Integer) -> Void <br/>
removePartById(car:Car, partId:Integer) -> Void <br/>
getParts(car:Car) -> List of Part 

### Parts Controller : PartsController(BaseController) -> Access to Methods
Description:  <br/>
A Controller containing functions that can be used by any Part. <br/>

Parameters: <br/>
baseController : BaseController <br/>

Methods: <br/>
createPart(name:String,cost:Integer,laborCost:Integer,salesTax:Integer,carMakeModel:String) -> Part <br/>
removePart(part:Part) -> Void <br/>
removePartById(partId:Integer) -> Void 

### Quotes Controller : QuotesController(BaseController) -> Access to Methods
Description:  <br/>
A Controller containing functions that can be used by any Quote. <br/>

Parameters: <br/>
baseController : BaseController <br/>

Methods: <br/>
createQuote(customer:Customer) -> Quote <br/>
removeQuote(quote:Quote) -> Void <br/>
removeQuoteById(quoteId:Integer) -> Void 

### Users Controller : UsersController(BaseController) -> Access to Methods
Description:  <br/>
A Controller containing functions that can be used by any User. <br/>

Parameters: <br/>
baseController : BaseController <br/>

Methods: <br/>
createUser(fullName:String,address:String,telephone:String,isManager:Boolean,isEmployee:Boolean,isCustomer:Boolean) -> User <br/>
lookupCustomer(user:User,customerTelephone:String) -> User<br/>
generateQuote(user:User,customerTelephone:String) -> Quote<br/>
printQuote(user:User,customerTelephone:String) -> Quote<br/>
removeUser(user:User) -> Void <br/>
removeUserById(userId:Integer) -> Void <br/>
addCar(user:User,car:Car) -> Void <br/>
removeCar(user:User,car:Car) -> Void <br/>
removeCarById(user:User,carId:Integer) -> Void <br/>
getCars(user:User) -> List of Car <br/>
getCarById(user:User,carId:Integer) -> Car 

## Views
### Car View : CarView(car:Car) -> Access to Methods
Description:  <br/>
A View containing functions that can be view details of any Car. <br/>

Parameters: <br/>
car : Car <br/>

Methods: <br/>
display() -> Terminal View 

### Part View : PartView(part:Part) -> Access to Methods
Description:  <br/>
A View containing functions that can be view details of any Part. <br/>

Parameters: <br/>
part : Part <br/>

Methods: <br/>
display() -> Terminal View 

### User View : PartView(user:User) -> Access to Methods
Description:  <br/>
A View containing functions that can be view details of any User. <br/>

Parameters: <br/>
user : User <br/>

Methods: <br/>
display() -> Terminal View 

### Quote View : QuoteView(quote:Quote) -> Access to Methods
Description:  <br/>
A View containing functions that can be view details of any Quote. <br/>

Parameters: <br/>
quote : Quote <br/>

Methods: <br/>
display() -> Terminal View <br/>
print() -> Terminal View & Writes Quote to txt File and Saves to Root Directory.

