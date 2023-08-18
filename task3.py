arr = list(map(int, input().split()))
n = len(arr)

# for i in range(n):
#     j = i
#     while j > 0 and arr[j - 1] > arr[j]:
#         arr[j - 1], arr[j] = arr[j], arr[j - 1]
#         j -= 1
#         print(arr)

for i in range(n):
    for j in range(0, i):
        if arr[j] > arr[i]:
            elem = arr.pop(i)
            arr.insert(j, elem)
            break

print(arr)