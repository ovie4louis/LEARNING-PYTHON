
name = "Dave"
count = 1



def another():

    color = "Red"
    global count
    count += 1
    print(count)
    def greeting(name):
        nonlocal color
        color = "Blue"
        print(color)
        print(name)
    greeting("Dave")

another()