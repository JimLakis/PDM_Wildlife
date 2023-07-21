'''

Author: James Lakis

Date: Jul 20, 2023

'''

from typing import Optional

from sqlmodel import Field, SQLModel, create_engine

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


sqlite_file_name = "animals_db.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
engine = create_engine(sqlite_url, echo = True)
SQLModel.metadata.create_all(engine)