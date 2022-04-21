
import uuid
from typing import List

from plum_bank.model.account import Account
from plum_bank.model.user import User
from plum_bank.repository.user_repository import UserRepository


class AccountService:
    repository: UserRepository

    def __init__(self) -> None:
        self.repository = UserRepository()

    def get_user(self, user_id: uuid) -> User:
        return self.repository.find_by_id(user_id)

    def get_balances(self, user_id: uuid) -> List[Account]:
        return self.get_user(user_id).accounts

    def get_account(self, account_id: uuid) -> Account:
        return self.repository.find_account_by_id(account_id)

    def create_account(self, user_id: uuid, deposit: float) -> None:
        user = self.repository.find_by_id(user_id)
        account = Account(deposit)
        user.accounts.append(account)

    def transfer(self, from_id: uuid, to_id: uuid, amount: float) -> None:
        from_acc = self.get_account(from_id)
        to_acc = self.get_account(to_id)

        if amount < 0:
            raise ValueError("Amount must not be negative")
        if from_acc.balance - amount < 0:
            raise ValueError(f"Insufficient balance on account with id:{from_acc.id}")

        from_acc.balance = from_acc.balance - amount
        to_acc.balance = to_acc.balance + amount
