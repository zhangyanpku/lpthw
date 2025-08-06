ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(" ")
more_stuff = ["Day", "Night","Song","Frisbee","Corn","Banana","Girl","Boy"]

while len(stuff) != 10:
    next_one =more_stuff.pop() #.pop([index]) method is used to remove and return an element from a list or dictionary
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")
    
print("There we go:", stuff)

print(stuff[1])
print(stuff[-1]) #print the last item in the list
print(stuff.pop()) #If no index is specified, it removes and returns the last element.
print(" ".join(stuff)) #concatenate the elements of an iterable into a string
print('#'.join(stuff[3:5])) #Including the first index, excluding the last index, similar to range.