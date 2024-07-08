from typing import List
from fastapi import APIRouter, Depends, File, UploadFile, HTTPException, status
from schemas import CustomerBase, CustomerDisplay, adminBase
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_customer
from auth.oauth2 import get_current_customer
#from auth.oauth2 import get_current_admin
import shutil



##> create router customers
router = APIRouter(       
    prefix= '/customer',
    tags= ['customer']    
)



##> create customer
@router.post('/' , response_model= CustomerDisplay)
def create_customer(request: CustomerBase, 
                db: Session = Depends(get_db)):
    return db_customer.create_customer(db, request)


##> Read/retrieve customers (all customers)
@router.get('/', response_model= List[CustomerDisplay])
def get_all_customers(db: Session = Depends(get_db),
                      #current_customer: CustomerBase = Depends(get_current_customer)           #>>> forWhat: to add Authorization to secure it
                      ):
    return db_customer.get_all_customers(db)

##> Read/retrieve customers (with one specific filter - here: username)
@router.get('/{username}', response_model= CustomerDisplay)
def get_customer_by_username(
                 username: str, 
                 db: Session = Depends(get_db),
                 current_customer: CustomerBase = Depends(get_current_customer)           #>>> forWhat: to add Authorization to secure it
                 ):
    if not current_customer.username == username:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not allowed")
    return db_customer.get_customer_by_username(db, username)


##> Read/retrieve customers (with more than one filter - here: id & lastname)
# @router.get('/{id}/lastname', response_model= CustomerDisplay)
# def get_customer_by_more_filter(id: int, 
#                        lastname: str, 
#                        db: Session = Depends(get_db),
#                        current_customer: CustomerBase = Depends(get_current_customer)           #>>> forWhat: to add Authorization to secure it
#                        ):
#     if not current_customer.id == id:
#         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not allowed")
#     return db_customer.get_customer_by_more_filter(db, id, lastname)


##> update customers
@router.put('/{id}')              
def update_customer(id: int, 
                    request: CustomerBase, 
                    db: Session = Depends(get_db),
                    current_customer: CustomerBase = Depends(get_current_customer),           #>>> forWhat: to add Authorization to secure it
                    #current_admin: adminBase = Depends(get_current_admin)
                    ):
    if not current_customer.id == id: #and not current_admin:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not allowed")
    return db_customer.update_customer(db, id, request)


##> delete customers
@router.delete('/{id}', status_code=204)          
def delete_customer(id: int, 
                    db: Session = Depends(get_db),
                    current_customer: CustomerBase = Depends(get_current_customer),           #>>> forWhat: to add Authorization to secure it
                    #current_admin: adminBase = Depends(get_current_admin)
                    ):
    if not current_customer.id == id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not allowed")
    return db_customer.delete_customer(db, id)


@router.post('/UploadID')
def get_upload_id(upload_file: UploadFile = File(...),
                  current_customer: CustomerBase = Depends(get_current_customer)
                  ):
    path= f"files/{upload_file.filename}"
    with open(path, 'w+b') as buffer:
        shutil.copyfileobj(upload_file.file, buffer)
    return{
        'filename': path,
        'type': upload_file.content_type
    }