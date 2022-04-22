import pytest
from plum_bank.model.exceptions.account_not_found import AccountNotFoundException
from plum_bank.model.exceptions.user_not_found_exception import UserNotFoundException
from plum_bank.model.account import Account
from plum_bank.model.user import User
from plum_bank.service.account_service import AccountService


class TestAccountService:
    def test_get_user(self):
        user_id = '572ac805-aea8-4039-aaac-ee028e97b827'
        service = AccountService()
        assert isinstance(service.get_user(user_id), User)

    def test_get_user_not_found(self):
        user_id = '1'
        service = AccountService()
        with(pytest.raises(UserNotFoundException)):
            service.get_user(user_id)

    def test_get_account(self):
        acc_id = '1'
        service = AccountService()
        assert isinstance(service.get_account(acc_id), Account)

    def test_get_account_not_found(self):
        acc_id = '100'
        service = AccountService()
        with(pytest.raises(AccountNotFoundException)):
            service.get_account(acc_id)

    def test_create_account(self):
        service = AccountService()
        user_id = '701c832c-5bd8-4322-9041-ddd3511bbc23'

        assert len(service.get_user(user_id).accounts) == 0

        service.create_account(user_id, 100.0)
        assert len(service.get_user(user_id).accounts) == 1
        assert service.get_user(user_id).accounts[0].balance == 100.0
        assert service.get_user(user_id).accounts[0].id is not None

    def test_internal_transfer(self):
        service = AccountService()
        user_id = '572ac805-aea8-4039-aaac-ee028e97b827'
        assert ['1', '2'] == [a.id for a in service.get_balances(user_id)]
        assert [250.0, 100.0] == [a.balance for a in service.get_balances(user_id)]

        from_id = '1'
        to_id = '2'
        service.transfer(from_id, to_id, 100)

        assert [150.0, 200.0] == [a.balance for a in service.get_balances(user_id)]

    def test_external_transfer(self):
        service = AccountService()

        # user1 account
        from_id = '1'
        assert service.get_account(from_id).balance == 250.0

        # user2 account
        user_id_2 = '701c832c-5bd8-4322-9041-ddd3511bbc23'
        service.create_account(user_id_2, 500.0)
        account = service.get_balances(user_id_2)[0]
        to_id = account.id
        assert account.balance == 500.0

        service.transfer(from_id, to_id, 100)

        assert service.get_account(from_id).balance == 150
        assert service.get_account(to_id).balance == 600

    def test_transfer_insufficient_balance(self):
        service = AccountService()
        from_id = '1'
        to_id = '2'

        with(pytest.raises(ValueError)):
            service.transfer(from_id, to_id, 10000)
