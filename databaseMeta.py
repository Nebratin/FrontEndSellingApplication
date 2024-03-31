from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import *
from datetime import date


class Base(DeclarativeBase):
    pass


class Produs(Base):
    __tablename__ = "nomenclator_produs"

    id: Mapped[int] = mapped_column(primary_key=True)
    denumire: Mapped[str] = mapped_column(nullable=False, unique=True)
    pret: Mapped[float] = mapped_column(nullable=False)
    cota_TVA: Mapped[int] = mapped_column(nullable=False, default=9)
    PLU: Mapped[int] = mapped_column(nullable=False)
    UM: Mapped[str] = mapped_column(nullable=False, default="kg")

    def __repr__(self) -> str:
        return f"Produs: {self.denumire} cu pretul: {self.pret} si TVA={self.cota_TVA}%  PLU: {self.PLU}  UM: {self.UM}"


class Bon(Base):
    __tablename__ = "bonuri"

    id: Mapped[int] = mapped_column(primary_key=True)
    cod_datecs: Mapped[str] = mapped_column(String(20), unique=True)
    data: Mapped[date] = mapped_column(DateTime)

    def __repr__(self) -> str:
        return f"Bonul: {self.cod_datecs} din data: {self.data}"
