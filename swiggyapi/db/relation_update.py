from .init import engine
from .tables import Food_Item,Restaurant_Menu,Restaurant,SQLModel
from sqlmodel import Session


def update_food_restaurent_item_relation():
    with Session(engine) as session:
    # Find the restaurant and food item
        restaurant = session.get(Restaurant, 1)  # Assuming restaurant with id 1 exists
        food_item = session.get(Food_Item, 2)   # Assuming food_item with id 2 exists

    # Create a new menu entry
    new_menu_item = Restaurant_Menu(
        rest_id=restaurant.rest_id,
        food_id=food_item.food_id,
        price=12.99
    )

    # Add it to the session
    session.add(new_menu_item)

    # Commit the changes to the database
    session.commit()


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
    #update_food_restaurent_item_relation()