import mysql.connector
# record what a customer has purchased and associated transaction simultaneously
def DatabaseConnect():
    mydb = mysql.connector.connect(
    host="localhost",
    user="marcel",
    passwd="root",
    database="UnitTest"
    )
    return mydb

def PurchaseFruit(customerId,fruitId,amount):
    conn = DatabaseConnect()
    cursor = conn.cursor()
    cursor.execute("START TRANSACTION")
    try:
        purchaseSql = "INSERT INTO customerPurchase (customer_id, fruit_id) VALUES (%s, %s)"
        purchaseVal = (customerId, fruitId)
        cursor.execute(purchaseSql, purchaseVal)
        purchaseId = cursor.lastrowid

        transactionSql = "INSERT INTO transactions (purchase_id, amount) VALUES (%s, %s)"
        transactionValues = (purchaseId, amount)
        cursor.execute(transactionSql, transactionValues)
        conn.commit()
        print("Customer Purchase and Fruits Inventory Updated!.")

    except mysql.connector.Error as e:
        conn.rollback()
        print("Transaction rolled back. Error->",e)
    cursor.close()
    conn.close()

PurchaseFruit(2,6,100)
PurchaseFruit(1,7,500)
