from re import T
from person import Person
from wallet import Wallet


a_wallet = Wallet('Brown',True)
person_1 = Person('Sean','Blonde', a_wallet)

print(person_1.name)

print(person_1.wallet.cash)

person_1.wallet.put_cash_in_wallet(100)

print(person_1.wallet.cash)