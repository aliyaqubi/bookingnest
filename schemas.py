from pydantic import BaseModel
from typing import List

##   Customer  ===============================================================================

##>>> BookNest: class for the [ArticleC] inside the CustomerDisplay (what goes into CustomerDisplay)
##>>> This construction is not what we send or receive from user when we create the article.
class ArticleC(BaseModel):
    title: str
    content: str
    published: bool
    class Config():
        orm_mode = True   

##>>> BookNest: class for the 'customer' inside the ArticleCDisplay (what goes into ArticleCDisplay)
class Customer(BaseModel):
    id: int
    username: str
    class Config():
        orm_mode = True   


##>>> BookNest: Class for data that comes from customer
class CustomerBase(BaseModel):
    firstname: str
    secondname: str
    username: str
    password: str
    email: str
    phone: str   # ???
    adress: str
    nationality: str
    age: int

##>>> BookNest: Class for data-display that the system send back to customer
class CustomerDisplay(BaseModel):
    firstname: str
    secondname: str
    username: str
    email: str
    phone: str   # ???
    adress: str
    nationality: str
    age: int
    items: list[ArticleC] = []  ##>>> ArticleC in here goes back to class: ArticleC
    class Config():
        orm_mode = True

#================================ADMIN=============================================
##>>> BookNest: class for the 'admin' 
class admin(BaseModel):
    id: int
    username: str
    class Config():
        orm_mode = True   


##>>> BookNest: Class for data that comes from admin
class adminBase(BaseModel):
    firstname: str
    secondname: str
    username: str
    password: str
    email: str
    phone: str   # ???
    adress: str
    nationality: str
    age: int

##>>> BookNest: Class for data-display that the system send back to admin
class adminDisplay(BaseModel):
    firstname: str
    secondname: str
    username: str
    email: str
    phone: str   # ???
    adress: str
    nationality: str
    age: int
    class Config():
        orm_mode = True
#=============================================================================================


##>>> BookNest: Class for Article that comes from customer 
class ArticleCBase(BaseModel):
    title: str
    content: str
    published: bool
    creator_id_c: int


##>>> BookNest: Class for Article that system send back to customer (structure of data-display)
class ArticleCDisplay(BaseModel):
    title: str
    content: str
    published: bool
    customer: Customer            ##>>> customer in here goes back to class: Customer
    class Config():
        orm_mode = True


##   Hotel  ===============================================================================

##>>> BookNest: class for the [ArticleH] inside the HotelDisplay (what goes into HotelDisplay)
class ArticleH(BaseModel):
    title: str
    content: str
    published: bool
    class Config():
        orm_mode = True   

##>>> BookNest: class for the 'hotel' inside the ArticleHDisplay (what goes into ArticleCDisplay)
class Hotel(BaseModel):
    id: int
    username: str
    class Config():
        orm_mode = True   



##>>> BookNest: Class for data that comes from hotel
class HotelBase(BaseModel):
    name: str
    manager: str
    username: str
    password: str
    email: str
    phone: str   # ???
    adress: str
    country: str
    city: str
    rooms: int
    star: int

##>>> BookNest: Class for data-display that the system send back to hotel
class HotelDisplay(BaseModel):
    name: str
    manager: str 
    username: str
    email: str
    phone: str   # ???
    adress: str
    country: str
    city: str
    rooms: int
    star: int
    items: list[ArticleH] = []  ##>>> ArticleH in here goes back to class: ArticleH
    class Config():
        orm_mode = True 


##>>> BookNest: Class for Article that comes from hotel 
class ArticleHBase(BaseModel):
    title: str
    content: str
    published: bool
    creator_id_h: int


##>>> BookNest: Class for Article that system send back to hotel (structure of data-display)
class ArticleHDisplay(BaseModel):
    title: str
    content: str
    published: bool
    hotel: Hotel            ##>>> hotel in here goes back to class: Customer
    class Config():
        orm_mode = True
























##   User  ===============================================================================

##>>>Whatis: class for the Article inside the UserDisplay (in definition of items)
##>>> This construction is not what we send or receive from user when we create the article.
##>>> This is just what goes into the UserDisplay. 
# class Article(BaseModel):
#     title: str
#     content: str
#     published: bool
#     #>>> ForWhat: because we do displaying, then we need this configuration of orm_mode
#     class Config():
#         orm_mode = True   

##>>>Whatis: class for the User inside the ArticleDisplay 
##>>> This construction is not what we send or receive from user when we create the article.
##>>> This is just what goes into the ArticleDisplay. 
# class User(BaseModel):
#     id: int
#     username: str
#     ##>>> ForWhat: because we do displaying, then we need this configuration of orm_mode
#     class Config():
#         orm_mode = True   
  


##>>> Whatis: Class for data that comes from user (received from user)
# class UserBase(BaseModel):
#     username: str
#     password: str
#     email: str
    

##>>> Whatis: Class for data that the system send back to user (provided to user)
##>>> ForWhat: to display in responce body just username & email, and not pwd & id
# class UserDisplay(BaseModel):
#     username: str
#     email: str
#     items: list[Article] = []  ##>>> Article in here goes back to class: Article
#     class Config():
#         orm_mode = True      ##>>> ForWhat: to allow the system to return database' data 
#                              ##>>> into the format that provide in this upper class.


##>>> Whatis: Class for Article that comes from user 
# class ArticleBase(BaseModel):
#     title: str
#     content: str
#     published: bool
#     creator_id: int


##>>> Whatis: Class for Article that system send back to user (structure of data when we retreive the article)
# class ArticleDisplay(BaseModel):
#     title: str
#     content: str
#     published: bool
#     user: User            ##>>> User in here goes back to class: User
#     class Config():
#         orm_mode = True

                             