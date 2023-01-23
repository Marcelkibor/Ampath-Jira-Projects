# in this example, a class is created to handle all the payment functionality.
# The class contains three functions which have seperate roles but don't enterfere with each other
class PaymentHandler:
    def __init__(self):
        self.balance = 0

    def addPayment(self, amount):
        print("old balance is", self.balance)
        # adding amount to the balance
        self.balance += amount
        print("new balance is",self.balance)

    def processBalance(self, amount):
        # this takes in a payed amount and subtracts it from the balance
        if self.balance >= amount:
            self.balance -= amount
        else:
            return "Illegal Operation"
handlePay = PaymentHandler()
handlePay.addPayment(10)
handlePay.processBalance(5)
