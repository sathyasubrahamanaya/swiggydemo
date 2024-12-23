from fastapi import APIRouter,Depends
from db.init import get_session
from sqlmodel import Session,select
from db.tables import Food_Item,Restaurant_Menu,Restaurant
from sqlalchemy.sql.operators import ilike_op,in_op
from .request_model import order
import random
from .request_model import CreateUser as user_request
from .request_model import UpdateUser
from  db.tables import Users as user_db
import datetime

random.seed(12)

user_router = APIRouter(prefix="/user")

def output_parser(output,issuccess=True):
    if issuccess:
        return {"Message":"Success","ErrorCode":0,"Data":output}
    else:
        return {"Message":"Failure","ErrorCode":1,"Data":output}
    



@user_router.get("/searchfood")
def searchfood(food_name:str="dosa",db:Session = Depends(get_session)):
    statement = select(Food_Item).filter(ilike_op(Food_Item.food_name,f'%{food_name}%'))
    food_items_id:list[int] = [food.food_id for food in db.exec(statement).all()]
    print(food_items_id)
    rest_list = db.exec(select(Restaurant).distinct()
                        .join(Restaurant_Menu,Restaurant.rest_id==Restaurant_Menu.rest_id)
                        .join(Food_Item,Food_Item.food_id == Restaurant_Menu.food_id)
                        .where(Restaurant_Menu.food_id.in_(food_items_id))).all()
    return output_parser(rest_list)

     
@user_router.get("/order")
def order_food(items:order,db:Session = Depends(get_session)):
    #work on later
    
    food_ids = [order_item.food_id for order_item in items.order_items]
    
    rest_list = db.exec(select(Restaurant,Food_Item).distinct()
                        .join(Restaurant_Menu,Restaurant.rest_id==Restaurant_Menu.rest_id)
                        .join(Food_Item,Food_Item.food_id == Restaurant_Menu.food_id)
                        .where(Restaurant_Menu.food_id.in_(food_ids))).all()
    restaurants, food_items = [] , []
    
    print(food_ids)
    order_summary = {"order_id":datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%d%h%m%"),
                     "order_date":datetime.datetime.now(datetime.timezone.tzname("ist")).date().ctime()
                   }

    return None
    
           
@user_router.get("/create")
def create_user(user_info:user_request, db:Session = Depends(get_session)):
    if user_info:
        # create a instance of User class
        row_count = db.query(user_db).count()
        user_row = user_db(user_id=row_count+1,user_name=user_info.user_name,location=user_info.user_location)
        db.add(user_row)
        db.commit()
        db.refresh(user_row)
        return {"ErrorCode":0,"Data":user_row,"Message":"user has been created"}
    
@user_router.get("/update")
def update_user(user_info:UpdateUser,db:Session = Depends(get_session)):
        statement = select(user_db).where(user_db.user_id == user_info.user_id)
        try:
          user_row= db.exec(statement).one()
          print("user:", user_row)

          user_row.user_name = user_info.user_name
          user_row.location = user_info.user_location
          db.add(user_row)
          db.commit()
          db.refresh(user_row)
          return {"ErrorCode":0,"Data":user_row,"Message":"user has been updated"}
        except:
             return {"ErrorCode":1,"Data":None,"Message":"user id not found"}

    
#order food
#cancel_food

#create a package restaurant
#create new restaureant
#delete restaurant
#update restuarant

# create a package food_item -->  CRUD APis 
# restaurent menu --> CRUD APIs