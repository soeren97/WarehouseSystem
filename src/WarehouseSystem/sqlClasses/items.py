"""Item logic."""

from sqlalchemy import BIGINT, Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from WarehouseSystem.constants import Base


class Item(Base):  # type: ignore
    """Item entity in warehouse database."""

    __tablename__ = "items"

    id = Column(BIGINT, primary_key=True, autoincrement=True)
    name = Column(String(255))
    description = Column(String(255))
    price = Column(Float)
    number_in_stock = Column(Integer)

    category_id = Column(BIGINT, ForeignKey("categories.id"))

    category = relationship("Category", back_populates="items")

    def __init__(
        self,
        # id: int,
        name: str,
        description: str,
        price: float,
        number_in_stock: int,
        category_id: int,
    ) -> None:
        """Initialize class.

        Args:
            name (str): Name of item.
            description (str): Description of item.
            price (float): Price of item.
            number_in_stock (int): Number in stock.
            category (int): Category.
        """
        self.name = name
        self.description = description
        self.price = price
        self.number_in_stock = number_in_stock
        self.category_id = category_id


if __name__ == "__main__":
    pass
