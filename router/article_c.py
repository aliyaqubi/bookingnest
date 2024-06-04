from typing import List
from fastapi import APIRouter, Depends
from db.models import DbCustomer
from schemas import ArticleCBase, ArticleCDisplay
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_article_c
from auth.oauth2 import oauth2_scheme, get_current_customer   #> import our variable from our file "oauth2" inside our folder"auth"
from schemas import CustomerBase


##>>> Whatis: create a router for articles-customer
router = APIRouter(       
    prefix= '/article-customer',
    tags= ['article-customer']    
)



##>>> Whatis: router for creation article-customer
@router.post('/', response_model= ArticleCDisplay)
def create_article_c(request: ArticleCBase, 
                db: Session = Depends(get_db), 
                current_customer: DbCustomer = Depends(get_current_customer)           #>>> forWhat: to add Authorization to secure it
                ):
    request.creator_id_c = current_customer.id
    return db_article_c.create_article_c(db, request)


##>>> Whatis: router for reading/retrieving articles-customer (Get specific article)
@router.get('/{id}')                                  #> response_model= ArticleCDisplay: it was deleted because of some replacings in the next lines
def get_article_c(id: int, 
                  db: Session = Depends(get_db), 
                  #token: str = Depends(oauth2_scheme)  #> it was replaced with next line
                  current_customer: CustomerBase = Depends(get_current_customer)         #>>> forWhat: to add Authorization to secure it
                  ):   
    #return db_article_c.get_article_c(db, id)  #> it was replaced with next line
    return {
        'data': db_article_c.get_article_c(db, id),
        'current_customer': current_customer
    }
