from sys import argv
from os.path import exists

# Simple python program copying contents of one file to another.

# Set our command line arguments
script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}.")

# Open the file
in_file = open(from_file)
# Read the data
in_data = in_file.read()

# Get the length
print(f"The input file is {len(in_data)} bytes long.")
# Make sure file exist if not create one.
print(f"Does the output file exists? {exists(to_file)}")
print("Ready; Hit RETURN to continue. CTRL-C to abort.")
input()

# write data to file
out_file = open(to_file, 'w')
out_file.write(in_data)

print("Alright all done.")

out_file.close()
in_file.close()
