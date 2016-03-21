class SumSquareDiff:
    sumSquareDiff = 0
    sumSquare = 0
    squareSum = 0

    def __init__(self):
        for i in range(1, 100):
            self.sumSquare += i * i
            self.squareSum += i
        self.squareSum = self.squareSum * self.squareSum
        self.sumSquareDiff = self.squareSum - self.sumSquare

    def displaySumSquareDiff(self):
        print(self.sumSquareDiff)
