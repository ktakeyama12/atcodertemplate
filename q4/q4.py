import sys
f = open('q4input.txt', 'r')
sys.stdin = f


class Q4:
    from collections import namedtuple
    def __init__(self):
        dp = []
        dp[0][0] = 0
        dp[0][1] = -float('inf')




if __name__ == '__main__':
    q4 = Q4()