"""Id search stradegy."""

from typing import Any

from sqlalchemy.orm import Session

from WarehouseSystem.sqlClasses.search.transactions.Base import SearchStrategy
from WarehouseSystem.sqlClasses.Transactions import Transaction


class IDSearch(SearchStrategy):
    """Search by title."""

    def search(
        self,
        query: str,
    ) -> Any:
        """Search by ID.

        Args:
            session (Session): SQL session.
            query (str): ID.

        Returns:
            Any: Search results.
        """
        transactions = (
            self.session.query(Transaction)
            .filter(Transaction.id.like(f"%{query}%"))
            .all()
        )

        return transactions
