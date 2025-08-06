people = 30
cars = 40
truck = 15


if cars > people:
    print("We sould take the cars")

elif people < cars:
    print("We should not take the cars!")
else:
    print("We can't decide.")

if truck  > cars:
    print("Too many trucks")

elif truck < cars:
    print("Maybe we could take the trucks")
else:
    print("We still can't decide.")

if people > truck:
    print("let's take the trucks")
else:
    print("Fine. Let's stay at home.")