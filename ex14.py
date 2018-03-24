from sys import argv

script, user_name = argv
prompt=">>> "
print(f"Hey! {user_name}, How are you doing?")
greeting = input(prompt)
print(f"What's your age, {user_name}?")
age= input(prompt)

print(f"""
So! {user_name}, you are doing {greeting},
and your age is {age}
""")
