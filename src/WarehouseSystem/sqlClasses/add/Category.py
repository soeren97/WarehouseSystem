"""Add categories class."""

from typing import Optional

from sqlalchemy.orm import Session

from WarehouseSystem.sqlClasses.Categories import Category


class CategoryAdder:
    """Class to add categories."""

    def __init__(self, session: Session):
        """Initialize class.

        Args:
            session (Session): Connection to SQL server.
        """
        self.session = session
        self.name: Optional[str]
        self.description: Optional[str]

    def exist_in_database(self) -> Optional[Category]:
        """Item exists in database.

        Returns:
            Optional[Category]: Category from database.
        """
        category = (
            self.session.query(Category).filter(Category.name == self.name).first()
        )

        return category

    def get_input(self) -> None:
        """Get input from user."""
        self.name = input("Please input name of category: ")
        self.description = input("Please input description of category: ")

    def add_category(self) -> None:
        """Add category to database."""
        if self.exist_in_database():
            print("Category already in database, if you wish to alter it go to edit.")
        else:
            category = Category(self.name, self.description)
            self.session.add(category)
            self.session.commit()
