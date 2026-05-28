from fastapi import FastAPI
import Logging.zlogger_config 
from Find_CARDS import router as Find_CARDS_rounter 
from ORM_Find_CARDS import router as ORM_Find_CARDS_rounter

import logging
logger = logging.getLogger(__name__)


app = FastAPI()
logger.info("App/ main server starting ...")


app.include_router(Find_CARDS_rounter)
logger.info("fetched API's from Find_CARDS.py")

app.include_router(ORM_Find_CARDS_rounter)
logger.info("fetched API's from ORM_Find_CARDS.py")

@app.get("/")
def mai():
  return {
    "msg" : "Type /docs in the url" 
  }
  
