"""Terminal based menu for user interaction."""

import os

from WarehouseSystem.sqlClasses.connection import SQLConnection
from WarehouseSystem.sqlClasses.items import Item
from WarehouseSystem.utils import ConfigManager


class TerminalMenu:
    """Terminal based menu for user interaction."""

    def __init__(self) -> None:
        """Initialize class."""
        self.menu_options = {
            "1": self.option1,
            "2": self.option2,
            "3": self.option3,
            "4": self.exit_program,
        }
        config_manager = ConfigManager("config.json")

        self.connection = SQLConnection(
            config_manager.username(), config_manager.password()
        )
        self.clear_terminal()

    def display_menu(self) -> None:
        """Display main menu."""
        print("Welcome to the Terminal Menu!")
        print("1. Search")
        print("2. Option 2")
        print("3. Create fake dataset")
        print("4. Exit")

    def get_user_choice(self) -> str:
        """Get input from user.

        Returns:
            str: User input.
        """
        choice = input("Enter your choice: ")
        return choice.strip()

    def run(self) -> None:
        """Run the TerminalMenu."""
        while True:
            self.display_menu()
            choice = self.get_user_choice()

            if choice in self.menu_options:
                self.menu_options[choice]()
                self.clear_terminal()
            else:
                print("Invalid choice. Please try again.")

    def option1(self) -> None:
        """Perform action for Option 1."""
        self.clear_terminal()
        print("You selected Option 1.")
        input("Press Enter to return to the main menu...")

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
            print("If you want to add more use the option add data.")

        input("Press Enter to return to the main menu...")

    def exit_program(self) -> None:
        """Exit the program."""
        self.clear_terminal()
        print("Exiting the program.")
        exit()

    @staticmethod
    def clear_terminal() -> None:
        """Clear the terminal."""
        os.system("cls" if os.name == "nt" else "clear")


if __name__ == "__main__":
    pass
