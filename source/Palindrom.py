class Palindrom:
    largestPalindrom = 0

    def __init__(self):
        for i in range(999, 100, -1):
            for j in range(999, 100, -1):
                if self.isPalindrom(i * j):
                    if self.largestPalindrom < i * j:
                        self.largestPalindrom = i * j

    def displayPrime(self):
        print(self.largestPalindrom)

    def isPalindrom(self, num):
        reverse = 0
        orignal = num
        while num > 0:
            remainder = num % 10
            reverse = reverse * 10 + remainder
            num /= 10
        return reverse == orignal
