import pytest
from plum_bank.exceptions.account_not_found import AccountNotFoundException
from plum_bank.exceptions.user_not_found_exception import UserNotFoundException
from plum_bank.model.account import Account
from plum_bank.model.user import User
from plum_bank.repository.user_repository import UserRepository


class TestUserRepository:
    def test_create_repository(self):
        repo = UserRepository()
        assert len(repo.users) == 4

    def test_find_by_id(self):
        _id = '572ac805-aea8-4039-aaac-ee028e97b827'
        repo = UserRepository()
        user = repo.find_by_id(_id)
        assert isinstance(user, User)

    def test_find_by_id_not_found(self):
        _id = '1'
        repo = UserRepository()
        with pytest.raises(UserNotFoundException):
            repo.find_by_id(_id)

    def test_find_account_by_id(self):
        acc_id = '1'
        repo = UserRepository()
        account = repo.find_account_by_id(acc_id)
        assert isinstance(account, Account)

    def test_find_account_by_id_not_found(self):
        acc_id = '10'
        repo = UserRepository()
        with pytest.raises(AccountNotFoundException):
            repo.find_account_by_id(acc_id)
