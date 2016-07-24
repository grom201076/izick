from functools import reduce

class Ledger:
    def __init__(self):
        self.records = []

    # withdraw
    def credit(self, person, account, bank, amount):
        assert(amount>0)
        #TODO: check final balance before transaction
        record = (person, account, bank, -amount)
        self.records.append(record)
     
    # put
    def debit(self, person, account, bank, amount):
        assert(amount>0)
        record = (person, account, bank, amount)
        self.records.append(record)

    def transfer(self, person_a, account_a, bank_a, person_b, account_b, bank_b, amount):
        assert(amount>0)
        self.credit(person_a, account_a, bank_a, amount)
        self.debit(person_b, account_b, bank_b, amount)

    def bank_records(self, bank):
        return [r for r in self.records if r[2]==bank]

    def bank_balance(self, bank):
        return reduce(lambda acc,x: acc+x[3], self.bank_records(bank), 0)

    def person_records(self, person):
        return [r for r in self.records if r[0]==person]

    def person_balance(self, person):
        return reduce(lambda acc,x: acc+x[3], self.person_records(person), 0)

    def account_records(self, account):
        return [r for r in self.records if r[1]==int(account)]

    def account_balance(self, account):
        return reduce(lambda acc,x: acc+x[3], self.account_records(account), 0)
