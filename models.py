'''

Author: James Lakis

Date (started): Jul 20, 2023

'''

from typing import Optional

from sqlmodel import Field, SQLModel

from datetime import datetime


'''
class HeroBase(SQLModel):
    name: str = Field(index = True)
    secret_name : str
    age: Optional[int] = Field(default = None, index = True)


class Hero(HeroBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


### Data Models classes, assignees for response_model: HeroCreate and HeroRead are essentially for use by response_model for data validation purposes.
class HeroCreate(HeroBase):
    pass


class HeroRead(HeroBase):
    id: int
### END - Data Models classes
'''


class AnimalsBase(SQLModel):
    date_observed: datetime
    date_posted: datetime
    witness_first_name: str
    witness_second_name: str
    animal_general_name: str
    animal_genus_name: Optional[str] = None
    animal_species_name: Optional[str] = None
    number_observed: Optional[int] = 1
    
class Animals(AnimalsBase, table = True):
    id: Optional[int] = Field(default = None, primary_key = True)
    
class AnimalsCreate(AnimalsBase):
    pass

class AnimalsRead(AnimalsBase):
    id: int


''' # Original "working" data table model

class Animals(SQLModel, table = True):
    id: Optional[int] = Field(default = None, primary_key = True)
    date_observed: datetime
    date_posted: datetime
    witness_first_name: str
    witness_second_name: str
    animal_general_name: str
    animal_genus_name: Optional[str] = None
    animal_species_name: Optional[str] = None
    number_observed: Optional[int] = 1
    
    #images_id: Optional[int] = Field(default=None, foreign_key="images.id")
'''


'''

class Images (SQLModel, table = True):
    id: Optional[int] = Field(default = None, primary_key = True)
    image_type: str
'''