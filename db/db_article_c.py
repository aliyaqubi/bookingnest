from exceptions import StoryException
from db.hash import Hash
from sqlalchemy.orm.session import Session
from schemas import ArticleCBase
from db.models import DbArticleC
from fastapi import HTTPException, status



##>>>  Whatis: create articles by customer
def create_article_c(db: Session, request: ArticleCBase):
    if request.content.startswith('Once upon a time'):  
        raise StoryException('No stories please')
    #>>>HowWork: in creating/updating article, if content start with this phrase, give an error and say: No story ...
      
    new_article_c = DbArticleC(
        title = request.title,
        content = request.content,
        published = request.published,
        rating = request.rating,
        customer_id = request.creator_id_c
    )
    db.add(new_article_c)            
    db.commit()                      
    db.refresh(new_article_c)        
    return new_article_c


##>>> Whatis: Read/retrieve articles of customer (one)
def get_article_c(db: Session, id: int):
    article_C = db.query(DbArticleC).filter(DbArticleC.id == id).first()
    if not article_C:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail= f'Article with id {id} not found.')                
    return article_C

