from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from dotenv import load_dotenv
import os
from middleware import AccessTokenMiddleware
from util import create_url

load_dotenv()

app = FastAPI()
# app.add_middleware(AccessTokenMiddleware)

@app.get("/")
async def root():
    return {"message": "Orc4bike API running"}

@app.get("/qr/{id}")
def redirect_qr(id: str):
    url = create_url(id)
    return RedirectResponse(url)

