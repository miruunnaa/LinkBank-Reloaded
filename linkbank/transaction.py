from .currency import Currency
import uuid

class Transaction:

    currency = Currency.RON

    def __init__(self, from_account, to_account, amount):
        # unique identifier (at bank level) - auto generated
        self._uuid = uuid.uuid4()
        self._from_account = from_account
        self._to_account = to_account
        self._amount = amount

    @property
    def id(self):
        return self._uuid

    def __str__(self):
        return f'Transaction with id {self._uuid} was made from account {self._from_account} to account {self._to_account} for the amount of {self._amount} {self.currency}'
