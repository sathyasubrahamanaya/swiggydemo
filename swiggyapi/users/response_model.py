from pydantic import BaseModel

class user(BaseModel):
    user_id:int
    user_name:str
    user_location:str