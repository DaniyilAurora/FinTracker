from transaction import Transaction

class TransactionManager():
    def __init__(self):
        self.transactions = list()
    
    def getTransactions(self):
        return self.transactions
    
    def addTransaction(self, origin: str, amount: float):
        newTransaction = Transaction(len(self.transactions), origin, amount)
        self.transactions.append(newTransaction)
    
    def removeTransaction(self, id: int):
        self.transactions.pop(id)