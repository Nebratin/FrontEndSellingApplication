import datetime

import sqlalchemy
from sqlalchemy import  create_engine
from databaseMeta import Produs, Base, Bon
from sqlalchemy.orm import Session

class Database:

    def __init__(self,databaseName):
        self.engine = create_engine("sqlite+pysqlite:///"+databaseName, echo=True)
        self.produs = Produs()
        self.base = Base()
        self.base.metadata.create_all(self.engine)


    def add_item(self, item):
        with Session(self.engine) as session:
            session.add(item)
            session.commit()

    def get_items(self, tableName, **kwargs):
        with Session(self.engine) as session:
            if kwargs:
                if kwargs["columnName"]  and kwargs["columnValue"]:
                    return session.execute(sqlalchemy.Select(tableName).where(getattr(tableName, kwargs["columnName"]) == kwargs["columnValue"])).scalars().all()
            return session.execute(sqlalchemy.Select(tableName)).scalars().all()

    def delete_item(self, tableName, **kwargs):
        with Session(self.engine) as session:
            if kwargs:
                if kwargs["columnName"] and kwargs["columnValue"]:
                    session.execute(sqlalchemy.delete(tableName).where(getattr(tableName, kwargs["columnName"]) == kwargs["columnValue"]))
                    session.commit()
                if "idValue" in kwargs:
                    session.execute(sqlalchemy.delete(tableName).where(getattr(tableName, id) == kwargs["idValue"]))
                    session.commit()

db = Database("newDB.db")
# pr = Produs(denumire="Carne Tocata Amestec", pret = 19.56, cota_TVA = 9, PLU=20)
# db.add_item(pr)

# result = db.get_items(Produs, columnName="pret", columnValue=14.56)
# print(result)
# result = db.get_items(Produs, columnName="denumire", columnValue="Salam")
# print(result)
# result = db.get_items(Produs)
# print(result)
#
# db.delete_item(Produs, columnName="pret", columnValue=16)

# bon = Bon(cod_datecs="D234532342", data=datetime.datetime.now())
# db.add_item(bon)
result = db.get_items(Bon, columnName="cod_datecs", columnValue="D234532342")
print(result)