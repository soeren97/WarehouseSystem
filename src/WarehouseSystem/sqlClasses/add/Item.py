"""Add items class."""

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

    def exist_in_database(self, item_name: str) -> Item | None:
        """Item exists in database.

        Args:
            item_name (str): Item name.

        Returns:
            Item | None: Item from database.
        """
        item = self.session.query(Item).filter(Item.name == item_name).first()

        return item

    def add_item(
        self,
        item_name: str,
        item_description: str,
        item_price: float,
        quantity: int,
        category: int,
    ) -> None:
        """Add item to the database."""
        item = self.exist_in_database(item_name)
        if item:
            print("Item already in database adding to number in stock.")
            item.number_in_stock += quantity
        else:
            item = Item(
                name=item_name,
                description=item_description,
                price=item_price,
                number_in_stock=quantity,
                category_id=category,
            )
            self.session.add(item)

        self.session.commit()
