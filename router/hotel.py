from typing import List
from fastapi import APIRouter, Depends, File, UploadFile
from schemas import HotelBase, HotelDisplay
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_hotel
import shutil


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



##>>>  BookNest: Read/retrieve hotels (all)
@router.get('/', response_model= List[HotelDisplay])
def get_all_hotels(rooms:int, country: str = None, city: str = None, db: Session = Depends(get_db)):
    return db_hotel.get_all_hotels(db, city, country, rooms)

##>>>  Howto: Read/retrieve hotels (get the hotels with one specific filter - here: id)
@router.get('/{id}', response_model= HotelDisplay)
def get_hotel(id: int, db: Session = Depends(get_db)):
    return db_hotel.get_hotel(db, id)

#>>>  Howto: Read/retrieve hotels (get the hotels with more than one filter - here: id & email)
@router.get('/{id}/email', response_model= HotelDisplay)
def get_more_hotel(id: int, email: str, db: Session = Depends(get_db)):
    return db_hotel.get_more_hotel(db, id, email)


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

#Hotel owner can upload a Pic of his hotel
@router.post('/Pics')
def get_upload_pic(id:int, upload_file: UploadFile = File(...)):
    path= f"files/{upload_file.filename}"
    with open(path, 'w+b') as buffer:
        shutil.copyfileobj(upload_file.file, buffer)
    return{
        'id': id,
        'filename': path,
        'type': upload_file.content_type
    }