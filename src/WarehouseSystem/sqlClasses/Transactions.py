"""Transaction logic."""

from datetime import datetime

from sqlalchemy import BIGINT, Column, DateTime, ForeignKey, Integer, String

from WarehouseSystem.constants import Base


class Transaction(Base):
    """Transaction entity in warehouse database."""

    __tablename__ = "transactions"

    id = Column(BIGINT, primary_key=True, autoincrement=True)
    item_id = Column(BIGINT, ForeignKey("items.id"))
    timestamp = Column(DateTime)
    quantity = Column(Integer)
    type = Column(String(255))

    def __init__(
        self,
        item_id: int,
        timestamp: datetime,
        quantity: int,
        type: str,
    ) -> None:
        """Initialize class.

        Args:
            item_id (int): Id of item.
            timestamp (datetime): Time of transaction.
            quantity (int): Number of items.
            type (str): Type of transaction.
        """
        self.item_id = item_id
        self.timestamp = timestamp
        self.quantity = quantity
        self.type = type
