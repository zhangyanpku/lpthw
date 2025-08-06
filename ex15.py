from sys import argv

script, filename = argv

txt = open(filename) #create a file object

print(f"Here's your file {filename}:")
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())

txt.close() #It's important to close the file when you're done with it.
txt_again.close() #It's important to close the file when you're done with it.