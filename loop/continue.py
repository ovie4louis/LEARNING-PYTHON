#while loop with continue statement
value =1

while value <= 10:

    value += 1
    if value == 5:
        continue
    print(value)
else:
    print("the value is now equal to " + str(value))