from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes='bcrypt', deprecated = 'auto')    #or: schemes=["bcrypt"]

class Hash():
    def bcrypt(password: str):
        return pwd_cxt.hash(password)
    
    def verify(hashed_password, plain_password):
        return pwd_cxt.verify(plain_password, hashed_password)
    
#     hashed_password = pwd_context.hash(user.password)
#     db_user = User(username=user.username, hashed_password=hashed_password)