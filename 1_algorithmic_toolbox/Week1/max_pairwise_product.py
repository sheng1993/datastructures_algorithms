# Uses python2
n = int(input())
a = [int(x) for x in raw_input().split()]
assert(len(a) == n)

max_number1 = -1
max_number2 = -1
max_index1 = -1

for i in range(0, n):
    if a[i] > max_number1:
        max_number1 = a[i]
        max_index1 = i


for i in range(0, n):
    if i != max_index1 and a[i] > max_number2:
        max_number2 = a[i]

print(max_number1 * max_number2)
