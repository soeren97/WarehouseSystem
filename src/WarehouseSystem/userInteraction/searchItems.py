"""Search transactions menu."""

from WarehouseSystem.sqlClasses.search.items.Id import IDSearch
from WarehouseSystem.sqlClasses.search.items.Name import NameSearch
from WarehouseSystem.userInteraction.menu import MenuBuilder


class SearchItemsMenu(MenuBuilder):
    """Child class of MenuBuilder with search options."""

    def __init__(self) -> None:
        """Initialize class with specific search options."""
        menu_options = {
            "1": ("Search by ID", self.search_ID),
            "2": ("Search by name", self.search_name),
            "3": ("Back to search menu", self.return_to_main_menu),
        }
        super().__init__(menu_options)

    def search_ID(self) -> None:
        """Perform action for searching by ID."""
        self.clear_terminal()
        print("You selected search by ID.")

        id_search = IDSearch(self.connection.session)
        id = input("Please write the ID you want to search for: ")
        items = id_search.search(id)
        if items:
            print("Found item(s):")
            for item in items:
                self.print_item(item)
        else:
            print("No items found with the provided ID.")
        input("Press Enter to return to the search menu...")

    def search_name(self) -> None:
        """Perform action for searching by name."""
        self.clear_terminal()
        print("You selected search by name.")

        name_search = NameSearch(self.connection.session)
        name = input("Please write the name you want to search for: ")
        items = name_search.search(name)
        if items:
            print("Found item(s):")
            for item in items:
                self.print_item(item)
        else:
            print("No items found with the provided name.")
        input("Press Enter to return to the search menu...")
