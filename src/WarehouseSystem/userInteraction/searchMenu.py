"""Search menu."""

from WarehouseSystem.userInteraction.menu import MenuBuilder
from WarehouseSystem.userInteraction.searchItems import SearchItemsMenu
from WarehouseSystem.userInteraction.searchTransactions import SearchTransactionsMenu


class SearchMenu(MenuBuilder):
    """Child class of MenuBuilder with search options."""

    def __init__(self) -> None:
        """Initialize class with specific search options."""
        menu_options = {
            "1": ("Search Transactions", self.search_transactions),
            "2": ("Search Items", self.search_items),
            "3": ("Back to main menu", self.return_to_main_menu),
        }
        super().__init__(menu_options)

    def search_transactions(self) -> None:
        """Perform action for searching transactions."""
        self.clear_terminal()
        print("You selected Search Transactions.")
        transaction_search = SearchTransactionsMenu()
        transaction_search.run()

    def search_items(self) -> None:
        """Perform action for searching items."""
        self.clear_terminal()
        print("You selected search items.")
        item_search = SearchItemsMenu()
        item_search.run()
