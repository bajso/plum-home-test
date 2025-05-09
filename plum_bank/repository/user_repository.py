import json
import uuid
from typing import List

from plum_bank.model.exceptions.account_not_found import AccountNotFoundException
from plum_bank.model.exceptions.user_not_found_exception import UserNotFoundException
from plum_bank.model.account import Account
from plum_bank.model.user import User

PREPOPULATED_USERS = """[
    {
        "id": "701c832c-5bd8-4322-9041-ddd3511bbc23",
        "name": "Arisha Barron"
    },
    {
        "id": "3c6289e7-1653-4f6e-a6c5-88b00d5c8a07",
        "name": "Branden Gibson"
    },
    {
        "id": "9d7a16a9-26c5-49a3-af6e-84a94c7d6a97",
        "name": "Rhonda Church"
    },
    {
        "id": "572ac805-aea8-4039-aaac-ee028e97b827",
        "accounts": [
            {
                "id": "1",
                "balance": "250"
            },
                        {
                "id": "2",
                "balance": "100"
            }
        ],
        "name": "Georgina Hazel"
    }
]"""


class UserRepository:
    users: List[User]

    def __init__(self) -> None:
        self.users = []
        tmp_users = json.loads(PREPOPULATED_USERS)
        for item in tmp_users:
            user = User(item['name'])
            user.id = item['id']
            if (accounts := item.get('accounts')) is not None:
                account_list = []
                for a in accounts:
                    account = Account(float(a['balance']))
                    account.id = a['id']
                    account_list.append(account)
                user.accounts = account_list
            self.users.append(user)

    def find_by_id(self, user_id: uuid) -> User:
        matches = [u for u in self.users if u.id == user_id]
        if not matches:
            raise UserNotFoundException(f"User with id:{user_id} not found")
        assert len(matches) == 1
        return matches[0]

    def find_account_by_id(self, acc_id: uuid) -> Account:
        for user in self.users:
            for acc in user.accounts:
                if (acc_id == acc.id):
                    return acc
        raise AccountNotFoundException(f"Account with id:{acc_id} not found")
