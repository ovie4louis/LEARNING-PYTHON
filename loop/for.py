#for loop execute a block of code a number of times
#for loop is useful for iterating over a sequence

actions = ["Dave", "Sara", "John"]
# for x in actions:
#     print(x)
    #prints each action in the list
    #the loop continues until all actions in the list have been printed
    #after each print, the loop moves on to the next name in the list
    #this process is repeated until all names have been printed
    #this is known as a "for loop"
    #the loop variable (x in this case) is used to access each item in the list one by one
    #the loop variable can be any valid variable name, but it's common to use "x" for simplicity

    
# for x in "mississippi":
#         print(x)

# for x in names:
#     if x == "Sara":
#         break
#     print(x)

# for x in names:
#     if x == "Sara":
#         continue
#     print(x)

# for x in range(4):
#     print(x)

# for x in range(2,4):
#     print(x)

for x in range(0,100, 5):
    print(x)
else:
    print("Glad that\'s over")


names = ["Dave", "Sara", "John"]
actions = ["codes", "eats", "sleeps"]

# for name in names:
#     for action in actions:
#         print(name + " " + action + ".")
        
for action in actions:
    for name in names:
        print(name + " " + action + ".")