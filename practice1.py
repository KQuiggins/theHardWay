from sys import argv

# Python program opening files

script, filename = argv

with open(filename) as txt:
    print(f"Here's your file {filename}")
    print(txt.read())

print("Type the filename again")
file_again = input(">")

with open(filename) as txt_again:
    print(txt_again.read())
