import sqlite3
from fastapi import FastAPI
from Modle import Value

app = FastAPI()
def con():
    connection = sqlite3.connect(
    r"D:\Coding laungages\python\Base\sequal_light\Database\database1.db" , check_same_thread=False
    )
    cursor = connection.cursor()
    return connection , cursor

@app.post("/cards")
def get_CARDS_details(data : Value):
    try :
        connection , cursor = con()
        cursor.execute('SELECT * FROM CARDS WHERE "BIN/IIN" = ? ' , (data.IIN ,))    
        row = cursor.fetchone()
        connection.close()
        if row == None:
            return { "message" : "CARD not found" }
        
        return {
            "BIN/IIN": row[0],
            "Network/Scheme": row[1],
            "Card Type": row[2],
            "Card Category": row[3],
            "Issuer": row[4]
        }
    except:
        return {"message" : "You did not put the correct details. "}