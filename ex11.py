print("How old are you?", end = ' ') # Use end=' ' to allow a person to input something, not end the line but with the input on the same line
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()

print(f"So you're {age} old, {height} tall and {weight} heavy.")
data = input("Enter your name,age and height separated by spaces:").split()
name1=data[0]
age1=int(data[1])
height1=float(data[2])
print(f"Name: {name1}, Age: {age1}, Height: {height1}")
# Handling Errors
try:
    age = int(input("Enter your age: "))
    print("You are " + str(age) + " years old.")
except ValueError:
    print("Please enter a valid number.")