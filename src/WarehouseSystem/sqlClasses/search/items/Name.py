"""Search stradegy to search items by name."""

from typing import Any

from WarehouseSystem.sqlClasses.Items import Item
from WarehouseSystem.sqlClasses.search.items.Base import SearchStrategy


class NameSearch(SearchStrategy):
    """Search by name."""

    def search(self, query: str) -> Any:
        """Search by name.

        Args:
            query (str): Name of item.

        Returns:
            Any: Search results.
        """
        items = self.session.query(Item).filter(Item.name.like(f"%{query}%")).all()
        return items
