# main.py

from fastapi import FastAPI
import datetime

app = FastAPI()


@app.get("/")
def landing():
    return {"message": "API connected"}


@app.get("/v1/now")
def get_time(as_integer: int = 0):
    curr_datetime = datetime.datetime.now()
    response = curr_datetime.isoformat()
    print("as_integer {}".format(as_integer))
    if as_integer:
        response = curr_datetime.timestamp()
    return {
        "now": str(response)
    }
