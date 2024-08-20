# 4. The differences between these HTTP verbs are as below:
# - Post: We can create/post data to the server to be processed to a specified resource.
# URL: '/product/'
# return body: {...}
# response code: 201
# response body:{...}

# - Get: We can retrieve/read data from a server.
# URL: '/product/'  or  '/product/{id}'
# return body: -
# response code: 200
# response body:[{...} , {...} , {...} , ...]

# - Put: We can update a current resource with new data
# URL: '/product/{id}'
# return body: {...}
# response code: 200
# response body:{...}

# - Delete: We can delete/emove a specified resource.
# URL: '/product/{id}'
# return body: -
# response code: 204
# response body:-