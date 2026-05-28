'''
An API acts as an intermidate to allow comunication between multiple software systems. 
    API taks the user's request to the server and brings back the result or response.

    In simple terms it's a type of massenger that allows communication between two software's. 
    
'''
import sqlite3
from fastapi import APIRouter
from Modle import Value

from Logging import zlogger_config
import logging

logger = logging.getLogger(__name__)

router = APIRouter()

connection = sqlite3.connect(
    r"D:\Coding laungages\python\Base\sequal_light\Database\database1.db",
    check_same_thread=False
)

cursor = connection.cursor()

logger.info("Router starting...!")




@router.post("/cards")
def post_CARDS_details(data: Value):
    logger.info("post_CARDS_details was called!")

    try:
        cursor.execute(
            'SELECT * FROM CARDS WHERE "BIN_IIN" = ?',
            (data.IIN,)
        )

        row = cursor.fetchone()

        if row is None:
            return {"message": "CARD not found"}

        return {
            "BIN/IIN": row[0],
            "Network/Scheme": row[1],
            "Card Type": row[2],
            "Card Category": row[3],
            "Issuer": row[4]
        }

    except Exception as e:
        logger.error(f"An error occurred -> {str(e)}")

        return {
            "message": "You did not put the correct details."
        }


@router.post("/allCards")
def findBINS(name: str):
    logger.info("findBINS was called!")

    try:
        cursor.execute(
            'SELECT BIN_IIN FROM CARDS WHERE "network_Scheme" = ?',
            (name,)
        )

        bin_list = cursor.fetchall()

        if not bin_list:
            logger.error("bin_list not found")

            return {
                "msg": "Name given not found."
            }

        return {
            "bin_list": [row[0] for row in bin_list]
        }

    except Exception as e:
        logger.error(f"An error occurred -> {str(e)}")

        return {
            "msg": "Something went wrong!"
        }