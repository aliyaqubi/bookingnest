from typing import List
from fastapi import APIRouter, Depends
from schemas import HotelBase, HotelDisplay
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_hotel

##>>>  Whatis: create a router for hotels
router = APIRouter(       
    prefix= '/hotel',
    tags= ['hotel']    
)


##>>>  BookNest: create hotels

@router.post('/', response_model= HotelDisplay)
def create_hotel(request: HotelBase, 
                db: Session = Depends(get_db)):
    return db_hotel.create_hotel(db, request)


##>>>  BookNest: read/retrieve hotels (all)

@router.get('/', response_model= List[HotelDisplay])
def get_all_hotels(db: Session = Depends(get_db)):
    return db_hotel.get_all_hotels(db)

# ##>>>  Howto: read/retrieve user (one)
# @router.get('/{id}', response_model= UserDisplay)
# def get_user(id: int, db: Session = Depends(get_db)):
#     return db_user.get_user(db, id)

# ##>>>  Howto: read/retrieve user (more than one)
# @router.get('/{id}/email', response_model= UserDisplay)
# def get_more_user(id: int, email: str, db: Session = Depends(get_db)):
#     return db_user.get_more_user(db, id, email)


##>>>  BookNest: update hotels
#@router.post('/{id}/update')       ##>>> trainer did it with .post instesd of .put
@router.put('/{id}')               ##>>>change to .put in class with Jurgen
def update_hotel(id: int, request: HotelBase, db: Session = Depends(get_db)):
    return db_hotel.update_hotel(db, id, request)


##>>>  BookNest: delete hotels
#@router.get('/{id})/delete')     ##>>> trainer did it with .get instesd of .delete
@router.delete('/{id}')           ##>>>change to .delete in class with Jurgen
def delete_hotel(id: int, db: Session = Depends(get_db)):
    return db_hotel.delete_hotel(db, id)

#test