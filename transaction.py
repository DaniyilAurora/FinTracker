class Transaction():
    def __init__(self, id: int, origin: str, amount: float):
        self.origin = origin
        self.amount = amount
        self.id = id

    def getID(self):
        return self.id