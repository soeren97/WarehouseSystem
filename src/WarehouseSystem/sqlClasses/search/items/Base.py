"""Base search stradegy class for items."""

from sqlalchemy.orm import Session

from WarehouseSystem.sqlClasses.Items import Item


class SearchStrategy:
    """Base class for search strategies."""

    def __init__(self, session: Session) -> None:
        """Initialize class.

        Args:
            session (Session): Connection to SQL database.
        """
        self.session = session

    def search(
        self,
        query: str,
    ) -> list[Item]:
        """Catch not implimented strategies.

        Args:
            query (str): Query to find items.

        Raises:
            NotImplementedError: strategies not implimented.

        Yields:
            list[Transactions]
        """
        raise NotImplementedError()
