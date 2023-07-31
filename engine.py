'''

Author: James Lakis

Date: Jul 29, 2023


'''


from sqlmodel import create_engine


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, echo=True, connect_args=connect_args) # for production echo is False