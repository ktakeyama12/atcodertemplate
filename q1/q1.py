import sys
f = open('q1input.txt', 'r')
sys.stdin = f


class Q1:
    def __init__(self):
        a, b, t = (int(i) for i in input().split())
        times = t // a
        print(times*b)


if __name__ == '__main__':
    q1 = Q1()