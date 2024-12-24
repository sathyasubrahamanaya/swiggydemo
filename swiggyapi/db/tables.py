from sqlmodel import SQLModel,Field,Relationship
from sqlmodel import Column,JSON

class Users(SQLModel,table=True):
    user_id: int|None = Field(primary_key=True,default=None)
    user_name:str = Field(nullable=False)
    location:str 
    #note here
    users_order:list["Orders"]|None = Relationship(back_populates="order_users") #note here

class Restaurant(SQLModel,table =True):
    rest_id:int = Field(primary_key=True,nullable=True)
    rest_name:str = Field(nullable=False,max_length=255)
    rest_location:str = Field(nullable=False,max_length=500)
    rest_type:str = Field(max_length=10)
    rest_menu:list["Restaurant_Menu"] = Relationship(back_populates="rests")
    rest_order:list["Orders"]|None = Relationship(back_populates="order_rest")   #note here

class Food_Item(SQLModel,table=True):
    food_id :int|None = Field(nullable=False,primary_key=True,default=None)
    food_name:str = Field(nullable=False)
    menu_items:list["Restaurant_Menu"] = Relationship(back_populates="food")
    food_order:list["Orders"]|None = Relationship(back_populates="order_food") #note here



class Restaurant_Menu(SQLModel,table=True):
       rest_id:int = Field(foreign_key="restaurant.rest_id",nullable=False,primary_key=True)
       food_id:int = Field(nullable=False,foreign_key="food_item.food_id",primary_key=True)
       price:float = Field(nullable=False)
       food:Food_Item|None = Relationship(back_populates="menu_items")
       rests:Restaurant|None = Relationship(back_populates="rest_menu")
      
       

class Orders(SQLModel,table=True):
     order_id:int = Field(primary_key=True,)
     rest_id:int = Field(foreign_key="restaurant.rest_id",nullable=False)
     food_id:int = Field(nullable=False,foreign_key="food_item.food_id")
     user_id:int = Field(nullable=False,foreign_key="users.user_id")
     items:dict = Field(sa_column=Column(JSON)) #note here
     #relationship multiple relations
     # many users can have many orders #note here
     order_users:list[Users]|None = Relationship(back_populates="users_order") #note here
     order_rest:list[Restaurant]|None = Relationship(back_populates="rest_order")#note here
     order_food:list[Food_Item]|None = Relationship(back_populates="food_order")#note here





      