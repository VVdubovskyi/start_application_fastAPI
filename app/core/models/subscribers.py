
from sqlalchemy import Column, Integer

from core.models import Base
from sqlalchemy.orm import Mapped, mapped_column


class Subscriber(Base):
    username: Mapped[str] = mapped_column(unique=True)

