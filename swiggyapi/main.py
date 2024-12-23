from fastapi import FastAPI #
from config import settings  
from db.relation_update import create_db_and_tables #
from users.usersapi import user_router
app = FastAPI(title="Swiggy")
create_db_and_tables()

@app.get("/")
def index():
    return "all good"

app.include_router(user_router)




