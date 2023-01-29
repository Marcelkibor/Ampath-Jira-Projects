#idea-> class should have 1 resp, one reason to change

class Payment:
    def __init__(self):
        self.balance = 0

    def depositAmount(self, amount):
        # adding amount to the balance
        self.balance += amount
        print("balance after deposit->",self.balance)

    def processPayment(self, amount):
        #balance should always be greater than payed amount
        if self.balance >= amount:
            self.balance -= amount
            print("balance after making payment->{}".format(self.balance))
        if self.balance< amount:
            print("insufficient funds")
handlePay = Payment()
handlePay.depositAmount(10)
handlePay.processPayment(50)
