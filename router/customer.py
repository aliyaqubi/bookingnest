from typing import List
from fastapi import APIRouter, Depends, File, UploadFile
from schemas import CustomerBase, CustomerDisplay
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_customer
from auth.oauth2 import oauth2_scheme, get_current_customer
import shutil
##>>>  BookNest: create a router for customers
router = APIRouter(       
    prefix= '/customer',
    tags= ['customer']    
)



##>>>  BookNest: create customers
@router.post('/', response_model= CustomerDisplay)
def create_customer(request: CustomerBase, 
                db: Session = Depends(get_db)):
    return db_customer.create_customer(db, request)


##>>>  BookNest: Read/retrieve customers (get all customers)
@router.get('/', response_model= List[CustomerDisplay])
def get_all_customers(db: Session = Depends(get_db),
                      current_customer: CustomerBase = Depends(get_current_customer)           #>>> forWhat: to add Authorization to secure it
                      ):
    return db_customer.get_all_customers(db)

##>>>  Howto: Read/retrieve customers (get the customers with one specific filter - here: id)
@router.get('/{username}', response_model= CustomerDisplay)
def get_customer_by_username(username: str, 
                 db: Session = Depends(get_db),
                 current_customer: CustomerBase = Depends(get_current_customer)           #>>> forWhat: to add Authorization to secure it
                 ):
    return db_customer.get_customer_by_username(db, username)

##>>>  Howto: Read/retrieve customers (get the customers with one specific filter - here: id)
@router.get('/{id}', response_model= CustomerDisplay)
def get_customer(id: int, 
                 db: Session = Depends(get_db),
                 current_customer: CustomerBase = Depends(get_current_customer)           #>>> forWhat: to add Authorization to secure it
                 ):
    return db_customer.get_customer(db, id)


##>>>  Howto: Read/retrieve customers (get the customers with more than one filter - here: id & secondname)
@router.get('/{id}/secondname', response_model= CustomerDisplay)
def get_customer_by_more_filter(id: int, 
                       secondname: str, 
                       db: Session = Depends(get_db),
                       current_customer: CustomerBase = Depends(get_current_customer)           #>>> forWhat: to add Authorization to secure it
                       ):
    return db_customer.get_customer_by_more_filter(db, id, secondname)


##>>>  BookNest: update customers
#@router.post('/{id}/update')       ##>>> trainer did it with .post instesd of .put

@router.put('/{id}')               ##>>>change to .put in class with Jurgen
def update_customer(id: int, 
                    request: CustomerBase, 
                    db: Session = Depends(get_db),
                    current_customer: CustomerBase = Depends(get_current_customer)           #>>> forWhat: to add Authorization to secure it
                    ):
    return db_customer.update_customer(db, id, request)


##>>>  BookNest: delete customers
#@router.get('/{id})/delete')     ##>>> trainer did it with .get instesd of .delete

@router.delete('/{id}')           ##>>>change to .delete in class with Jurgen
def delete_customer(id: int, 
                    db: Session = Depends(get_db),
                    current_customer: CustomerBase = Depends(get_current_customer)           #>>> forWhat: to add Authorization to secure it
                    ):
    return db_customer.delete_customer(db, id)

@router.post('/UploadID')
def get_upload_id(upload_file: UploadFile = File(...)):
    path= f"files/{upload_file.filename}"
    with open(path, 'w+b') as buffer:
        shutil.copyfileobj(upload_file.file, buffer)
    return{
        'filename': path,
        'type': upload_file.content_type
    }