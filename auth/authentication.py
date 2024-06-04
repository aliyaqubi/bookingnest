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

@router.post('/token')
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
