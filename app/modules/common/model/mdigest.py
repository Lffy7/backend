from pydantic import BaseModel

class MessageDigest(BaseModel):
    dg: str
    name: str
