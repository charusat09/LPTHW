from sys import argv

script, file_name = argv
prompt = ">>> "
print("""
I am going to delete your file.
If you are not sure then hit Ctrl + C or,
hit return !!!
""")
input(prompt)
print("I am reading your file, hold on........")
print("I'm done... your file is going to be deleted, are you sure???")
input(prompt)
target = open(file_name, "w")
target.truncate()

print("""
Now, let's add some contents to it.
I will need three lines
""")
line1 = input(f"{prompt} Enter line1: ")
line2 = input(f"{prompt} Enter line2: ")
line3 = input(f"{prompt} Enter line3: ")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

target.close()
target = open(file_name)
print(f"your final version!!!!")
print(target.read())
