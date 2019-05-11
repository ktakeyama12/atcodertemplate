import sys
f = open('q2input.txt', 'r')
sys.stdin = f


class Q2:
    def __init__(self):
        n = int(input())
        v = [int(i) for i in input().split()]
        c = [int(i) for i in input().split()]
        ans = 0
        for i in range(n):
            if v[i] > c[i]:
                ans += v[i] - c[i]
        print(ans)


if __name__ == '__main__':
    q2 = Q2()