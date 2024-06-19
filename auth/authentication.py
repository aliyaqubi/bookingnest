from fastapi import APIRouter, HTTPException, status
from fastapi.param_functions import Depends
from fastapi.security.oauth2 import OAuth2PasswordRequestForm   #> this the form that is appeared by clicking Authorize Key in Swagger.
from sqlalchemy.orm.session import Session
from db.database import get_db
from db import models
from db.hash import Hash
from auth import oauth2




router = APIRouter(       
    tags= ['authentication']    
)

@router.post('/admin-token')
def get_token(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    admin = db.query(models.Dbadmin).filter(models.Dbadmin.username == request.username).first()  #> Checking if the username is correct
    if not admin:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid username")
    if not Hash.verify(admin.password, request.password):                                               #> Checking if the password is correct
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Incorrect password")     
    
    access_token = oauth2.create_access_token(data={'sub' : admin.username})                            #> generating token, after check u & p

    return{
        'access_token': access_token,
        'token_type': 'bearer',                                                  #> bearer: an standard type for access token that always be used
        'admin_id': admin.id,
        'username': admin.username
    }

@router.post('/customer-token')
def get_token(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    customer = db.query(models.DbCustomer).filter(models.DbCustomer.username == request.username).first()  #> Checking if the username is correct
    if not customer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid username")
    if not Hash.verify(customer.password, request.password):                                               #> Checking if the password is correct
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Incorrect password")     
    
    access_token = oauth2.create_access_token(data={'sub' : customer.username})                            #> generating token, after check u & p

    return{
        'access_token': access_token,
        'token_type': 'bearer',                                                  #> bearer: an standard type for access token that always be used
        'customer_id': customer.id,
        'username': customer.username
    }

@router.post('/hotel-token')
def get_token(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    hotel = db.query(models.DbHotel).filter(models.DbHotel.username == request.username).first()  #> Checking if the username is correct
    if not hotel:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid username")
    if not Hash.verify(hotel.password, request.password):                                               #> Checking if the password is correct
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Incorrect password")     
    
    access_token = oauth2.create_access_token(data={'sub' : hotel.username})                            #> generating token, after check u & p

    return{
        'access_token': access_token,
        'token_type': 'bearer',                                                  #> bearer: an standard type for access token that always be used
        'hotel_id': hotel.id,
        'username': hotel.username
    }