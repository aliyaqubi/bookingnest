from typing import List
from fastapi import APIRouter, Depends
from fastapi.responses import Response, HTMLResponse
# from sqlalchemy.orm import Session
# from db.database import get_db
# from db import db_article_c

##>>> Whatis: create a router for product-customer
router = APIRouter(       
    prefix= '/product-customer',
    tags= ['product-customer']    
)

products_c = ['a', 'b', 'c']

@router.get('/all')
def get_all_products_c():
#    return products_c
    data = ' '.join(products_c)   #>>> converting the list to a string with one space between
    return Response(content=data, media_type="plain/text") 

@router.get('/{id}')
def get_product_C(id: int):
    product_c = products_c[id]
    out = f"""
    <head>                                 #>start 'head'
        <style>                            #>start 'style'
        .product_c {{
            width: 500xp;
            height: 30px;
            border: 2px inset green;
            background-color: lightblue;
            text-align: center;
        }}
        </style>                            #>end 'head'
    </head>                                 #>end 'style'
    <div class='products_c'>{product_c}</div>
    """
    return HTMLResponse(content=out, media_type="text/html")