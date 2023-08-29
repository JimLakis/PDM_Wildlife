'''

Author: James Lakis

Date (started): Jul 20, 2023

Notes:

    1. The order in the classes below is important. The dependent Image data model class needs to be defined at the top of the file before the independent Animal data model class.
    2. In the type definitions of the relationship attributes, example - animals: List["Animal"], it's important that the class name "Animal" be a string and not passed as the class defintion Animal w/o quotes. This is a form of Forward Reference.

'''

from typing import Optional, List

from sqlmodel import Field, SQLModel, Relationship

from datetime import datetime


class ImageBase(SQLModel):
    image_type: str

class Image(ImageBase, table = True):
    id: Optional[int] = Field(default = None, primary_key = True)
    animals: List["Animal"] = Relationship(back_populates="image")

class ImageCreate(ImageBase):
    pass

class ImageRead(ImageBase):
    id: int


class AnimalBase(SQLModel):
    date_observed: datetime
    date_posted: datetime
    witness_first_name: str
    witness_second_name: str
    animal_general_name: str
    animal_genus_name: Optional[str] = None
    animal_species_name: Optional[str] = None
    number_observed: Optional[int] = 1
    
class Animal(AnimalBase, table = True):
    id: Optional[int] = Field(default = None, primary_key = True)
    image_id: Optional[int] = Field(default=None, foreign_key="image.id")
    image: Optional["Image"] = Relationship(back_populates="animals")
    
class AnimalCreate(AnimalBase):
    pass

class AnimalRead(AnimalBase):
    id: int