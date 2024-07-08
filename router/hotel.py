from typing import List
from fastapi import APIRouter, Depends, File, UploadFile, status, HTTPException
from schemas import HotelBase, HotelDisplay
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_hotel
from auth.oauth2 import get_current_hotel
import shutil, random, string

##> Block 1: create router for hotels
router = APIRouter(       
    prefix= '/hotel',
    tags= ['hotel']    
)


##> Block 3: Difining types of image_url
##> absolute: When image comes from internet
##> relative: When image comes from uploaded images inside API (BookingNest\files)
image_url_types = ['absolute', 'relative']



##> Block 2: create hotels
@router.post('/', response_model= HotelDisplay)
def create_hotel(request: HotelBase, db: Session = Depends(get_db)):
    # if not request.image_url_type in image_url_types: #( because of problem in front-end)
    #     raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
    #                         detail="image_url_type can be only 'absolute' or 'relative'.")
    return db_hotel.create_hotel(db, request)


##> Read/retrieve hotels (all)
@router.get('/all', response_model= List[HotelDisplay])
def get_all_hotels(db: Session = Depends(get_db), country: str = None, city: str = None, 
                   #current_hotel: HotelBase = Depends(get_current_hotel)  #star:str = None,
                   ):
    return db_hotel.get_all_hotels(db, country, city)

##> Read/retrieve hotels (with one specific filter - here: id)
@router.get('/{id}', response_model= HotelDisplay)
def get_hotel(id: int, db: Session = Depends(get_db), 
              #current_hotel: HotelBase = Depends(get_current_hotel)
              ):
    #if not current_hotel.id == id:
     #   raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not allowed")
    return db_hotel.get_hotel(db, id)

#> Read/retrieve hotels (with more than one filter - here: id & email)
# @router.get('/{id}/email', response_model= HotelDisplay)
# def get_more_hotel(id: int, email: str, db: Session = Depends(get_db), 
#                    #current_hotel: HotelBase = Depends(get_current_hotel)
#                    ):
#     #if not current_hotel.id == id:
#      #   raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not allowed")
#     return db_hotel.get_more_hotel(db, id, email)


##> update hotels
@router.put('/{id}')                       #> another way:#@router.post('/{id}/update')
def update_hotel(id: int, request: HotelBase, db: Session = Depends(get_db), 
                 current_hotel: HotelBase = Depends(get_current_hotel)
                 ):
    if not current_hotel.id == id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not allowed")
    return db_hotel.update_hotel(db, id, request)


##> delete hotels
@router.delete('/{id}', status_code=204)                     #> another way:@router.get('/{id})/delete') 
def delete_hotel(id: int, db: Session = Depends(get_db), 
                 current_hotel: HotelBase = Depends(get_current_hotel)
                 ):
    if not current_hotel.id == id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not allowed")
    return db_hotel.delete_hotel(db, id)




##> Block 4: Upload image for Hotel (New version, video 106)
##> Attaching 6 random letters to end of filename, to prevent removing some images because of the same name  
@router.post('/image')
def upload_image(image: UploadFile = File(...),
                 current_hotel: HotelBase = Depends(get_current_hotel)
                 ):
    letters = string.ascii_letters
    rand_str = ''.join(random.choice(letters) for i in range(6))
    new = f'_{rand_str}.'
    filename = new.join(image.filename.rsplit('.', 1))
    path= f"images/{get_current_hotel.id}/{filename}"

    with open(path, 'w+b') as buffer:
        shutil.copyfileobj(image.file, buffer)
    return {'filename': path}



