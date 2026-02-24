'''
Alyssa asked Ben to review the following code:


class BankAccount:
    def __ini__(self, starting_balance):
        self._balance = starting_balance

    def balance_is_positive(self):
        return self.balance > 0

    @property
    def balance(self):
        return self._balance

You can access the self.balance because we have a getter method using the
@property decorator followed by the method definition. 

'''