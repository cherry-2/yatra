'''for i in range(100, 200):
    if all(i%num != 0 for num in range(2,i)):
        print(i)'''

'''list1 = [11, 12, 10, 15, 8, 99, 156, 13, 7]

i = 0
for i in range(i, len(list1)):
    for j in range(i+1, len(list1)):
        if list1[i] > list1[j]:
            temp = list1[i]
            list1[i] = list1[j]
            list1[j] = temp

print(list1)

nlist = []
while list1:
    minimum = list1[0]
    for x in list1:
        if x > minimum:
            minimum = x
            nlist.append(minimum)
            list1.remove(minimum)
# print(nlist)


# fibanacci series

def f(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return f(n-1) + f(n-2)


for n in range(0, 12):
    print(f(n))'''


def ispalidrome(string):
    rev = "".join(reversed(string))
    if rev == string:
        print("its palidrome")
    else:
        print("not")

ispalidrome("mada")

