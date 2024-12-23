from fastapi import APIRouter
from request import *

rest_router = APIRouter(prefix="/restaurant")

@rest_router.post("/create")
def create_resturant():
    pass

@rest_router.get("/get")
def get_restaurant(rest_id:int):
    pass


@rest_router.post("/update")
def update_restaurant(restuarant:Restuarant):
    pass

@rest_router.post("/create/menu")
def create_menu(menu:RestaurantMenu):
    pass


@rest_router.post("/update/menu")
def update_menu(menu:RestaurantMenu):
    pass


@rest_router.get("/get/menu")
def get_menu():
    #you must return the food_id, food_name,and restaurant_id
    pass

@rest_router.post("/delete/menu")
def delete_menu(menu_id:int):
    pass

@rest_router.post("/delete")
def delete_restaurant(rest_id:int):
    pass