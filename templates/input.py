class Input:
    def __init__(self):
        a, b, c, d = (int(i) for i in input().split())
        # a=2 b=4 c=5 d =7

        a = [int(i) for i in input().split()]
        # a = [2, 4, 5, 6]

        3 # n Aの数
        22 # A1
        14 # A2
        45 # A3
        n = int(input())
        t = [int(input()) for i in range(n)]
        # t = [22, 14, 45]

        n = int(input())
        e = [[int(i) for i in input().split()] for i in range(n)]
        #  [[22, 1, 45], [25, 53, 110], [4, 444, 555], [2, 5, 0]]


if __name__ == '__main__':
    input = Input()