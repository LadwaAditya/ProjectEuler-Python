class SmallestMultiple:
    smallestMultiple = 20

    def __init__(self):
        n = 20
        flag = 0
        while n:
            for i in range(2, 20):
                if n % i == 0:
                    flag = 1
                else:
                    flag = 0
                if flag == 0:
                    break
            if flag == 1:
                self.smallestMultiple = n
                break
            n += 1

    def printMultiple(self):
        print(self.smallestMultiple)
