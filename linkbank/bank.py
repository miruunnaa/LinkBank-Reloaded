class Bank:

    def __init__(self, name):
        self._name = name
        self._accounts = []

    def add_account(self, iban):
        self._accounts.append(iban)

    @property
    def accounts(self):
        return self._accounts
