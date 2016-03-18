class Fibonacci:
    sumFibo = 0

    def __init__(self, n):
        first = 0
        second = 1
        current = 0
        while current < n:
            current = first + second
            if current % 2 == 0:
                self.sumFibo += current
            first = second
            second = current

    def showFibo(self):
        print(self.sumFibo)
