'''

Author: James Lakis

Date (started): Jul 20, 2023

'''

from typing import Optional

from sqlmodel import Field, SQLModel

from datetime import datetime


class AnimalBase(SQLModel):
    date_observed: datetime
    date_posted: datetime
    witness_first_name: str
    witness_second_name: str
    animal_general_name: str
    animal_genus_name: Optional[str] = None
    animal_species_name: Optional[str] = None
    number_observed: Optional[int] = 1
    
class Animals(AnimalBase, table = True):
    id: Optional[int] = Field(default = None, primary_key = True)
    #images_id: Optional[int] = Field(default=None, foreign_key="images.id")
    
class AnimalCreate(AnimalBase):
    pass

class AnimalsRead(AnimalBase):
    id: int


'''

class Images (SQLModel, table = True):
    id: Optional[int] = Field(default = None, primary_key = True)
    image_type: str
'''

class ImageBase(SQLModel):
    image_type: str

class Images(ImageBase, table = True):
    id: Optional[int] = Field(default = None, primary_key = True)

class ImageCreate(ImageBase):
    pass

class ImagesRead(AnimalBase):
    id: int