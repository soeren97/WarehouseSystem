"""Add items class."""

from typing import Optional

from sqlalchemy.orm import Session

from WarehouseSystem.sqlClasses.Items import Item


class ItemAdder:
    """Class to add items."""

    def __init__(self, session: Session):
        """Initialize class.

        Args:
            session (Session): Connection to SQL server.
        """
        self.session = session
        self.name: Optional[str]
        self.description: Optional[str]
        self.price: Optional[float]
        self.quantity: Optional[int]
        self.category: Optional[int]

    def exist_in_database(self) -> Optional[Item]:
        """Item exists in database.

        Returns:
            Optional[Item]: Item from database.
        """
        item = self.session.query(Item).filter(Item.name == self.name).first()

        return item

    def get_input(self) -> None:
        """Get input from user."""
        self.name = input("Please input name of item: ")
        self.description = input("Please input description of item: ")

        while True:
            try:
                self.price = float(input("Please input price of item: "))
                self.quantity = int(input("Please input quantity of item: "))
                self.category = int(input("Please input category of item: "))
                break  # Break out of the loop if all inputs are valid
            except ValueError:
                print(
                    "Invalid input. "
                    "Please enter a valid number for price, quantity, and category."
                )

    def add_item(self) -> None:
        """Add item to the database."""
        item = self.exist_in_database()
        if item:
            print("Item already in database adding to number in stock.")
            item.number_in_stock += self.quantity
        else:
            item = Item(
                self.name,
                self.description,
                self.price,
                self.quantity,
                self.category,
            )
            self.session.add(item)

        self.session.commit()
