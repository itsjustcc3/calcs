import sys
while True:
    chance = float(input("what is the original dropchance "))
    magicfind = float(input("what is your magic find just the number"))
    chance = chance * (1+(magicfind/100)/100)

    print (f"""

        =====================================
        |                                   |
        |                                   |
        |      Chance: {chance:.02}                  |
        |                                   |
        |                                   |
        =====================================



        """)
    choice = input("do you want another calculation y/n ")
    if choice == n:
        print("Stopping....")
        sys.exit(0)
    else:
        print("Ok running program again...")

