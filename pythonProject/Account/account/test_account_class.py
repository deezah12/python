import unittest

from .account import Account


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.acc = Account("Elder Jega")

    def test_account_can_be_created(self):
        # acc = Account()
        self.assertIsNotNone(self.acc)

    def test_that_account_has_zero_balance_on_creation(self):
        # acc = Account()
        self.assertEqual(0, self.acc.balance)

    def test_that_account_has_a_name(self):
        # acc = Account("Elder Jega")

        self.assertEqual("Elder Jega", self.acc.name)

    def test_that_account_can_deposit(self):
        self.acc.deposit(1000)
        self.assertEqual(1000, self.acc.balance)

    def test_that_account_can_withdraw(self):
        self.acc.deposit(5000)
        self.assertEqual(5000, self.acc.balance)
        self.acc.withdraw(3000, 1111)
        self.assertEqual(2000, self.acc.balance)

    def test_account_cannot_withdraw_Higher_Amount(self):
        self.acc.deposit(1000)
        self.assertEqual(1000, self.acc.balance)
        self.acc.withdraw(2000, 1111)
        self.assertEqual(1000, self.acc.balance)

    def test_account_cannot_deposit_negative_amount(self):
        self.acc.deposit(-1000)
        self.assertEqual(0, self.acc.balance)

    def test_account_can_transfer(self):
        self.acc1 = Account("Hadiza")
        self.acc2 = Account("Umar")

        self.acc1.deposit(2000)
        self.assertEqual(2000, self.acc1.balance)
        self.acc1.transfer(1000, self.acc2)
        self.assertEqual(1000, self.acc1.balance)

        self.assertEqual(1000, self.acc2.balance)


if __name__ == '__main__':
    unittest.main()
