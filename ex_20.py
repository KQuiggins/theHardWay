from sys import argv

# Arguments to be passed at command line
script, input_file = argv


# Function to print the entire document
def print_all(f):
    print(f.read())


# Go back to beginning of the file
def rewind(f):
    f.seek(0)


# print line number and that single line.
def print_a_line(line_count, f):
    print(line_count, f.readline())


# Open the file
current_file = open(input_file)


print("First let's print the entire file:\n")


# print the entire file
print_all(current_file)

print("Now let's rewind, kinda like a tape.")

# Rewind to beginning of file
rewind(current_file)

print("Now let's print three lines:")

# Mark current line as line 1
current_line = 1
# Print current line
print_a_line(current_line, current_file)

# Add 1 to current line
current_line = current_line + 1
# Print line 2
print_a_line(current_line, current_file)

# Add 1 to current line, makes this line 3
current_line = current_line + 1
# Print line 3
print_a_line(current_line, current_file)

current_file.close()
