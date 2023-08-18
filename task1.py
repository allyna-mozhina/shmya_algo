arr = list(map(int, input().split()))
n = len(arr)

for i in range(n):
    NO_SWAPS = True

    for j in range(i, n - 1):
        if (arr[j] > arr[j + 1]):
            arr[j + 1], arr[j] = arr[j], arr[j + 1]
            NO_SWAPS = False
    
    if NO_SWAPS:
        break

print(arr)