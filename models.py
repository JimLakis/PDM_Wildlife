'''

Author: James Lakis

Date: Jul 20, 2023

'''

from typing import Optional

from sqlmodel import Field, SQLModel

from datetime import datetime


class Animals(SQLModel, table = True):
    id: Optional[int] = Field(default = None, primary_key = True)
    date_observed: datetime
    date_posted: datetime
    witness_first_name: str
    witness_second_name: str
    animal_general_name: str
    aninal_genus_name: Optional[str] = None
    aninal_species_name: Optional[str] = None
    number_observed: Optional[int] = 1
    
    #images_id: Optional[int] = Field(default=None, foreign_key="images.id")
    
'''
class Images (SQLModel, table = True):
    id: Optional[int] = Field(default = None, primary_key = True)
    image_type: str
'''