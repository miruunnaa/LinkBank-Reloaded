from enum import Enum

class Currency(Enum):

    RON = 1
    EUR = 2
    USD = 3

if __name__ == '__main__':

    vasile_currency = Currency.USD
    print(vasile_currency, type(vasile_currency))

    if vasile_currency == Currency.EUR:
        print(f"Correct! Vasile has his account in EUR")
    else:
        print(f"Not quite. Vasile has his account in {vasile_currency}")
