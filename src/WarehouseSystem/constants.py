"""Constant variables used throughout the repocetory."""

import pandas as pd
from faker import Faker
from sqlalchemy.ext.declarative import declarative_base

from WarehouseSystem.logging.LogHandler import LogHandler

logs = ["System", "Items", "Transactions"]

loghandler = LogHandler()
for log_name in logs:
    loghandler.init_logger(log_name)

Base = declarative_base()

fake = Faker()

transactions_types = [
    "Sale",
    "Purchace",
    "Return",
]

categories_table = pd.DataFrame(
    {
        # "id": [0, 1, 2, 3, 4],
        "name": [
            "type1",
            "type2",
            "type3",
            "type4",
            "type5",
        ],
        "description": [
            "Type1 ware",
            "Type2 ware",
            "Type3 ware",
            "Type4 ware",
            "Type5 ware",
        ],
    }
)

if __name__ == "__main__":
    pass
