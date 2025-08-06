i = 0
numbers = []

def floop(n,numbers):
    i = 0
    while i < n:
        print(f"At the top i is {i}")
        numbers.append(i)
        i = i + 1
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")
    return numbers
numbers1 = floop(10,numbers)

print("The numbers: ")

for num in numbers1:
    print(num)
