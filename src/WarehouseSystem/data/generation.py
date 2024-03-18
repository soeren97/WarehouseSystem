"""Generate fake data."""

import random
from typing import Any, Generator

from WarehouseSystem.constants import fake, transactions_types


class FakeData:
    """Fake data generator class."""

    def __init__(self, num_items: int, num_transactions: int) -> None:
        """Initialize class.

        Args:
            num_items (int): Number of items.
            num_transactions (int): Number of transactions.
        """
        self.num_items = num_items
        self.num_transactions = num_transactions

    def get_random_item_id(self) -> int:
        """Get a random item ID from all available items.

        Returns:
            int: Random item ID.
        """
        # Generate a random item ID within the range of available item IDs
        random_item_id = random.randint(1, self.num_items)

        return random_item_id

    def fake_items(self) -> Generator[dict[str, Any], None, None]:
        """Generate fake item.

        Returns:
            Generator[dict[str, Any], None, None]: Fake item.
        """
        for _ in range(self.num_items):
            yield {
                "name": fake.word(),
                "description": fake.text(),
                "price": round(random.random() * 100, 2),
                "number_in_stock": random.randint(0, 100),
                "category_id": random.randint(0, 4),
            }

    def fake_transaction(self) -> Generator[dict[str, Any], None, None]:
        """Generate fake transaction.

        Returns:
            Generator[dict[str, Any], None, None]: Fake transaction.
        """
        for _ in range(self.num_transactions):
            yield {
                "item_id": self.get_random_item_id(),
                "timestamp": fake.date_time_this_decade(),
                "quantity": random.randint(1, 10),
                "type": random.choice(transactions_types),
            }

    def generate_dataset(
        self,
    ) -> tuple[
        Generator[dict[str, Any], None, None],
        Generator[dict[str, Any], None, None],
    ]:
        """Generate fake items and transactions.

        Returns:
            tuple[ Generator[dict[str, Any], None, None],
            Generator[dict[str, Any], None, None], ]:
            Fake items and transactions.
        """
        return self.fake_items(), self.fake_transaction()
