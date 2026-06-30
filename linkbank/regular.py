from .account import Account
from .account_type import AccountType

# RegularAccount extends Account
class RegularAccount(Account):

    def __init__(self, first_name, last_name, interest):
        # call parent constructor
        super().__init__(first_name, last_name)
        self.interest = interest
        self.account_type = AccountType.REGULAR_ACCOUNT.value

    def __str__(self):
        return super().__str__()
