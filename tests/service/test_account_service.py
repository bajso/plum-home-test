import pytest
from plum_bank.exceptions.user_not_found_exception import UserNotFoundException
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

    def test_create_account(self):
        service = AccountService()
        user_id = '701c832c-5bd8-4322-9041-ddd3511bbc23'

        assert len(service.get_user(user_id).accounts) == 0

        service.create_account(user_id, 100.0)
        assert len(service.get_user(user_id).accounts) == 1
        assert service.get_user(user_id).accounts[0].balance == 100.0
        assert service.get_user(user_id).accounts[0].id is not None
