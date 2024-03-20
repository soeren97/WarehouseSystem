"""Category logic."""

from sqlalchemy import BIGINT, Column, String
from sqlalchemy.orm import relationship

from WarehouseSystem.constants import Base


class Category(Base):  # type: ignore
    """Category entity in warehouse database."""

    __tablename__ = "categories"

    id = Column(BIGINT, primary_key=True)
    name = Column(String(255))
    description = Column(String(255))

    items = relationship("Item", back_populates="category")
