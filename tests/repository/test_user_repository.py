import pytest
from plum_bank.exceptions.user_not_found_exception import UserNotFoundException
from plum_bank.model.user import User
from plum_bank.repository.user_repository import UserRepository


class TestUserRepository:
    def test_create_repository(self):
        repo = UserRepository()
        assert len(repo.users) == 4

    def test_find_by_id_exists(self):
        _id = '572ac805-aea8-4039-aaac-ee028e97b827'
        repo = UserRepository()
        user = repo.find_by_id(_id)
        assert isinstance(user, User)

    def test_find_by_id_not_found(self):
        _id = '1'
        repo = UserRepository()
        with pytest.raises(UserNotFoundException):
            repo.find_by_id(_id)
