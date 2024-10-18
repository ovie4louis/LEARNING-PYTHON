#creating sets

nums = {1, 2, 3, 4}

num2 = set((1, 2, 3, 4))

print(nums)
print(nums)
print(type(nums))
print(len(nums))

#no duplicate allowed in set

nums = {1, 2, 2, 3}
print(nums)

#True value is a dupe of 1, False is a dupe of zero

nums = {1, True, 2, False, 3, 4, 0}
print(nums)

#check if a value is in set
print(2 in nums)

#but you cannot refer to an element in the set with an index position or key

# add a new element to a set
nums.add(8)
print(nums)

#Add elements from one set to another
morenums = {5, 6, 7}
nums.update(morenums)
print(nums)

# you can use update with lists, tuples, and Dictionaries, too

# Merge two sets to create a new set
one = {1, 2, 3}
two = {5, 6, 7}

mynewset = one.union(two)
print(mynewset)

#keep only the duplicate
one = {1, 2, 3}
two = {2, 3, 4}

one.intersection_update(two)
print(one)

#keep  everything except only the duplicate
one = {1, 2, 3}
two = {2, 3, 4}

one.symmetric_difference_update(two)

print(one)