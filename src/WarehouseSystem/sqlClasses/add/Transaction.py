"""Add transaction class."""

from datetime import datetime
from typing import Optional

from sqlalchemy.orm import Session

from WarehouseSystem.constants import transactions_types
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
        self.item_id: Optional[int]
        self.quantity: Optional[int]
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
                while self.type not in range(len(transactions_types) + 1):
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

    def add_transaction(self) -> None:
        """Add transaction to the database."""
        item = self.exist_in_database()
        type = transactions_types[self.type - 1]
        if item:
            print("Item in database.")
            if type == "Sale":
                if item.number_in_stock >= self.quantity:
                    item.number_in_stock -= self.quantity
                else:
                    print("Not enough items to sell, transaction not made.")
                    return
            else:
                item.number_in_stock += self.quantity
            self.session.add(item)

        else:
            print("Item does not exist, please add it to database.")
            item_adder = ItemAdder(self.session)
            item_adder.get_input()
            item_adder.add_item()

        transaction = Transaction(self.item_id, datetime.now(), self.quantity, type)
        self.session.add(transaction)
        self.session.commit()
