'''

Author: James Lakis

Date: Jul 20, 2023

'''

from sqlmodel import SQLModel, create_engine

from models import models


models.Animals()

sqlite_file_name = "animals_db.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
engine = create_engine(sqlite_url, echo = True)
SQLModel.metadata.create_all(engine)