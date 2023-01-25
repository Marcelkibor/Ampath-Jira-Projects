# idea->classes only need to implement the methods that are relevant to them.
# Payment Interface
class Payment:
    def creditCardPayment(self, amount, card_number):
        pass
    def cashPayment(self, amount):
        pass
# Concrete class that implements credit payment only
class CreditCardPayment(Payment):
    def payWithCredit(self, amount, card_number):
        pass
# Concrete class that implements only cash
class CashPayment(Payment):
    def cashPayment(self, amount: float):
        return "cash payment of amount {} recieved".format(amount)
        
cash_payment = CashPayment()
print(cash_payment.cashPayment(50))
