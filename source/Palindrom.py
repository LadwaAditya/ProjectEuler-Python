class Palindrom:
    largestPrime = 0

    def __init__(self):
        for i in range(999, 100):
            for j in range(999, 100):
                self.largestPrime = i * j
