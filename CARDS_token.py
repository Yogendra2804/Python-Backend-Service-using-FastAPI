from fastapi import Depends , HTTPException
from fastapi.security import HTTPAuthorizationCredentials , HTTPBearer 
from jose import JWTError , jwt 
from pydantic import EmailStr
from Logging import  zlogger_config
import logging


logger = logging.getLogger(__name__)

SECRATE_KEY = "tHIS"
ALGORITHM = "HS256" 

outh_schema = HTTPBearer() 

def get_current_user(token : HTTPAuthorizationCredentials = Depends(outh_schema)):

    logging.info("Getting current user. ! ")
    
    token = token.credentials 

    userMail = verify_token(token) 

    if not userMail: 
        logging.error("Unauthorized request -_- ")
        raise HTTPException(401 , "Unauthorised Access")


def gen_token(payload):
    
    logging.info("Generate token request recived. ! ")
    
    token = jwt.encode(payload , SECRATE_KEY , algorithm=ALGORITHM)

    return token 


def verify_token(token : str):
    
    logging.info("Verfing Token . ! ")
    
    payload = jwt.decode(token , SECRATE_KEY , algorithms=[ALGORITHM]) 

    userMail = payload.get("sub")

    if not userMail: 
        logging.error("User not found. !")
        raise HTTPException(401 , "Unauthorized Access" ) 
    
    logging.info("User returned. !")
    return userMail

