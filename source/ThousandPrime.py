class ThousandPrime:
    thousandPrime = 0

    def __init__(self):
        n = 3
        count = 0
        flag = 0
        while True:
            for i in range(2, n / 2):
                if n % i == 0:
                    flag = 1
                    break
                else:
                    flag = 0
            if flag == 0:
                count += 1
            if count == 10001:
                self.thousandPrime = n
                break
            n += 1

    def displayThousand(self):
        print(self.thousandPrime)
