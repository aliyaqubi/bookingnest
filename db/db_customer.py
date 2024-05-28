from db.hash import Hash
from sqlalchemy.orm.session import Session
from schemas import CustomerBase
from db.models import DbCustomer
from fastapi import HTTPException, status



##>>>  BookNest: create customers
def create_customer(db: Session, request: CustomerBase):   ##>>> Howto: create new user in database 
    new_customer = DbCustomer(
        firstname = request.firstname,
        secondname = request.secondname,
        username = request.username,
        password = Hash.bcrypt(request.password),
        email = request.email,
        phone = request.phone,   # ???
        adress = request.adress,
        nationality = request.nationality,
        age = request.age
    )
    ##>>> Whatis: create elements
    db.add(new_customer)           ##>>> Howto: add new user to database }
    db.commit()                    ##>>> Howto: send the operation to database }
    db.refresh(new_customer)       ##>>> Howto: to add the data that be created by database itself }
    return new_customer


##>>>  BookNest: Read/retrieve customers (get all customers)
def get_all_customers(db: Session):
    customer = db.query(DbCustomer).all()
    if not customer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail= f'Customer with id {id} not found.') 
    return customer

##>>>  Howto: Read/retrieve customers (get the customers with one specific filter - here: id)
def get_customer(db: Session, id: int):
    customer = db.query(DbCustomer).filter(DbCustomer.id == id).first()
    if not customer:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
           detail= f'Customer with id {id} not found.') 
    return customer

##>>>  Howto: Read/retrieve customers (get the customers with more than one filter - here: id & email)
def get_more_customer(db: Session, id: int, email: str):
    customer = db.query(DbCustomer).filter(DbCustomer.id == id).filter(DbCustomer.email == email).first()
    if not customer:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
           detail= f'Customer with id {id} not found.') 
    return customer


##>>>  BookNest: update customers
def update_customer(db: Session, id: int, request: CustomerBase):
    customer = db.query(DbCustomer).filter(DbCustomer.id == id).first()
    if not customer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail= f'Customer with id {id} not found.') 
    customer.update({
        DbCustomer.firstname: request.firstname,
        DbCustomer.secondname: request.secondname,
        DbCustomer.username: request.username,
        DbCustomer.password: Hash.bcrypt(request.password),
        DbCustomer.email: request.email,
        DbCustomer.phone: request.phone,  
        DbCustomer.adress: request.adress,
        DbCustomer.nationality: request.nationality,
        DbCustomer.age: request.age
    })
    db.commit()
    return 'ok'


##>>>  BookNest: delete customers
def delete_customer(db: Session, id: int):
    customer = db.query(DbCustomer).filter(DbCustomer.id == id).first()
    if not customer:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
           detail= f'Customer with id {id} not found.') 
    db.delete(customer)
    db.commit()
    return 'ok'
