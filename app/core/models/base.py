from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase, declared_attr, declarative_base
from sqlalchemy.orm import Mapped, mapped_column

from core.config import settings


class Base(DeclarativeBase):
    __abstract__ = True

    metadata = MetaData(
        naming_convention=settings.db.naming_conventions
    )

    @declared_attr
    def __tablename__(self) -> str:
        return f"{self.__name__.lower()}s"

    id: Mapped[int] = mapped_column(primary_key=True)
