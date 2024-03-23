"""Add menu."""

from WarehouseSystem.sqlClasses.add.Category import CategoryAdder
from WarehouseSystem.sqlClasses.add.Item import ItemAdder
from WarehouseSystem.sqlClasses.add.Transaction import TransactionAdder
from WarehouseSystem.userInteraction.menu import MenuBuilder


class AddMenu(MenuBuilder):
    """Child class of MenuBuilder with search options."""

    def __init__(self) -> None:
        """Initialize class with specific search options."""
        menu_options = {
            "1": ("Add Transaction", self.add_transaction),
            "2": ("Add Item", self.add_item),
            "3": ("Add Category", self.add_category),
            "4": ("Back to main menu", self.return_to_main_menu),
        }
        super().__init__(menu_options)

    def add_transaction(self) -> None:
        """Perform action for adding transactions."""
        self.clear_terminal()
        print("You selected add transaction.")
        adder = TransactionAdder(self.connection.session)
        adder.get_input()
        adder.add_transaction()
        print("Transaction added.")

    def add_item(self) -> None:
        """Perform action for adding items."""
        self.clear_terminal()
        print("You selected add item.")
        adder = ItemAdder(self.connection.session)
        adder.get_input()
        adder.add_item()
        print("Item added.")

    def add_category(self) -> None:
        """Perform action for adding category."""
        self.clear_terminal()
        print("You selected add category.")
        adder = CategoryAdder(self.connection.session)
        adder.get_input()
        adder.add_category()
        print("Category added.")
