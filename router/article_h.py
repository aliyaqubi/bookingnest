from typing import List
from fastapi import APIRouter, Depends
from schemas import ArticleHBase, ArticleHDisplay
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_article_h

##>>> Whatis: create a router for articles-hotel
router = APIRouter(       
    prefix= '/article-hotel',
    tags= ['article-hotel']    
)



##>>> Whatis: router for creation article-hotel
@router.post('/', response_model= ArticleHDisplay)
def create_article_h(request: ArticleHBase, 
                db: Session = Depends(get_db)):
    return db_article_h.create_article_h(db, request)


##>>> Whatis: router for reading/retrieving articles-hotel (one)
@router.get('/{id}', response_model= ArticleHDisplay)
def get_article_h(id: int, db: Session = Depends(get_db)):
    return db_article_h.get_article_h(db, id)
