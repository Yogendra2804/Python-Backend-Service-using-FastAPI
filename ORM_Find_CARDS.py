from fastapi import FastAPI , Depends
from Modle import CARDS, Value
from engine import session
from CARDS_token import get_current_user , gen_token
from pydantic import EmailStr
from datetime import datetime , timedelta
from sqlalchemy import select
app = FastAPI()
# -------------------------------------------------------------------------------------------------------
# ORM 


# -------------------------------------------------------------------------------------------------------

import logging
from Logging import zlogger_config

logger = logging.getLogger(__name__)

logger.info("App starting. !")

@app.get("/cards")
def ORM_get_CARD_details(iin: int ,  _ : None = Depends(get_current_user)):
    logger.info("ORM_get_CARD_details. !")
    try:
        card = session.get(CARDS, iin)
        logger.debug(f"This was the card -> {card}")
        if card:
            logger.info(f"Detailes from {card.bin_iin} were returned")
            return {
                "BIN/IIN": card.bin_iin,
                "Network/Scheme": card.network_Scheme,
                "Card Type": card.card_type,
                "Card Category": card.card_category,
                "Issuer": card.issuer,
            }
        session.close()
        return {
            "msg" : "CARD Not found !"
        }
    
    except Exception as e:
        session.close()
        logger.error(f"Error occured. ! -> {str(e)}")
        return {"message": "You did not put the correct details. "}


@app.post("/cards")
def ORM_post_get_CARDS(data: Value , _ : None = Depends(get_current_user)):
    logger.info("ORM_post_CARD_details. !")
    try:
        card = session.get(CARDS, data.IIN)
        if card:
            logger.info(f"Detailes from {card.bin_iin} were returned")
            return {
                "BIN/IIN": card.bin_iin,
                "Network/Scheme": card.network_Scheme,
                "Card Type": card.card_type,
                "Card Category": card.card_category,
                "Issuer": card.issuer,
            }
        session.close()
    
        return{
            "msg" : "CARD Not found !"
        }
    
    except Exception as e:
        session.close()
        logger.error(f"Error occured. ! -> {str(e)}")
        return {"message": "ORM expect caught something."}


@app.post("/getToken")
def generateToken(Mail : EmailStr): 
    logger.info("generateTokens was called. !")
    payload = {
        "sub" : Mail , 
        "exp" : datetime.utcnow() + timedelta(minutes=5)
    }

    token = gen_token(payload)

    logger.info("Token Returned. ")
    return{
        "msg" : f"Your Token is : {token}"
    }

@app.post("/allCards")
def findBINS(name : str  , _ : None = Depends(get_current_user)):
    logger.info("findBINS was called. !")
    try: 
        # session.execute('SELECT "BIN/IIN" FROM CARDS WHERE "Network/Scheme" = ? ' , (name))
        bin_list = session.scalars(select(CARDS.bin_iin).where(CARDS.network_Scheme == name)).all()
        
        if not bin_list:
            logger.error(f"Bin list nnot found? Where's DB? bin_list = {bin_list}")
            return {
                "msg" : "Name give not found. "
            }

        logger.info("List found! .")
        return {
            "bin_list" : bin_list 
        }

    except Exception as e:
        logger.error(f"An error occured as -> {str(e)}")
        return{
            "msg" : "Something went wrong ! "
        }    
    
    
