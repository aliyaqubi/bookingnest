from datetime import date
from pydantic import BaseModel
from sqlalchemy.orm.session import Session
from schemas import BookingBase
from db.models import DbBooking

# class BookingRequest(BaseModel):
#     hotel_id: int
#     customer_id: int
#     check_in: date
#     check_out: date

##> Block 1: createing book-hotel by customer
#@app.post("/bookings/")
def book_hotel(db: Session, booking: BookingBase): #= Depends(get_db)):
    # Assume there are models for Booking, Hotel, and Customer
    new_booking = DbBooking(
        check_in = booking.check_in,
        check_out = booking.check_out,
        hotel_id = booking.hotel_id,
        customer_id = booking.customer_id    
    )
    db.add(new_booking)
    db.commit()
    db.refresh(new_booking)
    return new_booking