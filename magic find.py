

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

