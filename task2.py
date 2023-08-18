arr = list(map(int, input().split()))
n = len(arr)

for i in range(n):
    min_i = i
    for j in range(i + 1, n):
        if arr[j] < arr[min_i]:
            min_i = j
        
    if min_i != i:
        arr[min_i], arr[i] = arr[i], arr[min_i]

print(arr)
