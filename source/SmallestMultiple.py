class SmallestMultiple:
    smallestMultiple = 20

    def __init__(self):
        n = 20
        flag = 0
        while n:
            for i in range(2, 20):
                flag = n % i == 0
                if flag != 1:
                    break
            if flag == 1:
                self.smallestMultiple = n
                break

    def printMultiple(self):
        print(self.smallestMultiple)
