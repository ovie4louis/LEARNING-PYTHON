
band = {
    "vocals" : "plant",
    "guitar" : "page"

}

band2 = dict(vocals = "plant", guitar = "page")

print(band)
print(band2)

# Access items
print(type(band))
print(len(band))

# list all keys

print(band.keys())

# list all values

print(band.values())

#list of keyysvalue pairs as Tuples
print(band.items())

#verify a key exists
print("guitar" in band)
print("triangle" in band)

#change value
band["vocals"] = "Coverdale"
#add new keys value pairs
band.update({"base": "Jpl"})

print(band)

# remove a items
print(band.pop("base"))
print(band)

band["drums"] = "Bonham"
print(band)

#remove the last value keys pairs added to it and return Tuple
print(band.popitem())
print(band)

#delete and clear itmem

band["drums"] = "Bonham"
print(band)

del band["drums"]
print(band)

band2.clear()
print(band2)

# del band2
# print(band2)

# copy dictionaries

# band2 = band # this is not copy but create a reference (i.e both are pointing the same place in the memory what ever you remove from band2 will be remove in band )

# print("Bad copy!")
# print(band2)
# print(band)


# band2["drums"] = "ovie"
# print(band)

band2 = band.copy()
band2["drums"] = "Dave"
print("Good copy!")
print(band)
print(band2)

# or use the dict() function

band3 = dict(band)
print("Good copy!")
print(band3)

# Nested dictionaries

member1 = {
    "name": "plant",
    "intrument": "vocals"
}
member2 = {
    "name": "page",
    "instrument": "guitar"
}

band = {
    "member1": member1,
    "member2": member2
}
print(band)
print(band["member1"]["name"])
