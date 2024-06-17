##>>> Whatis: Token generation code (CopyPaste from Udemy)

from fastapi.security import OAuth2PasswordBearer   #> Whatis: let the system know that we want to secure our endpoints.
from typing import Optional
from datetime import datetime, timedelta
from jose import jwt                                #> jwt: JSON Web Tokens
from jose.exceptions import JWTError
from fastapi.param_functions import Depends
from sqlalchemy.orm import Session
from db.database import get_db
from fastapi import HTTPException, status
from db import db_customer, db_admin
 
 
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")     #> Whatis: provide the endpoint for our token retrieval.

##Whatis: secret key is the key that allows us to sign the token yhar be generated. (it's random but should be unique.)
#The secret key used to verify the token's signature. It should be a secure, private key known only to the server.
# The algorithm used to decode the token. It’s usually specified as a string or a list of strings, such as "HS256".
SECRET_KEY = '77407c7339a6c00769e51af1101c4abb4aea2a31157ca5f7dfd87da02a628107'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30
 
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
  to_encode = data.copy()
  if expires_delta:
    expire = datetime.utcnow() + expires_delta
  else:
    expire = datetime.utcnow() + timedelta(minutes=15)
  to_encode.update({"exp": expire})
  encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)      #>>> using jwt for encoding
  return encoded_jwt






##> Block 3: to retrieve the current admin that the token is attached to, & verify the token to make sure the customer is authenticated.
def get_current_admin(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
  credentials_exception = HTTPException(                             #> with this exception we can raise if we find an error in our code.
    status_code= status.HTTP_401_UNAUTHORIZED,
    detail = 'Could not validate the credentials of the admin',
    headers={'WWW-Authenticate': 'Bearer'}                           #> Standard HTTP exception if we can not authorize a user.
  )
  try:                                                               #> The try block is used to wrap code that may raise exceptions. 
    payload = jwt.decode(token, SECRET_KEY, algorithms=(ALGORITHM))  #> using jwt for decoding. payload is the result of decoding the token.
    username: str = payload.get('sub')                               #> a standard way to retrieve a username from a token
    if username is None:                                             #> i.e if the 'sub' claim is not present in the payload. (sub:subject)
      raise credentials_exception                                    #> It's raised when token is invalid or credentials are not provided.
  ##>>> Whatis: WTError is an exception from the JWT library, which is raised when there is an issue with decoding the token. 
  ##>>>         (e.g., invalid token, signature verification failed).                                    
  except JWTError:                                                   #> Catches any JWTError exceptions that occur during decoding of token.
    raise credentials_exception                                     
  
  admin = db_admin.get_admin_by_username(db, username)      #> in db_customer we changed get_customer with get_customer_by_username
  if admin is None:
    raise credentials_exception
  
  return admin



##>>> Whatis: to retrieve the current customer that the token is attached to, & verify the token to make sure the customer is authenticated.
def get_current_customer(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
  credentials_exception = HTTPException(                             #> with this exception we can raise if we find an error in our code.
    status_code= status.HTTP_401_UNAUTHORIZED,
    detail = 'Could not validate the credentials of the customer',
    headers={'WWW-Authenticate': 'Bearer'}                           #> Standard HTTP exception if we can not authorize a user.
  )
  try:                                                               #> The try block is used to wrap code that may raise exceptions. 
    payload = jwt.decode(token, SECRET_KEY, algorithms=(ALGORITHM))  #> using jwt for decoding. payload is the result of decoding the token.
    username: str = payload.get('sub')                               #> a standard way to retrieve a username from a token
    if username is None:                                             #> i.e if the 'sub' claim is not present in the payload. (sub:subject)
      raise credentials_exception                                    #> It's raised when token is invalid or credentials are not provided.
  ##>>> Whatis: WTError is an exception from the JWT library, which is raised when there is an issue with decoding the token. 
  ##>>>         (e.g., invalid token, signature verification failed).                                    
  except JWTError:                                                   #> Catches any JWTError exceptions that occur during decoding of token.
    raise credentials_exception                                     
  
  customer = db_customer.get_customer_by_username(db, username)      #> in db_customer we changed get_customer with get_customer_by_username
  if customer is None:
    raise credentials_exception
  
  return customer

