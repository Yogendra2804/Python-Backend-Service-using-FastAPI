from fastapi import FastAPI
from Modle import CARDS, Value
from engine import session

app = FastAPI()
# -------------------------------------------------------------------------------------------------------
# ORM 


@app.get("/cards")
def ORM_get_CARD_details(iin: int):
    card = session.get(CARDS, iin)
    try:
        if card:
            return {
                "BIN/IIN": card.bin_iin,
                "Network/Scheme": card.network_Scheme,
                "Card Type": card.card_type,
                "Card Category": card.card_category,
                "Issuer": card.issuer,
            }
        session.close()
    except:
        session.close()
        return {"message": "You did not put the correct details. "}


@app.put("/cards")
def ORM_post_get_CARDS(data: Value):
    card = session.get(CARDS, data.IIN)
    try:
        if card:
            return {
                "BIN/IIN": card.bin_iin,
                "Network/Scheme": card.network_Scheme,
                "Card Type": card.card_type,
                "Card Category": card.card_category,
                "Issuer": card.issuer,
            }
        session.close()
    except:
        session.close()
        return {"message": "ORM expect caught something."}

