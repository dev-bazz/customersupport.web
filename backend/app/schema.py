# pydantic models
from typing import Optional
from pydantic import BaseModel

class user(BaseModel):
    id = int
    email = str
    username = str
    companyName = str
    
class user_update(BaseModel):
    email = str
    username = str
    companyName = str
