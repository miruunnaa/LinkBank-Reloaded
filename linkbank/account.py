class Account(object):

    currency = 'RON'  # class property
    iban_base = 'RO12LNK_'
    global_account_id = 10000

    def __init__(self, first_name, last_name):
        Account.global_account_id += 1
        self._iban = Account.iban_base + str(Account.global_account_id)  # e.g. RO12LNK_10001
        self.first_name = 'F_' + first_name
        self.last_name = 'L_' + last_name
        self._amount = 0  # encapsulation
        self.__limit = 100 * 1000
        self._transactions_uuids = []
        self.account_type = ''

    @property
    def iban(self):
        return self._iban

    @iban.setter
    def iban(self, iban):
        self._iban = iban

    @property
    def amount(self):  # getter
        # SELECT amount FROM accounts...
        # self._amount = from_database
        return self._amount

    @amount.setter
    def amount(self, amount):
        self._amount = amount

    def __str__(self):  # TODO: Remove F_ and L_
        return f"[{self._iban}] {self.first_name} {self.last_name} has in account {self._amount} {Account.currency}"

    def show_info(self):
        return f"{self.first_name} {self.last_name} has in account {self._amount} {Account.currency}"

    def deposit(self, amount):
        if amount < 0:
            return

        # TODO: Add transaction history
        self._amount += amount

    def withdraw(self, amount):

        if self._amount - amount < 0:
            return

        # INSERT INTO transactions ...
        self._amount -= amount

    def transfer(self, transaction_uuid):
        self._transactions_uuids.append(transaction_uuid)
