from plum_bank.repository.user_repository import UserRepository


class TestUserRepository:
    def test_create_repository(self):
        repo = UserRepository()
        assert len(repo.users) == 4
