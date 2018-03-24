from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# we could do these two on one line, how?
indata = open(from_file).read()
print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()

# Notes:
# When I try to make this script shorter I get an error when I close the
# files at the end. You probably did something like this, indata =
# open(from_file).read(), which means you don’t need to then do
# in_file.close() when you reach the end of the script. It should already be
# closed by Python once that one line runs. 
