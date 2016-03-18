class LargestPrime:
    limit = 600851475143
    primeFactor = 0

    def __init__(self):
        for i in range(2, self.limit / 2):
            if self.limit % i == 0:
                self.checkPrime(i)

    def displayPrime(self):
        print self.primeFactor

    def checkPrime(self, num):
        for j in range(2, num / 2):
            if num % j == 0:
                break
            else:
                self.primeFactor = num
