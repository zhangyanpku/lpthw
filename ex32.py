the_count = [1,2,3,4,5]
fruits = ['apples','oranges','pears','apricots']
change = [1, 'pennies', 2, 'dimes',3, 'quarters']

#this first kind of for-loop goes through a list
for number in the_count:
    print(f"This is count {number}.")

for fruit in fruits:
    print(f"A fruit of type: {fruit}")

for i in change:
    print(f"I got {i}")
    
elements=[] #empty list
for i in range(0,6):    # i is >=0 and less than 6
    print(f"Adding {i} to the list.")
    elements.append(i)

for i in elements:
    print(f"Element was: {i}")

