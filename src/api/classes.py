from pydantic import BaseModel

class Authorize_Class(BaseModel):
    token: str

