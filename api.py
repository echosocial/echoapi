from typing import Union
from deta import Deta
from dotenv import load_dotenv, dotenv_values
from fastapi import FastAPI

load_dotenv()
deta = Deta()
db = deta.Base("chats")
app = FastAPI()

res = db.fetch()
all_items = res.items

# Continue fetching until "res.last" is None.
while res.last:
    res = db.fetch(last=res.last)
    all_items += res.items

@app.get("/")
def read_root():
    return {(str(all_items))}

