from db.hash import Hash
from sqlalchemy.orm.session import Session
from schemas import CustomerBase
from db.models import DbCustomer, Dbadmin
from fastapi import HTTPException, status



##> create customers
def create_customer(db: Session, request: CustomerBase):   ##>>> Howto: create new user in database 
    new_customer = DbCustomer(
        firstname = request.firstname,
        lastname = request.lastname,
        username = request.username,
        password = Hash.bcrypt(request.password),
        email = request.email,
        phone = request.phone,   
        # adress = request.adress,
        # nationality = request.nationality,
        # age = request.age
    )
                                   ##> create elements
    db.add(new_customer)           ##> add new user to database 
    db.commit()                    ##> send the operation to database 
    db.refresh(new_customer)       ##> to add the data that be created by database itself 
    return new_customer


##> Read/retrieve customers (all customers)
def get_all_customers(db: Session):
    customer = db.query(DbCustomer).all()
    if not customer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail= f'Customer with id {id} not found.') 
    return customer


##> Read/retrieve customers by username (with one specific filter - here: username) {we need it in oauth2.py}
def get_customer_by_username(db: Session, username: str):
    customer = db.query(DbCustomer).filter(DbCustomer.username == username).first()
    if not customer:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
           detail= f'Customer with username {username} not found.') 
    return customer


##> Read/retrieve customers (with more than one filter - here: id & lastname)
def get_customer_by_more_filter(db: Session, id: int, lastname: str):
    customer = db.query(DbCustomer).filter(DbCustomer.id == id).filter(DbCustomer.lastname == lastname).first()
    if not customer:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
           detail= f'Customer with id {id} or with lastname {lastname} not found.') 
    return customer

##> update customers
##> Note: There are two kinds of updating way:
##> 1. using update methode by: hotel.update({ DbHotel.name: request.name, ... }) without .first() in didfinition of hotel
##> 2. assigning the new values directly to the hotel instance's attributes.(ex:hotel.name= request.name) + .first() in didfinition of hotel
##> In db_customer.py the first way is used, and in db_hotel.py second way. (The second way is the correct way to handle updates. ???)

def update_customer(db: Session, id: int, request: CustomerBase):
    customer = db.query(DbCustomer).filter(DbCustomer.id == id)   #> .first() is deleted
    #admin = db.query(Dbadmin).all()
    if not customer: #and not admin:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail= f'Customer with id {id} not found.') 
    customer.update({
        DbCustomer.firstname: request.firstname,
        DbCustomer.lastname: request.lastname,
        DbCustomer.username: request.username,
        DbCustomer.password: Hash.bcrypt(request.password),
        DbCustomer.email: request.email,
        DbCustomer.phone: request.phone,  
        # DbCustomer.adress: request.adress,
        # DbCustomer.nationality: request.nationality,
        # DbCustomer.age: request.age
    })
    db.commit()
    return 'ok'


##> delete customers
def delete_customer(db: Session, id: int):
    customer = db.query(DbCustomer).filter(DbCustomer.id == id).first()
    #admin = db.query(Dbadmin).all()
    if not customer: #and not admin:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
           detail= f'Customer with id {id} not found.') 
    db.delete(customer)
    db.commit()
    return 'ok'

