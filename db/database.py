from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
 
SQLALCHEMY_DATABASE_URL = "sqlite:///./BookingNest.db"   #>>> <BookingNest> for each new virtual environment should be renamed.
 
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
 
Base = declarative_base()   ##{This variable as a construct will use in code to create Models.}

##==================================================================================

## 1 {to get a hold of the database to perform operations from anywhere in our code}
##   {any time we perform any operation on database, we get SessionLocal then use it by: yield and finally close it.}
def get_db():
    db = SessionLocal()
    try:                 ## {The try keyword is used in try...except blocks. It defines a block of code test if it contains any errors.}
        yield db         ## {The yield keyword is used to return a list of values from a function.}
    finally:
        db.close()

