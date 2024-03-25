"""Search transactions menu."""

from WarehouseSystem.constants import loghandler
from WarehouseSystem.userInteraction.menu import MenuBuilder


class LogMenu(MenuBuilder):
    """Child class of MenuBuilder with log options."""

    def __init__(self) -> None:
        """Initialize class with specific search options."""
        menu_options = {
            "1": ("Show item log", self.show_items),
            "2": ("Show transaction log", self.show_transactions),
            "3": ("Show entire log", self.show_all),
            "4": ("Back to main menu", self.return_to_main_menu),
        }
        super().__init__(menu_options)

    def show_items(self) -> None:
        """Perform action for showing item log."""
        self.clear_terminal()
        print("You selected show item log.")
        loghandler.display_log("Items")

        input("Press Enter to return to the log menu...")

    def show_transactions(self) -> None:
        """Perform action for showing transaction log."""
        self.clear_terminal()
        print("You selected show transaction log.")
        loghandler.display_log("Transactions")

        input("Press Enter to return to the log menu...")

    def show_all(self) -> None:
        """Preform action for showning entire log."""
        self.clear_terminal()
        print("You selected show entire log.")
        loghandler.display_log("System")

        input("Press Enter to return to the log menu...")
