##> Note 1: from schemas & models

# ##> Block 7: class RoomBase (rooms of each hotel) 

# class RoomBase(BaseModel):
#     room_number: int
#     roon_size: int
#     room_beds: int
#     room_type: str
#     room_amenities: str 
#     creator_id: int


# ##> Whatis: Class for Rooms that system send back to hotel (structure of data-display)
# class RoomDisplay(BaseModel):
#     room_number: int
#     roon_size: int
#     room_beds: int
#     room_type: str
#     room_amenities: str 
#     hotel: Hotel            ##>>> in this line hotel goes back to class: Hotel
#     class Config():
#         orm_mode = True

# ##> Whatis: class for the 'Room' inside the CustomerDisplay & HotelDisplay & BookingDisplay
# class Room(BaseModel):
#     room_number: int
#     roon_size: int
#     room_beds: int
#     room_type: str
#     room_amenities: str 
#     class Config():
#         orm_mode = True 

##>>> BookNest: Room Model
# class DbRoom(Base):                 
#     __tablename__ = 'rooms'
#     id = Column(Integer, primary_key=True, index=True)
#     room_number = Column(Integer)
#     room_size = Column(Integer)
#     room_beds = Column(Integer)
#     room_type = Column(String) 
#     room_amenities = Column(String) 
#     hotel_id = Column(Integer, ForeignKey('hotels.id'))
#     hotel = relationship('DbHotel', back_populates= 'items_room')
#     items_book = relationship('DbBooking', back_populates='room') 


#   items_rooms: list[Room] = []  ##>>> in this line Room goes back to class: Room
#   items_rooms: list[Room] = []  ##>>> in this line Room goes back to class: Room
#   items_room = relationship('DbRoom', back_populates='hotel')
#   items_room = relationship('DbRoom', back_populates='hotel')
#   room_id = Column(Integer, ForeignKey('rooms.id'))
#   room = relationship('DbRoom', back_populates= 'items_book')

#=================================================================================

##> Note 2: from customer & db_customer

# ##>>>  Howto: Read/retrieve customers (get the customers with one specific filter - here: id)
# @router.get('/{id}', response_model= CustomerDisplay)
# def get_customer(id: int, 
#                  db: Session = Depends(get_db),
#                  current_customer: CustomerBase = Depends(get_current_customer)           #>>> forWhat: to add Authorization to secure it
#                  ):
#     return db_customer.get_customer(db, id)


# ##>>>  Howto: Read/retrieve customers (get the customers with one specific filter - here: id) {Deactivated bcz of adding get_customer_by_username}
# def get_customer(db: Session, id: int):
#     customer = db.query(DbCustomer).filter(DbCustomer.id == id).first()
#     if not customer:
#        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#            detail= f'Customer with id {id} not found.') 
#     return customer

#=================================================================================

##> Note 3: from hotel & db_hotel

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



