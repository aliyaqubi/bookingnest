from db.hash import Hash
from sqlalchemy.orm.session import Session
from schemas import adminBase
from db.models import Base
from db.models import Dbadmin, Update
from fastapi import HTTPException, status



##>>>  BookNest: create db for admin
def create_admin(db: Session, request: adminBase):   ##>>> Howto: create new admin in database 
    new_admin = Dbadmin(
        firstname = request.firstname,
        lastname = request.lastname,
        username = request.username,
        password = Hash.bcrypt(request.password),
        email = request.email,
        # phone = request.phone,   # ???
        # adress = request.adress,
        # nationality = request.nationality,
        # age = request.age
    )
    ##>>> Whatis: create elements
    db.add(new_admin)           ##>>> Howto: add new admin to database }
    db.commit()                    ##>>> Howto: send the operation to database }
    db.refresh(new_admin)       ##>>> Howto: to add the data that be created by database itself }
    return new_admin

##>>>  BookNest: Read/retrieve admin (get all admins)
def get_all_admin(db: Session):
    admin = db.query(Dbadmin).all()
    if not admin:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail= f'Customer with id {id} not found.') 
    return admin

##>>>  Howto: Read/retrieve admin by username (get the customers with one specific filter - here: username) {we need it in oauth2.py}
def get_admin_by_username(db: Session, username: str):
    admin = db.query(Dbadmin).filter(Dbadmin.username == username).first()
    if not admin:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
           detail= f'Admin with username {username} not found.') 
    return admin

##>>>  Howto: Read/retrieve admin (get the admin with one specific filter - here: id)
def get_admin(db: Session, id: int):
    admin = db.query(Dbadmin).filter(Dbadmin.id == id).first()
    if not admin:                                                               ## ATIQ ??? WHY NDERLINE
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
           detail= f'admin with id {id} not found.') 
    return admin

##>>>  Howto: Read/retrieve admin (get the admin with more than one filter - here: id & email)
def get_more_admin(db: Session, id: int, email: str):
    admin = db.query(Dbadmin).filter(Dbadmin.id == id).filter(Dbadmin.email == email).first()
    if not admin:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
           detail= f'admin with id {id} not found.') 
    return admin


##>>>  BookNest: update admin
def update_admin(db: Session, id: int, request: adminBase):
    adminquery = db.query(Dbadmin).filter(Dbadmin.id == id)
    if not adminquery:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail= f'admin with id {id} not found.') 
    adminquery.update({
        Dbadmin.firstname: request.firstname,
        Dbadmin.lastname: request.lastname,
        Dbadmin.username: request.username,
        Dbadmin.password: Hash.bcrypt(request.password),
        Dbadmin.email: request.email,
        # Dbadmin.phone: request.phone,  
        # Dbadmin.adress: request.adress,
        # Dbadmin.nationality: request.nationality,
        # Dbadmin.age: request.age
    })
    db.commit()
    return 'ok'

##>>>  BookNest: delete admin
def delete_admin(db: Session, id: int):
    admin = db.query(Dbadmin).filter(Dbadmin.id == id).first()
    if not admin:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
           detail= f'admin with id {id} not found.') 
    db.delete(admin)
    db.commit()
    return 'ok'