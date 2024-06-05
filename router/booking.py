from typing import List
from fastapi import APIRouter, Depends
from db.models import DbBooking
from schemas import BookingBase, BookingDisplay, CustomerBase, HotelBase
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_booking
from auth.oauth2 import oauth2_scheme, get_current_customer   #> import our variable from our file "oauth2" inside our folder"auth"


##> Block 1: creating router for booking
router = APIRouter(       
    prefix= '/bookings',
    tags= ['bookings']    
)

##> Block 2: router for creation book-hotel
@router.post('/', response_model= BookingDisplay)
def book_hotel(booking: BookingBase, 
                db: Session = Depends(get_db) 
                #current_customer: DbCustomer = Depends(get_current_customer)           #>>> forWhat: to add Authorization to secure it
                ):
    #request.creator_id_c = current_customer.id
    return db_booking.book_hotel(db, booking)