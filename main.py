from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi.exceptions import HTTPException
from exceptions import StoryException
from router import customer, hotel, product_c, article_c, article_h, booking
from router import admin
from auth.oauth2 import oauth2_scheme
from auth import authentication
from db import models
from db.database import engine
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles


#> Block 1
app = FastAPI()
app.include_router(authentication.router)
app.include_router(admin.router)
app.include_router(customer.router)
app.include_router(article_c.router)
app.include_router(hotel.router)
app.include_router(article_h.router)
app.include_router(product_c.router)
app.include_router(booking.router)


#> Block 2
@app.exception_handler(StoryException)
def story_exception_handler(request: Request, exc: StoryException):   #>>> exc:exception
    return JSONResponse(
        status_code=418,  #>>> 418 is a classic test status code. It is used as an "Easter egg" in some websites.
        content= {'detail': exc.name}  #>>> "detail" is a standard key for any problems that occur in exceptions
    )


#> Block 3
##>>> Whatis: If you want a custom handeler for HTTP exceptions, use below code.
##>>> But it intercept all exceptions. If you don't want this, then you can uncomment it.
# @app.exception_handler(HTTPException)
# def custom_handler(request: Request, exc: StoryException):
#     return PlainTextResponse(str(exc), status_code=400)  #>>> also can use: status_code= status.something


#> Block 4
models.Base.metadata.create_all(engine) 
##>>Note :if something change in structure of tables, delete <fastapi-practice.db> and run server again.
      

#> Block 5: CORS - a standard functionality to build application on the same machine as building the endpoint.
origins = [
    'http://localhost:3000'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ['*'],
    allow_headers = ['*']
)
app.mount('/files', StaticFiles(directory="files"), name='files')