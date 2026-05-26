'''
An API acts as an intermidate to allow comunication between multiple software systems. 
    API taks the user's request to the server and brings back the result or response.

    In simple terms it's a type of massenger that allows communication between two software's. 
    
'''

import sqlite3
from fastapi import FastAPI
from Modle import Value 

from Logging import zlogger_config
import logging


logger = logging.getLogger(__name__)

app = FastAPI()

connection = sqlite3.connect(
r"D:\Coding laungages\python\Base\sequal_light\Database\database1.db" , check_same_thread=False
)
cursor = connection.cursor()

logger.info("App strating. !")

@app.get("/cards/raw")
def get_CARDS_details(IIN : int):
    logger.info("get_CARDS_details was called. !")
    try :
        cursor.execute('SELECT * FROM CARDS WHERE "BIN_IIN" = ? ' , (IIN ,))    
        row = cursor.fetchone()
        if row == None:
            return { "message" : "CARD not found" }
        
        connection.close()

        return {
            "BIN/IIN": row[0],
            "Network/Scheme": row[1],
            "Card Type": row[2],
            "Card Category": row[3],
            "Issuer": row[4]
        }
    except Exception as e:
        connection.close()
        logger.error(f"An error occured - > {str(e)}")
        return {"message" : "You did not put the correct details. "}


@app.post("/cards")
def post_CARDS_details(data : Value):
    logger.info("post_CARDS_details was called. !")
    try :
        cursor.execute('SELECT * FROM CARDS WHERE "BIN_IIN" = ? ' , (data.IIN ,))    
        row = cursor.fetchone()
        if row == None:
            return { "message" : "CARD not found" }
        
        connection.close()
        return {
            "BIN/IIN": row[0],
            "Network/Scheme": row[1],
            "Card Type": row[2],
            "Card Category": row[3],
            "Issuer": row[4]
        }
    except Exception as e:    
        connection.close()
        logger.error(f"An error occured - > {str(e)}")
        return {"message" : "You did not put the correct details. "}



@app.post("/allCards")
def findBINS(name : str ):
    logger.info(f"findBINS was called. !")
    try: 
        bin_list = cursor.execute('SELECT bin_iin FROM CARDS WHERE "network_Scheme" = ? ' , (name))
        
        if not bin_list:
            logger.error(f"bin_list not found? check db errors? ")
            return {
                "msg" : "Name give not found. "
            }
        
        return {
            "bin_list" : bin_list 
        }

    except Exception as e:
        logger.error(f"An error occured - > {str(e)}")
        return{
            "msg" : "Something went wrong ! "
        }    