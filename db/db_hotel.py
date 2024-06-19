from db.hash import Hash
from sqlalchemy.orm.session import Session
from schemas import HotelBase
from db.models import DbHotel
from fastapi import HTTPException, status
from datetime import datetime


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
        star = request.star,
        image_url = request.image_url,
        image_url_type = request.image_url_type,
        image_caption = request.image_caption,
        #timestamp = datetime.datetime.now()   
        )
    ##>>> Whatis: create elements
    db.add(new_hotel)           ##>>> Howto: add new hotel to database 
    db.commit()                 ##>>> Howto: send the operation to database 
    db.refresh(new_hotel)       ##>>> Howto: to add the data that be created by database itself 
    return new_hotel

def get_hotel_by_username(db: Session, username: str):
    hotel = db.query(DbHotel).filter(DbHotel.username == username).first()
    if not hotel:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
           detail= f'Hotel with username {username} not found.') 
    return hotel

##>>>  BookNest: Read/retrieve hotels (all)
def get_all_hotels(db: Session, city: str, country: str, star: int):
    hotelQuery = db.query(DbHotel)
    
    if(city != None):
        hotelQuery = hotelQuery.filter(DbHotel.city.contains(city))
    
    if(country != None):
        hotelQuery = hotelQuery.filter(DbHotel.country == country)
    
    if(star != None):
        hotelQuery = hotelQuery.filter(DbHotel.star == star)
    
    return hotelQuery.all()

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
##>>>  Note: There are two kinds of updating way:
##>       1. using update methode by: hotel.update({ DbHotel.name: request.name, ... }) without .first() in didfinition of hotel
##>       2. assigning the new values directly to the hotel instance's attributes.(ex:hotel.name= request.name) + .first() in didfinition of hotel
##>    In db_customer.py the first way is used, and in db_hotel.py second way. (The second way is the correct way to handle updates. ???)

def update_hotel(db: Session, id: int, request: HotelBase):
    hotel = db.query(DbHotel).filter(DbHotel.id == id).first()
    if not hotel:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail= f'Hotel with id {id} not found.')
    hotel.name= request.name
    hotel.manager= request.manager
    hotel.username= request.username
    hotel.password= Hash.bcrypt(request.password)
    hotel.email= request.email
    hotel.phone= request.phone 
    hotel.adress= request.adress
    hotel.country= request.country
    hotel.city= request.city 
    hotel.rooms= request.rooms
    hotel.star= request.star
    hotel.image_url = request.image_url
    hotel.image_url_type = request.image_url_type
    hotel.image_caption = request.image_caption
    #hotel.timestamp = datetime.datetime.now()      
    
    # hotel.update({
    #     DbHotel.name: request.name,
    #     DbHotel.manager: request.manager,
    #     DbHotel.username: request.username,
    #     DbHotel.password: Hash.bcrypt(request.password),
    #     DbHotel.email: request.email,
    #     DbHotel.phone: request.phone, 
    #     DbHotel.adress: request.adress,
    #     DbHotel.country: request.country,
    #     DbHotel.city: request.city, 
    #     DbHotel.rooms: request.rooms,
    #     DbHotel.star: request.star   
    # })

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
    return
