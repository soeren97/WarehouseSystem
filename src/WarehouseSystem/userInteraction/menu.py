"""Terminal based menu for user interaction."""

import os
from typing import Any

from WarehouseSystem.sqlClasses.connection import SQLConnection
from WarehouseSystem.utils import ConfigManager


class MenuBuilder:
    """Parent class to build a terminal-based menu for user interaction."""

    def __init__(self, menu_options: dict[str, Any]) -> None:
        """Initialize class with menu options."""
        self.menu_options = menu_options
        config_manager = ConfigManager("config.json")
        self.connection = SQLConnection(
            config_manager.username(), config_manager.password()
        )
        self.clear_terminal()

    def display_menu(self) -> None:
        """Display main menu."""
        print("Welcome to the Terminal Menu!")
        for key, value in self.menu_options.items():
            print(f"{key}. {value[0]}")

    def get_user_choice(self) -> str:
        """Get input from user."""
        choice = input("Enter your choice: ").strip()
        return choice

    def run(self) -> None:
        """Run the menu."""
        while True:
            self.display_menu()
            choice = self.get_user_choice()

            if choice in self.menu_options:
                return_to_main = self.menu_options[choice][1]()
                if return_to_main:
                    break  # Exit the loop if return_to_main is True
                self.clear_terminal()
            else:
                print("Invalid choice. Please try again.")

    def clear_terminal(self) -> None:
        """Clear the terminal."""
        os.system("cls" if os.name == "nt" else "clear")

    def return_to_main_menu(self) -> bool:
        """Return to the main menu."""
        self.clear_terminal()
        print("Returning to the main menu.")
        return True

    def exit_program(self) -> None:
        """Exit the program."""
        self.clear_terminal()
        self.connection.session.close()
        print("Exiting the program.")
        exit()


if __name__ == "__main__":
    pass
