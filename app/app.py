from fastapi import FastAPI
from models import _get_time
import uvicorn

app = FastAPI()


@app.get("/")
def landing():
    return {"message": "API connected update"}


@app.get("/v1/now")
def get_time(as_integer: int = 0):
    resposne = _get_time(bool(as_integer))
    return resposne


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8080, reload=True)
