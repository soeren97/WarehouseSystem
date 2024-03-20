"""Main menu for TUI."""

from WarehouseSystem.sqlClasses.Items import Item
from WarehouseSystem.userInteraction.menu import MenuBuilder
from WarehouseSystem.userInteraction.searchMenu import SearchMenu


class TerminalMenu(MenuBuilder):
    """Child class of MenuBuilder with specific options."""

    def __init__(self) -> None:
        """Initialize class with specific menu options."""
        menu_options = {
            "1": ("Search", self.option1),
            "2": ("Option 2", self.option2),
            "3": ("Create fake dataset", self.option3),
            "4": ("Exit", self.exit_program),
        }
        super().__init__(menu_options)

    def option1(self) -> None:
        """Perform action for Option 1."""
        self.clear_terminal()
        print("You selected search.")
        search_menu = SearchMenu()
        search_menu.run()

    def option2(self) -> None:
        """Perform action for Option 2."""
        self.clear_terminal()
        print("You selected Option 2.")
        input("Press Enter to return to the main menu...")

    def option3(self) -> None:
        """Perform action for Option 3."""
        self.clear_terminal()
        if self.connection.is_table_empty(Item):
            print("You selected created a fake dataset.")
            num_items = input("Enter number of items: ")
            num_transactions = input("Enter number of transactions: ")
            self.connection.create_fake_dataset(num_items, num_transactions)
            self.clear_terminal()
        else:
            print("Data already in server.")
            print("If you want to add more use the option add data option.")
        input("Press Enter to return to the main menu...")
