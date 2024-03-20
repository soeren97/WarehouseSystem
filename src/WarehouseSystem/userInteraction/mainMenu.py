"""Main menu for TUI."""

from WarehouseSystem.sqlClasses.Items import Item
from WarehouseSystem.userInteraction.menu import MenuBuilder
from WarehouseSystem.userInteraction.searchMenu import SearchMenu


class TerminalMenu(MenuBuilder):
    """Child class of MenuBuilder with specific options."""

    def __init__(self) -> None:
        """Initialize class with specific menu options."""
        menu_options = {
            "1": ("Search", self.search),
            "2": ("Add data", self.add_data),
            "3": ("Create fake dataset", self.create_dataset),
            "4": ("Exit", self.exit_program),
        }
        super().__init__(menu_options)

    def search(self) -> None:
        """Perform search action."""
        self.clear_terminal()
        print("You selected search.")
        search_menu = SearchMenu()
        search_menu.run()

    def add_data(self) -> None:
        """Add data to database."""
        self.clear_terminal()
        print("You selected Option 2.")
        input("Press Enter to return to the main menu...")

    def create_dataset(self) -> None:
        """Create fake dataset."""
        self.clear_terminal()
        if self.connection.is_table_empty(Item):
            print("You selected created a fake dataset.")
            num_items = input("Enter number of items: ")
            num_transactions = input("Enter number of transactions: ")
            self.connection.create_fake_dataset(num_items, num_transactions)
            self.clear_terminal()
        else:
            print("Data already in server.")
            print("If you want to add more use the add data option.")
        input("Press Enter to return to the main menu...")
