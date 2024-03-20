"""Search transactions menu."""

from WarehouseSystem.sqlClasses.search.transactions.Id import IDSearch
from WarehouseSystem.userInteraction.menu import MenuBuilder


class SearchTransactionsMenu(MenuBuilder):
    """Child class of MenuBuilder with search options."""

    def __init__(self) -> None:
        """Initialize class with specific search options."""
        menu_options = {
            "1": ("Search by ID", self.search_ID),
            "2": ("Search Items", self.search_items),
            "3": ("Back to search menu", self.return_to_main_menu),
        }
        super().__init__(menu_options)

    def search_ID(self) -> None:
        """Perform action for searching by ID."""
        self.clear_terminal()
        print("You selected Search by ID.")

        id_search = IDSearch()
        id = input("Please write ID you want to search for: ")
        transactions = id_search.search(self.connection.session, id)
        if transactions:
            print("Found transactions:")
            for transaction in transactions:
                print(
                    f"ID: {transaction.id}, "
                    f"Item ID: {transaction.item_id}, "
                    f"Timestamp: {transaction.timestamp}, "
                    f"Quantity: {transaction.quantity}, "
                    f"Type: {transaction.type}"
                )
        else:
            print("No transactions found with the provided ID.")
        input("Press Enter to return to the search menu...")

    def search_items(self) -> None:
        """Perform action for searching items."""
        self.clear_terminal()
        print("You selected Search Items.")
        # Add your logic for searching items here
        input("Press Enter to return to the search menu...")
