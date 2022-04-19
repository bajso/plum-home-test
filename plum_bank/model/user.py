import uuid
from dataclasses import dataclass
from typing import List

from plum_bank.model.account import Account


@dataclass
class User:
    name: str
    accounts: List[Account]
    id: uuid = uuid.uuid4()

    def __init__(self, name: str) -> None:
        if not isinstance(name, str):
            raise TypeError(f"Expecting type str but received {type(name)}")
        self.name = name
        self.accounts = []

    def add_account(self, account: Account) -> None:
        self.accounts.append(account)
