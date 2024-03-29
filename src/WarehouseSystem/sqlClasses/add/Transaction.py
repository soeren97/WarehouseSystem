"""Add transaction class."""

from datetime import datetime
from typing import Optional

from sqlalchemy.orm import Session

from WarehouseSystem.constants import transactions_types
from WarehouseSystem.logging.logging import logger_wrapper_transactions
from WarehouseSystem.sqlClasses.add.Item import ItemAdder
from WarehouseSystem.sqlClasses.Items import Item
from WarehouseSystem.sqlClasses.Transactions import Transaction


class TransactionAdder:
    """Class to add transactions."""

    def __init__(self, session: Session):
        """Initialize class.

        Args:
            session (Session): Connection to SQL server.
        """
        self.session = session
        self.timestamp = datetime.now()
        self.item_id: Optional[int]
        self.quantity: Optional[int]
        self.transaction_type: Optional[str]
        self.type: int = 0

    def exist_in_database(self) -> Optional[Item]:
        """Item exists in database.

        Returns:
            Optional[Item]: Item from database.
        """
        item = (
            self.session.query(Item).filter(Transaction.item_id == self.item_id).first()
        )

        return item

    def get_input(self) -> None:
        """Get input from user."""
        while True:
            try:
                self.item_id = int(input("Please input item ID: "))
                self.quantity = int(input("Please input quantity of items: "))
                while self.type not in range(1, len(transactions_types) + 1):
                    self.type = int(
                        input(
                            "Please input type of transaction"
                            "(1: Sale, 2: Purchace, 3: Return): "
                        )
                    )
                break  # Break out of the loop if all inputs are valid
            except ValueError:
                print(
                    "Invalid input. "
                    "Please enter a valid number for item ID, quantity and type."
                )

    @logger_wrapper_transactions  # type: ignore
    def add_transaction(self) -> Optional[Transaction]:
        """Add transaction to the database.

        Returns:
            Optional[Transaction]: Transaction object.
        """
        item = self.exist_in_database()
        self.transaction_type = transactions_types[self.type - 1]
        if item:
            print("Item in database.")
            if self.transaction_type == "Sale":
                if item.number_in_stock >= self.quantity:
                    item.number_in_stock -= self.quantity
                else:
                    print("Not enough items to sell, transaction not made.")
                    return None
            else:
                item.number_in_stock += self.quantity
            self.session.add(item)

        else:
            print("Item does not exist, please add it to database.")
            item_adder = ItemAdder(self.session)
            item_adder.get_input()
            item_adder.add_item()

        transaction = Transaction(
            self.item_id,
            self.timestamp,
            self.quantity,
            self.transaction_type,
        )
        self.session.add(transaction)
        self.session.commit()

        return transaction
