mytuple = tuple(("Dave", 42, True))

anothertuple = (1, 4, 2, 8, 2, 2,)

print(mytuple)
print(anothertuple)

newlist = list(mytuple)
print(newlist)
newlist.append("Neil")
print(newlist)
newtuple = tuple(newlist)
print(newtuple)


(one, two, *hey) = anothertuple

print(one)
print(two)
print(*hey)

print(anothertuple.count(2))