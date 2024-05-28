from typing import List
from fastapi import APIRouter, Depends
from schemas import ArticleCBase, ArticleCDisplay
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_article_c

##>>> Whatis: create a router for articles-customer
router = APIRouter(       
    prefix= '/article-customer',
    tags= ['article-customer']    
)



##>>> Whatis: router for creation article-customer
@router.post('/', response_model= ArticleCDisplay)
def create_article_c(request: ArticleCBase, 
                db: Session = Depends(get_db)):
    return db_article_c.create_article_c(db, request)


##>>> Whatis: router for reading/retrieving articles-customer (one)
@router.get('/{id}', response_model= ArticleCDisplay)
def get_article_c(id: int, db: Session = Depends(get_db)):
    return db_article_c.get_article_c(db, id)
