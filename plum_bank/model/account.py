import uuid
from dataclasses import dataclass


@dataclass
class Account:
    balance: float
    id: uuid = uuid.uuid4()

    def __init__(self, balance: float = 0.0) -> None:
        if not isinstance(balance, float):
            raise TypeError(f"Expecting type float but received {type(balance)}")
        if balance < 0:
            raise ValueError("Unexpected negative balance")
        self.balance = balance

    def update_balance(self, new_balance: float) -> None:
        self.balance = new_balance
