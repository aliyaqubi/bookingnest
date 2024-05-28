from exceptions import StoryException
from db.hash import Hash
from sqlalchemy.orm.session import Session
from schemas import ArticleHBase
from db.models import DbArticleH
from fastapi import HTTPException, status



##>>>  Whatis: create articles by hotel
def create_article_h(db: Session, request: ArticleHBase):
    if request.content.startswith('Once upon a time'):  
        raise StoryException('No stories please')
    #>>>HowWork: in creating/updating article, if content start with this phrase, give an error and say: No story ...
    
    new_article_h = DbArticleH(
        title = request.title,
        content = request.content,
        published = request.published,
        hotel_id = request.creator_id_h
    )
    db.add(new_article_h)            
    db.commit()                      
    db.refresh(new_article_h)        
    return new_article_h


##>>> Whatis: Read/retrieve articles of hotel (one)
def get_article_h(db: Session, id: int):
    article_h = db.query(DbArticleH).filter(DbArticleH.id == id).first()
    if not article_h:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail= f'Article with id {id} not found.') 
    return article_h

