import unittest
from ledger import Ledger

class TestLedger(unittest.TestCase):

    def _prepare(self):
        self.ledger = Ledger()
        self.ledger.records = [
            ("Joe", 1, "BigBag", 1000),
            ("Mick", 2, "MoneyPile", 1000),
            ("Bob", 3, "BigBag", 1000),
            ("Alice", 4, "MoneyPile", 1000),
            ]

    def test_credit(self):
        self._prepare()
        self.ledger.credit("Joe", 1, "BigBag", 500)
        self.assertEqual(len(self.ledger.records), 5)
        self.assertEqual(self.ledger.records[-1], ("Joe", 1, "BigBag", -500))
    
    def test_debit(self):
        self._prepare()
        self.ledger.debit("Joe", 1, "BigBag", 500)
        self.assertEqual(len(self.ledger.records), 5)
        self.assertEqual(self.ledger.records[-1], ("Joe", 1, "BigBag", 500))

    def test_credit_neg(self):
        self._prepare()
        with self.assertRaises(Exception):
            self.ledger.credit("Joe", 1, "BigBag", -500)

    def test_bank_balance(self):
        self._prepare()
        self.assertEqual(self.ledger.bank_balance("MoneyPile"), 2000) 

    def test_transfer(self):
        self._prepare()
        self.ledger.transfer("Joe", 1, "BigBank", "Mick", 1, "MoneyPile", 1)
        self.assertEqual(self.ledger.person_balance("Joe"), 999)
        self.assertEqual(self.ledger.person_balance("Mick"), 1001)

    # More tests missing


if __name__ == '__main__':
    unittest.main()
