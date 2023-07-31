'''

Author: James Lakis

Date: Jul 23, 2023

Inspired by: SqlModel - Code Structure and Multiple Files
https://sqlmodel.tiangolo.com/tutorial/code-structure/

'''

from sqlmodel import Session, select
from fastapi import FastAPI

# app modules
from database import create_db_and_tables
from models import Animals
from engine import engine


app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()
    

##### Routes #####
    
    
@app.get("/")
async def root():
    return {"message": "Hello World!"}


@app.post("/animals/")
def create_animal(animal: Animals):
    with Session(engine) as session:
        session.add(animal)
        session.commit()
        session.refresh(animal)
        return animal


@app.get("/animals/")
def read_animals():
    with Session(engine) as session:
        animals = session.exec(select(Animals)).all()
        return animals
    



def main():
    create_db_and_tables()


if __name__ == "__main__":
    main()