"""Log functionality."""

import logging
from typing import Any, Callable

from WarehouseSystem.sqlClasses.Categories import Category
from WarehouseSystem.sqlClasses.Items import Item
from WarehouseSystem.sqlClasses.Transactions import Transaction


def logger_wrapper_transactions(
    func: Callable[..., Transaction]
) -> Callable[..., None]:
    """Wrap a function with logging functionality.

    Args:
        func (Callable[..., Transaction]): The function to be wrapped.

    Returns:
        Callable[[], None]: The wrapper function.
    """

    def wrapper(self: Any) -> None:
        """Log functionality."""
        # Initialize loggers
        transaction_logger = logging.getLogger("Transactions")
        system_logger = logging.getLogger("System")

        transaction_logger.setLevel(logging.INFO)
        system_logger.setLevel(logging.INFO)

        transaction = func(self)

        if transaction:
            transaction_logger.info(
                f"Adding transaction: ID: {transaction.id}, "
                f"{transaction.return_values()}."
            )
            system_logger.info(
                f"Adding transaction: ID: {transaction.id}, "
                f"{transaction.return_values()}."
            )
        else:
            transaction_logger.info("Transaction failed.")
            system_logger.info("Transaction failed.")

    return wrapper


def logger_wrapper_items(func: Callable[..., Item]) -> Callable[..., None]:
    """Wrap a function with logging functionality.

    Args:
        func (Callable[..., Item]): The function to be wrapped.

    Returns:
        Callable[[], None]: The wrapper function.
    """

    def wrapper(self: Any) -> None:
        """Log functionality."""
        # Initialize loggers
        item_logger = logging.getLogger("Items")
        system_logger = logging.getLogger("System")

        item_logger.setLevel(logging.INFO)
        system_logger.setLevel(logging.INFO)

        item = func(self)

        # Log function call
        item_logger.info(
            f"Adding item: ID: {item.id}, "
            f"{item.return_values()}, "
            f"Category: {item.category.name}."
        )
        system_logger.info(
            f"Adding item: ID: {item.id}, "
            f"{item.return_values()}, "
            f"Category: {item.category.name}."
        )

    return wrapper


def logger_wrapper_category(func: Callable[..., Category]) -> Callable[..., None]:
    """Wrap a function with logging functionality.

    Args:
        func (Callable[..., Category]): The function to be wrapped.

    Returns:
        Callable[[], None]: The wrapper function.
    """

    def wrapper(self: Any) -> None:
        """Log functionality."""
        # Initialize loggers
        category_logger = logging.getLogger("Categories")
        system_logger = logging.getLogger("System")

        category_logger.setLevel(logging.INFO)
        system_logger.setLevel(logging.INFO)

        category = func(self)

        # Log function call
        category_logger.info(
            f"Adding category: ID: {category.id}, {category.return_values()}."
        )
        system_logger.info(
            f"Adding category: ID: {category.id}, {category.return_values()}."
        )

    return wrapper
