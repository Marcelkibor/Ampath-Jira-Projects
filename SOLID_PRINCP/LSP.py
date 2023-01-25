# idea-> obj sup can rep sub , witht afct corectness
class Payment:
    def __init__(self, amount):
        self.amount = amount
    def getPaymentAmount(self):
        return self.amount
#subclass
class MpesaPayment(Payment):
    def __init__(self, amount, tillNumber):
        super().__init__(amount)
        self.tillNumber = tillNumber
    def getTillNumber(self):
        return self.tillNumber

#HL module ->expects superclass, but...
def processPayment(payment:Payment):
    return "payed amount {} confirmed".format(str(payment.getPaymentAmount()))

mpesaPayment = MpesaPayment(100,32452)
# can be replaced with subclass
print(processPayment(mpesaPayment))

