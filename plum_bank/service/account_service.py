
import uuid

from plum_bank.model.account import Account
from plum_bank.model.user import User
from plum_bank.repository.user_repository import UserRepository


class AccountService:
    repository: UserRepository

    def __init__(self) -> None:
        self.repository = UserRepository()

    def get_user(self, user_id: uuid) -> User:
        return self.repository.find_by_id(user_id)

    def create_account(self, user_id: uuid, deposit: float) -> None:
        user = self.repository.find_by_id(user_id)
        account = Account(deposit)
        user.accounts.append(account)
