"""Category logic."""

from sqlalchemy import BIGINT, Column, String
from sqlalchemy.orm import relationship

from WarehouseSystem.constants import Base


class Category(Base):
    """Category entity in warehouse database."""

    __tablename__ = "categories"

    id = Column(BIGINT, primary_key=True, autoincrement=True)
    name = Column(String(255))
    description = Column(String(255))

    items = relationship("Item", back_populates="category")

    def __init__(self, name: str, description: str) -> None:
        """Initialize class.

        Args:
            name (str): Name of category.
            description (str): Description of category.
        """
        self.name = name
        self.description = description

    def return_values(self) -> str:
        """Return all values of category.

        Returns:
            str: Values.
        """
        return f"Name: {self.name}, Description: {self.description}."
