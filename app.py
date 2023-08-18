'''

Author: James Lakis

Date (started): Jul 23, 2023

Inspired by: SqlModel - Code Structure and Multiple Files
https://sqlmodel.tiangolo.com/tutorial/code-structure/


'''


from typing import List

from sqlmodel import Session, select
from fastapi import FastAPI

# app modules
from database import create_db_and_tables
from models import Animal, AnimalCreate, AnimalRead, Image, ImageCreate, ImageRead
from engine import engine


app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()
    

##### Routes #####
    

@app.get("/")
async def root():
    return {"message": "Hello World!"}


@app.post("/animals/", response_model = AnimalRead)
def create_animal(animal : AnimalCreate):
    with Session(engine) as session:
        animal = Animal.from_orm(animal)
        session.add(animal)
        session.commit()
        session.refresh(animal)
        return animal


@app.get("/animals", response_model = List[AnimalRead])
def read_animals():
    with Session(engine) as session:
        animals = session.exec(select(Animal)).all()
    return animals


@app.post("/images/", response_model = ImageRead)
def create_image(image : ImageCreate):
    with Session(engine) as session:
        image = Image.from_orm(image)
        session.add(image)
        session.commit()
        session.refresh(image)
        return image


@app.get("/images", response_model = List[ImageRead])
def read_images():
    with Session(engine) as session:
        image = session.exec(select(Image)).all()
    return image


def main():
    create_db_and_tables()


if __name__ == "__main__":
    main()