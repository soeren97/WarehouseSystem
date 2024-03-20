"""Base search stradegy class for transactions."""

from WarehouseSystem.sqlClasses.Transactions import Transaction


class SearchStrategy:
    """Base class for search strategies."""

    def search(
        self,
        transactions: list[type[Transaction]],
        query: str,
    ) -> list[Transaction]:
        """Catch not implimented strategies.

        Args:
            books (list[type[Book]]): Books.
            query (str): Query to find books.

        Raises:
            NotImplementedError: strategies not implimented.

        Yields:
            Generator[type[Book], None, None]: Found books.
        """
        raise NotImplementedError()
