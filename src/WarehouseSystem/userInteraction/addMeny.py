"""Add menu."""

from WarehouseSystem.sqlClasses.add.Item import ItemAdder
from WarehouseSystem.userInteraction.menu import MenuBuilder


class AddMenu(MenuBuilder):
    """Child class of MenuBuilder with search options."""

    def __init__(self) -> None:
        """Initialize class with specific search options."""
        menu_options = {
            "1": ("Add Transaction", self.add_transaction),
            "2": ("Add Item", self.add_item),
            "3": ("Back to main menu", self.return_to_main_menu),
        }
        super().__init__(menu_options)

    def add_transaction(self) -> None:
        """Perform action for adding transactions."""
        self.clear_terminal()
        print("You selected add transaction.")

    def add_item(self) -> None:
        """Perform action for adding items."""
        self.clear_terminal()
        print("You selected add Item.")
        adder = ItemAdder(self.connection.session)

        while True:
            name = input("Please input name of item: ")
            description = input("Please input description of item: ")
            try:
                price = float(input("Please input price of item: "))
                quantity = int(input("Please input quantity of item: "))
                category = int(input("Please input category of item: "))
                break  # Break out of the loop if all inputs are valid
            except ValueError:
                print(
                    "Invalid input. "
                    "Please enter a valid number for price, quantity, and category."
                )

        adder.add_item(name, description, price, quantity, category)
        print("Item added.")
        input("Press Enter to return to the search menu...")
