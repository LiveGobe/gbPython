n = int(input())
a = list(map(int, input().split()))
x = int(input())

left = 0
right = n - 1

while left < right:
    mid = (left + right) // 2
    if abs(a[mid] - x) < abs(a[mid - 1] - x) and abs(a[mid] - x) < abs(a[mid + 1] - x):
        print(a[mid])
        break
    elif a[mid] < x:
        left = mid + 1
    else:
        right = mid - 1
else:
    if abs(a[left] - x) < abs(a[left - 1] - x):
        print(a[left])
    else:
        print(a[left - 1])