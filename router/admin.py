from typing import List
from fastapi import APIRouter, Depends
from schemas import adminBase, adminDisplay
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_admin
from auth.oauth2 import get_current_admin
from fastapi.responses import FileResponse

##>>>  BookNest: create a router for admin
router = APIRouter(       
    prefix= '/Admin',
    tags= ['admin']    
)

##>>>  BookNest: create admin

@router.post('/', response_model= adminDisplay)
def create_admin(request: adminBase, 
                db: Session = Depends(get_db)):
    return db_admin.create_admin(db, request)

##>>>  BookNest: Read/retrieve admin (get all admin)
@router.get('/', response_model= List[adminDisplay])
def get_all_admin(db: Session = Depends(get_db),
                  current_admin: adminBase = Depends(get_current_admin)
                  ):
    return db_admin.get_all_admin(db)

##>>>  Howto: Read/retrieve admins (get the customers with one specific filter - here: id)
@router.get('/{username}', response_model= adminDisplay)
def get_admin_by_username(username: str, 
                          db: Session = Depends(get_db),
                          current_admin: adminBase = Depends(get_current_admin)
                          ):
    return db_admin.get_admin_by_username(db, username)

##>>>  Howto: Read/retrieve admin (get the customers with more than one filter - here: id & email)
@router.get('/{id}/email', response_model= adminDisplay)
def get_more_admin(id: int, email: str, db: Session = Depends(get_db),
                   current_admin: adminBase = Depends(get_current_admin)
                   ):
    return db_admin.get_more_admin(db, id, email)


##>>>  BookNest: update admin
#@router.post('/{id}/update')       ##>>> trainer did it with .post instesd of .put

@router.put('/{id}')               ##>>>change to .put in class with Jurgen
def update_admin(id: int, request: adminBase, db: Session = Depends(get_db),
                 current_admin: adminBase = Depends(get_current_admin)
                 ):
    return db_admin.update_admin(db, id, request)


##>>>  BookNest: delete admin
#@router.get('/{id})/delete')     ##>>> trainer did it with .get instesd of .delete

@router.delete('/{id}')           ##>>>change to .delete in class with Jurgen
def delete_admin(id: int, db: Session = Depends(get_db),
                 current_admin: adminBase = Depends(get_current_admin)
                 ):
   return db_admin.delete_admin(db, id)

## admin can download the file (id) that is uploaded by customer
@router.get('/download/{name}', response_class=FileResponse)
def get_file(name: str):
    path= f'images/{name}'
    return path