from linkbank.regular import RegularAccount
from linkbank.credit import CreditAccount
from linkbank.account import Account
from linkbank.transaction import Transaction
from linkbank.bank import Bank
from linkbank.account_type import AccountType
import json

link_bank = Bank('LINK Bank')

def create_account(bank, account_type, first_name, last_name, interest):
    match account_type:
        case AccountType.REGULAR_ACCOUNT:
            account = RegularAccount(first_name, last_name, interest)
        case AccountType.CREDIT_ACCOUNT:
            account = CreditAccount(first_name, last_name, interest)
        case _:
            return None
    bank.add_account(account.iban)
    return account

def save_data(filename, accounts):
    f = open(filename, 'w')
    accounts_str = json.dumps(accounts)
    f.write(accounts_str)
    f.close()

def read_data(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    json_str = ''.join(lines)
    accounts_list = json.loads(json_str)
    f.close()
    return accounts_list

# vasile_account = create_account(link_bank, AccountType.REGULAR_ACCOUNT, "Vasile", "Popescu", 1)
# gigel_account = create_account(link_bank, AccountType.CREDIT_ACCOUNT, "Gigel", "Haralambie", 15)
# accounts = [vasile_account, gigel_account]
# accounts = [vasile_account.__dict__, gigel_account.__dict__]
# print(vasile_account)

# save_data('accounts.json', accounts)

def create_accounts(bank, accounts_dict_list):
    accounts_objs = []
    for account_data in accounts_dict_list:
        account = create_account(bank,
                       AccountType(account_data['account_type']),
                       account_data['first_name'],
                       account_data['last_name'],
                       account_data['interest'])
        if account is None:
            continue

        account.iban = account_data['_iban']
        account.amount = account_data['_amount']
        # TODO: load limit
        # TODO: load transactions

        if isinstance(account, CreditAccount):
            account.debt = account_data['_debt']
        accounts_objs.append(account)

    return accounts_objs

accounts_dict_list = read_data('accounts.json')
accounts_objs = create_accounts(link_bank, accounts_dict_list)

def show_accounts(accounts_objs):
    for obj in accounts_objs:
        print(obj)

show_accounts(accounts_objs)
transfer50 = Transaction(accounts_objs[0].iban, accounts_objs[1].iban, 50)
show_accounts(accounts_objs)

print(link_bank.accounts)

# TODO: Add accounts to a list

# display all account information
# print(f"{vasile_account.first_name} {vasile_account.last_name} has in account {vasile_account.amount} {Account.currency}")

# print(vasile_account.show_info())
# print(gigel_account.show_info())

# print(vasile_account)
# vasile_account.deposit(100)
# print(vasile_account)
# vasile_account.amount = 3
# print(vasile_account.amount)
# vasile_account.withdraw(15)
# print(vasile_account)
# vasile_account.withdraw(90)
# print(vasile_account)

# print(gigel_account)
# gigel_account.deposit(13)
# print(gigel_account)
# gigel_account.withdraw(50)
# print(gigel_account)
# gigel_account.withdraw(10)
# print(gigel_account)
# gigel_account.deposit(20)
# print(gigel_account)

# for account in accounts:
#     account.deposit(10)  # polymorphism

# print(vasile_account, gigel_account)
# vasile_account._amount = -39132132
# vasile_account.withdraw(414)

# Vasile sends Gigel 50 RON
# Create the transaction
# transfer50 = Transaction(vasile_account.iban, gigel_account.iban, 50)
# print(transfer50)
# add transaction to Vasile's list
# vasile_account.transfer(transfer50.id)
# add transaction to Gigel's list
# gigel_account.transfer(transfer50.id)

# vasile_account.deposit(-313131)
