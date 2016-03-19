class Palindrom:
    largestPrime = 0

    def __init__(self):
        for i in range(999, 100):
            for j in range(999, 100):
                self.largestPrime = i * j

        print(self.isPalindrom(1001))

    def displayPrime(self):
        print(self.largestPrime)

    def isPalindrom(self, num):
        reverse = 0
        orignal = num
        remainder = 0
        while num > 0:
            remainder = num % 10
            reverse = reverse * 10 + remainder
            num = num / 10
        return reverse == orignal
