# LinkBank – Python OOP Banking System (v2)

An expanded object-oriented banking system built in Python, demonstrating advanced OOP concepts including inheritance, encapsulation, polymorphism, enums, data persistence with JSON, and unique identifier generation.

## Project Structure

```
linkbank/
│
├── account.py        # Base Account class with IBAN and transaction tracking
├── regular.py        # RegularAccount – extends Account with interest rate
├── credit.py         # CreditAccount – extends Account with debt tracking
├── transaction.py    # Transaction class with UUID-based identification
├── bank.py           # Bank class managing a collection of accounts
├── currency.py       # Currency enum (RON, EUR, USD)
├── account_type.py   # AccountType enum (REGULAR, CREDIT)
│
├── accounts.json     # Persisted account data (save/load)
└── test-bank.py      # Main script demonstrating all functionality
```

## Classes

### `Account` (account.py)
The base class for all account types.

- **Class variables:** `currency`, `iban_base`, `global_account_id` (auto-increments per account)
- **Properties:** `iban`, `amount` (getter + setter)
- **Methods:**
  - `deposit(amount)` – adds funds to the account
  - `withdraw(amount)` – removes funds if balance allows
  - `transfer(transaction_uuid)` – records a transaction UUID
  - `show_info()` – returns a formatted account summary

### `RegularAccount` (regular.py)
Extends `Account` with an interest rate. Type set to `AccountType.REGULAR_ACCOUNT`.

### `CreditAccount` (credit.py)
Extends `Account` with credit/debt functionality. Type set to `AccountType.CREDIT_ACCOUNT`.

- **Properties:** `debt` (getter + setter)
- **Overrides:**
  - `deposit(amount)` – deposits and reduces debt
  - `withdraw(amount)` – allows balance to go negative, tracking debt
  - `__str__()` – displays balance and current debt

### `Transaction` (transaction.py)
Represents a transfer between two accounts.

- Auto-generates a unique `uuid4` identifier
- Stores `from_account`, `to_account`, and `amount`

### `Bank` (bank.py)
Manages a list of account IBANs.

- `add_account(iban)` – registers an account
- `accounts` property – returns all registered IBANs

### `Currency` (currency.py)
Enum for supported currencies: `RON`, `EUR`, `USD`.

### `AccountType` (account_type.py)
Enum for account types: `REGULAR_ACCOUNT`, `CREDIT_ACCOUNT`.

## Data Persistence

Accounts can be saved to and loaded from a JSON file:

```python
save_data('accounts.json', accounts)             # save
accounts = read_data('accounts.json')            # load
accounts_objs = create_accounts(bank, accounts)  # rebuild objects from JSON
```

## How to Run

```bash
python test-bank.py
```

Make sure `accounts.json` exists in the same directory, or uncomment the account creation and `save_data` lines in `test-bank.py` to generate it first.

## Concepts Demonstrated

| Concept | Where |
|---|---|
| Encapsulation | `_amount`, `_iban`, `_debt`, `__limit` |
| Inheritance | `RegularAccount`, `CreditAccount` extend `Account` |
| Method overriding | `withdraw()`, `deposit()`, `__str__()` in `CreditAccount` |
| Polymorphism | `deposit()` called on mixed list of account types |
| Enums | `Currency`, `AccountType` |
| Properties | `@property` getters/setters throughout |
| Class variables | `currency`, `iban_base`, `global_account_id` |
| Unique identifiers | Auto-incremented IBAN, UUID for transactions |
| Data persistence | JSON save/load with object reconstruction |
| Factory function | `create_account()` using `match/case` |

## Requirements

- Python 3.10+ (required for `match/case` syntax)
- No external dependencies

## Notes

- This is an expanded version of the original LinkBank project, adding persistence, enums, a Bank class, and transaction tracking
- Built as part of a Python & OOP course at **Link Academy**
- Some features are marked `TODO` (e.g. loading transaction history, limit enforcement)
