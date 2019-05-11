import sys
f = open('q3input.txt', 'r')
sys.stdin = f


class Q3:
    def __init__(self):

        def gcd(x, y):
            if y == 0:
                return x
            else:
                return gcd(y, x % y)

        n = int(input())
        a = [int(i) for i in input().split()]
        if len(a) == 2:
            print(gcd(a[0],a[1]))
        else:
            minval = min(a)
            maxgcd = max(gcd(a[0],a[1]),gcd(a[1],a[2]),gcd(a[0],a[2]))
            maxgcd2 = maxgcd
            for index, value in enumerate(a):
                if value == minval:
                    continue
                temp = gcd(minval, value)
                if temp <= maxgcd:
                    maxgcd2 = maxgcd
                    maxgcd = temp
            minval2 = float('inf')
            counter = 0
            if maxgcd2 == minval:
                for index, value in enumerate(a):
                    if value == minval:
                        counter += 1
                        if counter == 2:
                            minval2 = maxgcd2
                    if minval2 > value > minval:
                        minval2 = value
                print(minval2)
                return
            print(maxgcd2)



if __name__ == '__main__':
    q3 = Q3()