import pytest
from plum_bank.model.account import Account
from plum_bank.model.user import User


class TestUser:
    def test_create_user(self):
        user = User("Adam")
        assert user.name == "Adam"
        assert len(user.accounts) == 0
        assert user.id is not None

    def test_create_user_with_int_name(self):
        with pytest.raises(TypeError):
            User(1)

    def test_add_account(self):
        user = User("Adam")
        user.accounts = [Account(100.0)]
        account = Account(200.0)
        user.add_account(account)
        assert filter(lambda x: x.id == account.id, user.accounts) is not None
