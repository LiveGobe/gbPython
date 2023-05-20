n, m, k = map(int, input().split())

if k < n * m and (k % n == 0 or k % m == 0):
    print("yes")
else:
    print("no")