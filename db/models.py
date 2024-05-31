from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, Boolean
from db.database import Base
from sqlalchemy import Column
from sqlalchemy import Update

##   Admin  ===============================================================================

##>>> BookNest: admin Model
class Dbadmin(Base):                 
    __tablename__ = 'admin'
    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String)
    secondname  = Column(String)
    username = Column(String)
    password = Column(String)
    email = Column(String)
    phone = Column(String)  #???
    adress = Column(String)
    nationality = Column(String)
    age = Column(Integer)

##   Customer  ===============================================================================

##>>> BookNest: Customer Model
class DbCustomer(Base):                 
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String)
    secondname  = Column(String)
    username = Column(String)
    password = Column(String)
    email = Column(String)
    phone = Column(String)  #???
    adress = Column(String)
    nationality = Column(String)
    age = Column(Integer)  #???
    items_c = relationship('DbArticleC', back_populates='customer')

##>>> BookNest: Article-Customer Model (Articles that be crated by customer)
class DbArticleC(Base):
    __tablename__ = 'articles-c'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    published = Column(Boolean)
    customer_id = Column(Integer, ForeignKey('customers.id'))   
    ##>>> ForeignKey customers for create relationship between articles & customers (It links two table together)
    customer = relationship('DbCustomer', back_populates= 'items_c')


##   Hotel  ===============================================================================

##>>> BookNest: Hotel Model
class DbHotel(Base):                 
    __tablename__ = 'hotels'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    manager  = Column(String)  #???
    username = Column(String)
    password = Column(String)
    email = Column(String)
    phone = Column(String) #???
    adress = Column(String)
    country = Column(String)
    city = Column(String) 
    rooms = Column(Integer) 
    star = Column(Integer)  #???
    items_h = relationship('DbArticleH', back_populates='hotel') 


##>>> BookNest: Article-Hotel Model (Articles that be crated by hotel)
class DbArticleH(Base):
    __tablename__ = 'articles-h'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    published = Column(Boolean)
    hotel_id = Column(Integer, ForeignKey('hotels.id'))   
    ##>>> ForeignKey hotels for create relationship between articles & hotels (It links two table together)
    hotel = relationship('DbHotel', back_populates= 'items_h')







































##   User  ===================================================================================

# ##>>> Whatis: Class (structure) for data that goes to database
# class DbUser(Base):                 
#     __tablename__ = 'users'
#     id = Column(Integer, primary_key=True, index=True)
#     username = Column(String)
#     email = Column(String)
#     password = Column(String)
#     items = relationship('DbArticle', back_populates='user')


# ##>>> Whatis: Article Model
# class DbArticle(Base):
#     __tablename__ = 'articles'
#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String)
#     content = Column(String)
#     published = Column(Boolean)
#     user_id = Column(Integer, ForeignKey('users.id'))   
#     ##>>> ForeignKey uses for create relationship between articles & users (It links two table together)
#     user = relationship('DbUser', back_populates= 'items')



