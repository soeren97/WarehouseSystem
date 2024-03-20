"""Functions to handle sql database."""

from typing import Any, Generator, Union

from mysql import connector
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from WarehouseSystem.constants import Base, categories_table
from WarehouseSystem.data.generation import FakeData
from WarehouseSystem.sqlClasses.Categories import Category
from WarehouseSystem.sqlClasses.Items import Item
from WarehouseSystem.sqlClasses.Transactions import Transaction


class SQLConnection:
    """Class to handle sql connection and queries."""

    _instance = None

    def __new__(cls: Any, *args: tuple[Any], **kwargs: tuple[Any]) -> Any:
        """Make sure there is only one instance of this class.

        Args:
            cls (DatabaseConnection): The class of the instance being created.

        Returns:
            DatabaseConnection: The instance of the DatabaseConnection class.
        """
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, username: str, password: str) -> None:
        """Initialize class.

        Args:
            username (str): Username for sql server.
            password (str): Password for sql server.
        """
        self.username = username
        self.password = password
        self.session = self.create_database()

    def create_database(self) -> Session:
        """Create the sql database if not present and connect.

        Returns:
            Session: Connection to sql server.
        """
        connection_mysql = connector.connect(
            host="localhost",
            user=self.username,
            password=self.password,
        )
        cursor = connection_mysql.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS Warehouse")

        # Close the connection
        connection_mysql.close()

        # Now connect to the 'Warehouse' database
        engine = create_engine(
            f"mysql+mysqlconnector://{self.username}:{self.password}"
            "@localhost/Warehouse",
            echo=True,
        )

        # Create categories table
        try:
            categories_table.to_sql("categories", engine, index=True, index_label="id")
        except ValueError:
            # Already have a category table
            pass

        Base.metadata.create_all(engine)

        # Create a sessionmaker bound to the engine
        Session = sessionmaker(bind=engine)

        # Create a session
        session = Session()

        return session

    def upload_data_in_chunks(
        self,
        data: Generator[dict[str, Any], None, None],
        chunk_size: int,
        dataclass: Union[type[Item], type[Transaction], type[Category]],
    ) -> None:
        """Upload data to sql server in chunks.

        Args:
            data (Generator[dict[str, Any], None, None]): Data to be uploaded.
            chunk_size (int): Amount of data uploaded at once.
            dataclass (Union[type[Item], type[Transaction], type[Category]]):
            Type of data being uploadet.
        """
        chunk = []
        for record in data:
            chunk.append(dataclass(**record))
            if len(chunk) >= chunk_size:
                self.session.bulk_save_objects(chunk)
                self.session.commit()
                chunk = []
        if chunk:
            self.session.bulk_save_objects(chunk)
            self.session.commit()

    def is_table_empty(self, table: type[Item]) -> bool:
        """Check if a table is empty.

        Args:
            table (Item): Table to be checked.

        Returns:
            bool: Is table empty.
        """
        # Count the number of rows in the table
        count = self.session.query(table).count()

        # If the count is zero, the table is empty
        return bool(count == 0)

    def create_fake_dataset(self, num_items: int, num_transactions: int) -> None:
        """Create fake data for database."""
        chunk_size = 100
        data_generator = FakeData(num_items, num_transactions)
        items, transactions = data_generator.generate_dataset()
        self.upload_data_in_chunks(items, chunk_size, Item)
        self.upload_data_in_chunks(transactions, chunk_size, Transaction)


if __name__ == "__main__":
    pass
