import pytest
from plum_bank.model.account import Account


class TestAccount:
    def test_create_account(self):
        account = Account(100.0)
        assert account.balance == 100.0
        assert account.id is not None

    def test_create_account_without_balance(self):
        account = Account()
        assert account.balance == 0.0
        assert account.id is not None

    def test_create_account_with_str_balance(self):
        with pytest.raises(TypeError):
            Account('meow')

    def test_create_account_with_neg_balance(self):
        with pytest.raises(ValueError):
            Account(-100.0)

    def test_update_balance(self):
        account = Account(100.0)
        account.update_balance(200.0)
        assert account.balance == 200.0
