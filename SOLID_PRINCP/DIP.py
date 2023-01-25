# idea:-> HLM not dep on lw, bt astractions.

# Abstract class
class Payment:
    def __init__(self):
        pass
    def process_payment(self, amount):
        pass

# Concrete class (Low level)
class CreditCardPayment(Payment):
    def __init__(self, card_number):
        self.card_number = card_number
    def process_payment(self, amount):
         print("payed {} with credit".format(amount))

# Concrete class (Low level)
class MpesaPayment(Payment):
    def __init__(self, tillNumber):
        self.tillNumber = tillNumber
    def process_payment(self, amount):
        print("payed {} with Mpesa".format(amount))

# High-level module
class PaymentService:
    def __init__(self, payment: Payment):
        self.payment = payment
    def makePayment(self, amount):
        self.payment.process_payment(amount)


payWithCredit = CreditCardPayment("1234 5678 9012 3456")
paymentService = PaymentService(payWithCredit)
paymentService.makePayment(100)

payWithMpesa = MpesaPayment(1234)
payment_service = PaymentService(payWithMpesa)
payment_service.makePayment(100)
