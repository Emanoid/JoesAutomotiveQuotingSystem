# JoesAutomotiveQuotingSystem
A Quoting System for Joe's Automotive

## Application Entry Point
### App.py (Located at Root Directory)
Will request a directory path, enter your local Application's root directory. <br/>
If program crashes?<br/>
Manually enter path into the "PATHBACKUP" variable and substitute "PATH" with "PATHBACKUP" wherever "PATH" appears.</br>
This should resolve the issue.
<br/><br/>
Objects have already been created for Testing. And all tests have been ran and passed.

## Models/Entities
### Part
id : Integer <br/>
name : String <br/>
mainSupplierName: String <br/>
cost : Integer <br/>

### Service
id : Integer <br/>
name : String <br/>
description: String <br/>
laborCost : Integer <br/>
parts : List of Parts

### Car
id : Integer <br/>
make : String <br/>
model : String <br/>
year : String 

### User
id : Integer <br/>
firstName : String <br/>
lastName : String <br/>
fullName : String <br/>
street : String<br/>
city : String <br/>
state : String <br/>
zip : String <br/> 
address : String <br/>
telephone : String <br/>
cars : List of Cars <br/>
isManager : Boolean <br/>
isEmployee : Boolean <br/>
isCustomer : Boolean <br/>
canGenerateQuote : Boolean <br/>
canLookupCustomer : Boolean 

### Quote
id : Integer <br/>
customer : User  <br/>
services : List of Services

## Controllers
### Base Controller : BaseController(path:String) -> Access to Methods
Description:  <br/>
A Controller containing functions that are used by all other controllers and serves as RAM for used objects/entities. <br/>

Parameters: <br/>
path : String <br/>
partId : Integer <br/>
serviceId : Integer <br/>
carId : Integer <br/>
quoteId : Integer <br/>
userId : Integer <br/>
users : Dictionary of Users<br/>
parts : Dictionary of Parts<br/>
cars : Dictionary of Cars<br/>
quotes : Dictionary of Quotes<br/>

Methods: <br/>
generatePartId() -> Integer <br/>
generateServiceId() -> Integer <br/>
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
getCars() -> Terminal view of all cars <br/>

### Parts Controller : PartsController(BaseController) -> Access to Methods
Description:  <br/>
A Controller containing functions that can be used by any Part. <br/>

Parameters: <br/>
baseController : BaseController <br/>

Methods: <br/>
createPart(name:String,mainSupplierName:String,cost:Integer) -> Part <br/>
getPartCost(name:String,mainSupplierName:String) -> Integer <br/>
getParts() -> Terminal view of all parts <br/>
removePart(name:String,mainSupplierName:String) -> Void <br/>


### Service Controller : ServicesController(BaseController) -> Access to Methods
Description:  <br/>
A Controller containing functions that can be used by any Service. <br/>

Parameters: <br/>
baseController : BaseController <br/>

Methods: <br/>
createService(name:String,description:String,laborCost:Integer) -> Service <br/>
getService(serviceName:String) -> Service & Terminal View of Service <br/>
getServices() -> Terminal View of Services <br/> 
removeService(serviceName:String) -> Void <br/>
addPart(service:Service,part:Part) -> Void <br/>
removePart(service:Service,part:Part) -> Void

### Quotes Controller : QuotesController(BaseController) -> Access to Methods
Description:  <br/>
A Controller containing functions that can be used by any Quote. <br/>

Parameters: <br/>
baseController : BaseController <br/>

Methods: <br/>
createQuote(customer:Customer) -> Quote <br/>
addService(quote:Quote,service:Service) -> Void <br/>
getQuote(customerTelephone:String) -> Quote <br/>
getQuotes() -> ListOfQuotes <br/>
removeQuote(customerTelephone:String) -> Void <br/>

### Users Controller : UsersController(BaseController) -> Access to Methods
Description:  <br/>
A Controller containing functions that can be used by any User. <br/>

Parameters: <br/>
baseController : BaseController <br/>

Methods: <br/>
---Customer Methods---<br/>
addCustomerCar(customer:User,make:String,model:String,year:String) -> Void <br/>
getCustomerCars(customer:User) -> Terminal View of Cars <br/><br/>
---Manager/Employee Methods---<br/>
createUser(user:User,firstName:String,lastName:String,street:String,city:String,state:String,zip:String,telephone:String,isManager:Boolean,isEmployee:Boolean,isCustomer:Boolean) -> User <br/>
lookupCustomer(user:User,customerTelephone:String) -> User & Terminal View of User<br/>
generateQuote(user:User,customerTelephone:String,service:Service) -> Void<br/>
displayQuote(user:User,customerTelephone:String) -> Terminal View of Quote <br/>
printQuote(user:User,customerTelephone:String) -> Terminal View of Quote, and writes Quote to text file in root directory <br/>
removeUser(user:User,userTelephone:String) -> Terminal View of User <br/>

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

### Service View : ServiceView(service:Service) -> Access to Methods
Description:  <br/>
A View containing functions that can be view details of any Service. <br/>

Parameters: <br/>
service : Service <br/>

Methods: <br/>
display() -> Terminal View 

### User View : PartView(user:User) -> Access to Methods
Description:  <br/>
A View containing functions that can be view details of any User. <br/>

Parameters: <br/>
user : User <br/>

Methods: <br/>
display() -> Terminal View
displayAll() -> Terminal View 

### Quote View : QuoteView(quote:Quote) -> Access to Methods
Description:  <br/>
A View containing functions that can be view details of any Quote. <br/>

Parameters: <br/>
quote : Quote <br/>

Methods: <br/>
display() -> Terminal View <br/>
print() -> Terminal View & Writes Quote to text File and Saves to Root Directory.

