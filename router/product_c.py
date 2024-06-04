from typing import List, Optional
from fastapi import APIRouter, Depends, Header, Cookie, Form
from fastapi.responses import Response, HTMLResponse, PlainTextResponse


#> Block 1: create a router for product-customer
router = APIRouter(       
    prefix= '/product',
    tags= ['product']    
)

products = ['rooms', 'laundry', 'pick/drop service']


#> Block 6: create product
@router.post('/new')
def create_product(name: str = Form(...)):
    products.append(name)
    return products


#> Block 2: retrieve all product + set cookies
@router.get('/all')
def get_all_products():
    data = ' '.join(products)   #>>> converting the list to a string with one space between
    response = Response(content=data, media_type="plain/text")
    response.set_cookie(key='test_cookie', value='test_cookie_value')     #> setting cookie 
    return response 


#> Block 5: add/provide headers + retrieve cookies
@router.get('/withheader')
def get_products(response: Response, 
                   #custom_header: Optional[str] = Header(None)          #>in case of adding one header
                    custom_header: List[Optional[str]] = Header(None),   #>in case of adding a list of multiple headers
                    #> In above line: List[Optional[str]] is correct, Not Optional[List[str]] as he said in Udemy 46
                    test_cookie: Optional[str] = Cookie(None)            #> retrieving cookie 
                   ):
    if custom_header:
        response.headers['custom_response_header'] = ', '.join(custom_header)        #>adding response headers
    return {
        'data': products,
        'custom_header': custom_header,
        'my_cookie': test_cookie
    }



#> Block 4: providing a list of responses inside router, in order to declare that there are different types of responses. 
@router.get('/{id}', responses= {
    200: {
        'contenet': {
            'text/html': {
                'example': '<div>Product</div>'
            }
        },
        'description': 'Returns the HTML for an object.'
    },
    404: {
        'contenet': {
            'text/plain': {
                'example': 'Product not available'
            }
        },
        'description': 'A cleartext error message.'
    }
})

#> Block 3: this endpoint & functionality can return different responses based on some internal logic.
#>             first part return a plainText kind of responce and second part return an HTML
def get_product(id: int):
    if id > len(products):                                 #>provide some functionality if the product is not found
        out = 'Product not available'
        return PlainTextResponse(status_code=404, content=out, media_type='text/plain')
    else:
        product = products[id]             
        out = f"""                                           #>start of building HTML
        <head>                                               #>start 'head'
            <style>                                          #>start 'style'
            .product {{
                width: 500xp;
                height: 30px;
                border: 2px inset green;
                background-color: lightblue;
                text-align: center;
            }}
            </style>                                         #>end 'head'
        </head>                                              #>end 'style'
        <div class= 'products'>{product}</div>
        """
        return HTMLResponse(content=out, media_type="text/html")                  #> return an HTML type of responce

