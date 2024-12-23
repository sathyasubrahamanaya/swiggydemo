from pydantic import BaseModel

class Restuarant(BaseModel):
    rest_id:int|None
    rest_name:str
    rest_location:str
    rest_type:str

class RestaurantMenu(BaseModel):
    rest_id:int
    food_id:int
    price:float

