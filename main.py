from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi.exceptions import HTTPException
from exceptions import StoryException
from router import customer
from router import hotel
from router import article_c
from router import article_h
from db import models
from db.database import engine


app = FastAPI()
app.include_router(customer.router)
app.include_router(article_c.router)
app.include_router(hotel.router)
app.include_router(article_h.router)

@app.exception_handler(StoryException)
def story_exception_handler(request: Request, exc: StoryException):   #>>> exc:exception
    return JSONResponse(
        status_code=418,  #>>> 418 is a classic test status code. It is used as an "Easter egg" in some websites.
        content= {'detail': exc.name}  #>>> "detail" is a standard key for any problems that occur in exceptions
    )


##>>> Whatis: If you want a custom handeler for HTTP exceptions, use below code.
##>>> But it intercept all exceptions. If you don't want this, then you can uncomment it.

# @app.exception_handler(HTTPException)
# def custom_handler(request: Request, exc: StoryException):
#     return PlainTextResponse(str(exc), status_code=400)  #>>> also can use: status_code= status.something


models.Base.metadata.create_all(engine) 
##>>Note :if something change in structure of tables, delete <fastapi-practice.db> 
##        and run the server again.























#from router import blog_get
#from router import blog_post
#from router import user
#from router import article

#app.include_router(user.router)
#app.include_router(article.router)
#app.include_router(blog_get.router)
#app.include_router(blog_post.router)

#@app.get('/hello')
#def index():
#    return {'message': 'Hello world!'}