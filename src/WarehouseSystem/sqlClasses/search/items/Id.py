"""Id search stradegy."""

from typing import Any

from WarehouseSystem.sqlClasses.Items import Item
from WarehouseSystem.sqlClasses.search.transactions.Base import SearchStrategy


class IDSearch(SearchStrategy):
    """Search by Id."""

    def search(
        self,
        query: str,
    ) -> Any:
        """Search by ID.

        Args:
            query (str): ID.

        Returns:
            Any: Search results.
        """
        transactions = self.session.query(Item).filter(Item.id.like(f"%{query}%")).all()

        return transactions
