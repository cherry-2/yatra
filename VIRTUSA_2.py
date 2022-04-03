# A array (or list or equivalent) F1 has got names of Facebook users and their friend association.
# For example if we write:  User1, User2 it implies that User1 is a friend of User2. This also implies that User2 is a friend of User1.
# Write a program which will parse F1 and remove duplicates and write all the unique pairs to a new array F2
def UniquePairs():
    listf1 = ["U1,U2", "U3,U4", "U1,U5", "U2,U1", "U3,U4"]
    list2 = map(lambda each: each.strip('"'), listf1)
    listf2 = []
    for i in list2:
        listf2.append(i.split(','))
    print(listf2)
    print(set(tuple(sorted(i)) for i in listf2))


UniquePairs()