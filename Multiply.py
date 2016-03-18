class Multiple:
    sumMultiply = 0

    def __init__(self, n):
        self.n = n
        for i in range(1, n):
            if i % 3 == 0:
                if i % 5 == 0:
                    self.sumMultiply += i

    def showMultiple(self):
        print self.sumMultiply



