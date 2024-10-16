users = ["Ovie", "Louis", "Enakarhire"]

data = ["Ovie", 43, True]

emptylist = []

print("Ovie" in emptylist)

print(users[0])
print(users[-1])

print(users.index("Ovie")) # Getting position

print(users[0:2])
print(len(users))
users.append("Elsa")
print(users)

# adding lists to a list
users += ["joy", "james"] 
print(users)

#or

# users.extend(["peace", "mercy"])
# print(users)

# users.insert(0, "John")
# print(users)
# users.insert(3, "phone")
# print(users)

# users[2:2] = ["fish", "yam"]
# print(users)
# users.clear()
# print(users)



mylist  = ["My", "Name", "Is", "Ovie"]
print(mylist)
mylist.sort()

print(mylist)

mylist[1:2] = ['louis']

print(mylist)

print(mylist)
mylist.sort()

print(mylist)

print(mylist)
mylist.sort(key=str.lower)

print(mylist)

num = [4, 42, 78, 1, 5]
num.reverse()
print(num)

# num.sort(reverse=True)
# print(num)

print(sorted(num, reverse=True))


#three ways of copy list

numcopy = num.copy()
mynum = list(num)
mycopy = num[:]

print(numcopy)

print(mynum)

print(mycopy)

