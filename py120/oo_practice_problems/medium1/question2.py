'''
Alan craeted the following code to keep track of items for a shopping card application he's writting:

class InvoiceEntry:
    def __init__(self, product_name, number_purchased):
        self._product_name = product name
        self._quantity = number_purchased

entry = InvoiceEntry('Marbles', 5000)
print(entry.quantity)

entry.quantity = 10000
print(entry,quantity)

Without changing any of the lines of code, update the InvoiceEntry class so it functions as shown.


'''

class InvoiceEntry:
    def __init__(self, product_name, number_purchased):
        self._product_name = product_name
        self._quantity = number_purchased

    @property
    def quantity(self):
        return self._quantity
    
    @quantity.setter
    def quantity(self, quantity):
        self._quantity = quantity
    
entry = InvoiceEntry('Marbles', 5000)
print(entry.quantity)         # 5000

entry.quantity = 10_000
print(entry.quantity)         # 10000