from pydantic import BaseModel

class CreateUser(BaseModel):
   user_name:str
   user_location:str

class order_item(BaseModel):
   food_id :int 
   food_quantity:int
   
class order(BaseModel):
   order_items: list[order_item]
   restaurant_id:int

class UpdateUser(BaseModel):
   user_id:int
   user_name:str
   user_location:str