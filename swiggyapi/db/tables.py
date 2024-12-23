from sqlmodel import SQLModel,Field,Relationship


class Users(SQLModel,table=True):
    user_id: int|None = Field(primary_key=True,default=None)
    user_name:str = Field(nullable=False)
    location:str 

class Restaurant(SQLModel,table =True):
    rest_id:int = Field(primary_key=True,nullable=True)
    rest_name:str = Field(nullable=False,max_length=255)
    rest_location:str = Field(nullable=False,max_length=500)
    rest_type:str = Field(max_length=10)
    rest_menu:list["Restaurant_Menu"] = Relationship(back_populates="rests")

class Food_Item(SQLModel,table=True):
    food_id :int = Field(nullable=False,primary_key=True)
    food_name:str = Field(nullable=False)
    menu_items:list["Restaurant_Menu"] = Relationship(back_populates="food")


class Restaurant_Menu(SQLModel,table=True):
       rest_id:int = Field(foreign_key="restaurant.rest_id",nullable=False,primary_key=True)
       food_id:int = Field(nullable=False,foreign_key="food_item.food_id",primary_key=True)
       price:float = Field(nullable=False)
       food:Food_Item|None = Relationship(back_populates="menu_items")
       rests:Restaurant|None = Relationship(back_populates="rest_menu")

      