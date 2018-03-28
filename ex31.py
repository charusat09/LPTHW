print("""
1: Go to haven
2: Go to hell
Enter your choise: """)
prompt = "> "
choise1 = input(prompt)

if choise1 == "1":
    print("Welcome to hevan.....")
    print("""
    Now, make new choise
    1: if you want to go with ferry
    2: if you want to enjoy the music
    """)
    choise2 = input(prompt)
    if choise2 == "1":
        print("Ok wait for some time, ferry is on the way....")
    elif choise2 == "2":
        print("Your album is downloading......")
    else:
        print("You didn't make correct choise, go back to earth....")
elif choise1 == "2":
    print("Oh.. you are in hell now...")
    print("""
      Still, you have some choise,
      1: To be fried in hot oil
      2: To be fried in hot water
    """)
    choise3 = input(prompt)
    if choise3 == "1":
        print("Please wait, we are bioling oil...")
    elif choise3 == "2":
        print("Please wait, we are boiling water...")
    else:
        print("Sorry, you didn't make correct choise, now you need to be fried in both, oil and water, enjoy...")
else:
    print("It seems like you want to live more....")
