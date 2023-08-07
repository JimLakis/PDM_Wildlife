'''

Author: James Lakis

Date: Jul 23, 2023

Inspired by: SqlModel - Code Structure and Multiple Files
https://sqlmodel.tiangolo.com/tutorial/code-structure/

'''

'''
# Imports taken from FastAPI Tutorials

from typing import List, Optional # <-- List to validate GET output as a list

from fastapi import FastAPI
from sqlmodel import Field, Session, SQLModel, create_engine, select

'''

from typing import List

from sqlmodel import Session, select
from fastapi import FastAPI

# app modules
from database import create_db_and_tables
from models import Animals, AnimalsCreate, AnimalsRead #, AnimalsBase 
from engine import engine


app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()
    

##### Routes #####
    

'''


@app.post("/heroes/", response_model=HeroRead) # Recall argument Pydantic's reponse_model is used for data validation purposes. Here the HeroRead class (including the id primary key) is referenced.
def create_hero(hero: HeroCreate): # Similar class to HeroRead used for type-hinting less id is utilized. The underlying table's id column does not need to be included here since the database populates this field.
    with Session(engine) as session:
        hero = Hero.from_orm(hero) # Here a new Hero model is created in memory w/o the need to provide the id
        session.add(hero)
        session.commit()
        session.refresh(hero)
        return hero


@app.get("/heroes/", response_model=List[HeroRead]) # response_model defines (validates) the reponse as a list containing columns defined by HeroRead class, note: Hero.id is included.
def read_heroes():
    with Session(engine) as session:
        heroes = session.exec(select(Hero)).all()
        return heroes

'''


@app.get("/")
async def root():
    return {"message": "Hello World!"}


@app.post("/animals/", response_model = AnimalsRead)
def create_animals(animals : AnimalsCreate):
    with Session(engine) as session:
        animals = Animals.from_orm(animals)
        session.add(animals)
        session.commit()
        session.refresh(animals)
        return animals


@app.get("/animals", response_model = List[AnimalsRead])
def read_animals():
    with Session(engine) as session:
        animals = session.exec(select(Animals)).all()
    return animals


''' # Original "working" route/path operations...

@app.post("/animals/", response_model = Animals) # <-- add response_model
def create_animal(animal: Animals):
    with Session(engine) as session:
        session.add(animal)
        session.commit()
        session.refresh(animal)
        return animal


@app.get("/animals/", response_model = List[Animals]) # <-- add response_model
def read_animals():
    with Session(engine) as session:
        animals = session.exec(select(Animals)).all()
        return animals
        
'''


def main():
    create_db_and_tables()


if __name__ == "__main__":
    main()