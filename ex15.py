from sys import argv

script, file_name = argv
prompt = ">>> "
print("Here is the your file ", file_name)
file_one = open(file_name)
print(file_one.read())

loop = True

while loop:
  print(f"{prompt}Do you want to open new file?")
  ans = input(prompt)
  if ans == 'yes':
    another_file_name = input(f"{prompt}Enter file name :")
    another_file = open(another_file_name)
    print(another_file.read())
  else:
    loop = False
