from db.hash import Hash
from sqlalchemy.orm.session import Session
from schemas import HotelBase
from db.models import DbHotel
from fastapi import HTTPException, status


##>>>  BookNest: create hotels
def create_hotel(db: Session, request: HotelBase):   ##>>> Howto: create new hotel in database 
    new_hotel = DbHotel(
        name = request.name,
        manager = request.manager,
        username = request.username,
        password = Hash.bcrypt(request.password),
        email = request.email,
        phone = request.phone, 
        adress = request.adress,
        country = request.country,
        city = request.city, 
        rooms = request.rooms, 
        star = request.star   
    )
    ##>>> Whatis: create elements
    db.add(new_hotel)           ##>>> Howto: add new hotel to database 
    db.commit()                 ##>>> Howto: send the operation to database 
    db.refresh(new_hotel)       ##>>> Howto: to add the data that be created by database itself 
    return new_hotel


##>>>  BookNest: Read/retrieve hotels (all)
def get_all_hotels(db: Session):
    hotel = db.query(DbHotel).all()
    if not hotel:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail= f'Hotel with id {id} not found.') 
    return hotel

##>>>  Howto: Read/retrieve hotels (get the hotels with one specific filter - here: id)
def get_hotel(db: Session, id: int):
    hotel = db.query(DbHotel).filter(DbHotel.id == id).first()
    if not hotel:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail= f'Hotel with id {id} not found.') 
    return hotel

#>>>  Howto: Read/retrieve hotels (get the hotels with more than one filter - here: id & email)
def get_more_hotel(db: Session, id: int, email: str):
    hotel = db.query(DbHotel).filter(DbHotel.id == id).filter(DbHotel.email == email).first()
    if not hotel:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail= f'Hotel with id {id} not found.') 
    return hotel


##>>>  BookNest: update hotels
def update_hotel(db: Session, id: int, request: HotelBase):
    hotel = db.query(DbHotel).filter(DbHotel.id == id).first()
    if not hotel:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail= f'Hotel with id {id} not found.') 
    hotel.update({
        DbHotel.name: request.name,
        DbHotel.manager: request.manager,
        DbHotel.username: request.username,
        DbHotel.password: Hash.bcrypt(request.password),
        DbHotel.email: request.email,
        DbHotel.phone: request.phone, 
        DbHotel.adress: request.adress,
        DbHotel.country: request.country,
        DbHotel.city: request.city, 
        DbHotel.rooms: request.rooms,
        DbHotel.star: request.star   
    })
    db.commit()
    return 'ok'

##>>>  BookNest: delete hotels
def delete_hotel(db: Session, id: int):
    hotel = db.query(DbHotel).filter(DbHotel.id == id).first()
    if not hotel:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail= f'Hotel with id {id} not found.') 
    db.delete(hotel)
    db.commit()
    return 'ok'
