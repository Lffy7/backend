from typing import Annotated
from fastapi import Depends, FastAPI, Request
from fastapi.security import OAuth2PasswordBearer

# will break this in the future into micro structure so this entry page
# does not need to get too big with a lot of new endpoints
from modules.v1.home.welcome import welcome_http
from modules.v1.home.login import login_http
from modules.v1.message.arbitary import arbitary_http
from modules.common.model.arbitary import Arbitary

parish = FastAPI(title="Backend Server",
        summary="Backend Framework - REST-API Endpoints",
        version="6.12.13",
        )

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@parish.get("/")
async def welcome():
    return await welcome_http()
    
@parish.post("/v1/login")
async def login(data : Arbitary.JSONStructure):
    return await login_http(data)    

@parish.post("/v1/test")
async def testn(data : Arbitary.JSONStructure):
    return await arbitary_http(data)




