# a superclass should be closed for modification but open for extension. 
class Payment:
    def __init__(self, amount):
        self.amount = amount

    def getPaymentAmount(self):
        return self.amount

class CreditPayment(Payment):
    def __init__(self, amount, creditedBankName):
        super().__init__(amount)
        self.creditedBankName = creditedBankName

    def get_bank_name(self):
        return self.creditedBankName

def processPayment(payment: Payment):
    print("Payment of Ksh/=" + str(payment.getPaymentAmount()) + " confirmed.")

creditPayment = CreditPayment(100, "Equity Bank")
processPayment(creditPayment)
