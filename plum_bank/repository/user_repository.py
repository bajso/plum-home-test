import json
from typing import List

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
            self.users.append(user)
