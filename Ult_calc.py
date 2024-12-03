# Levi Ray and Ahcene Amara Calculators
import sys
import math
import time
# Declare pi as global variable
pi = math.pi
# Define a menu to call other functions from
def menu():
    print("         menu")
    print("_______________________")
    print("|                     |")
    print("|   1 for math        |\n|   2 for grade       |\n|   3 for percent     |\n|   4 for geometric   |\n|   5 for algebraic   |\n|   6 for Trigimetric |\n|   7 for fincial     |\n|   8 for hypixel     |\n|   0 to stop         |")
    print("_______________________")



    calcChoice = int(input("What Kind of calc do you want "))
    print("\n\n\n")
    return calcChoice # This is how we pull calcChoice out of the function
def math_():
    choice = int(input("how many numbers? "))
    choices = []


    for x in range(choice):
        choices.append((float(input("Enter Number {}: ".format(x + 1)))))


    addition_result = choices[0]
    subtract_result = choices[0]
    multiply_result = choices[0]
    division_result = choices[0]


    for number in choices[1:]:
        addition_result = addition_result + number
        subtract_result = subtract_result - number
        multiply_result = multiply_result * number


        if (number == 0):
            print("can not divided by zero"); exit(0)


        division_result = division_result / number
    print('_______________________________')
    print("| Addition Result:", str(addition_result),"        |")
    print("| Subtract Result:", str(subtract_result),"        |")
    print("| Multiply Result:", str(multiply_result),"        |")
    print("| division Result:", str(division_result),"        |")
    print("_______________________________")
def grade():
    points = (float(input("How many points do you have? ")))
    tpoints = (float(input("Out of how many points ")))
    precent = points / tpoints * 100
    print("___________________")
    print(f"|    %{precent:.2f}          |")
    if precent >= 97:
        print("|       A+        |")
    elif precent >= 93:
        print("|       A         |")
    elif precent >= 90:
        print("|       A-        |")
    elif precent >= 87:
        print("|       B+        |")
    elif precent >= 83:
        print("|       B         |")
    elif precent >= 80:
        print("|       B-        |")
    elif precent >= 77:
        print("|       C+        |")
    elif precent >= 73:
        print("|       C         |")
    elif precent >= 70:
        print("|       C-        |")
    elif precent >= 67:
        print("|       D+        |")
    elif precent >= 63:
        print("|       D         |")
    elif precent >= 60:
        print("|       D-        |")
    elif precent <= 60:
        print("|       F         |")
    print("___________________")
def percent():
    print()
    print("1 for finding percent\n2 for finding amount of number ")
    choice = int(input("what type of prolem "))
    if choice == 1:
        num_one = (float(input("What is the first number ")))
        num_two = (float(input("Out of what number ")))
        percent = num_one / num_two * 100
        print("___________________")
        print("|  Percent: %",percent,"|")
        print("___________________")
        print()
    else:
        num_one = (float(input("What is the percentage %")))
        num_two = (float(input("Of what number ")))
        percent = num_one * num_two / 100
        print ("__________________")
        print("Number:", percent)
        print("___________________")
def geometric():
    print()
    print("1 for circle\n2 for triangle\n3 for square")
    choice = int(input("What shape "))
    # Circle
    if choice == 1:
        print()
        print("1 for area \n2 for circumference\n3 for radius\n4 for diamiter")
        print("________________")
        choice_two = int(input("What type of problem "))
        print("________________")
   
    # Circle area
    if choice == 1 and choice_two == 1:
        radius = (float(input("Whats the radius ")))
        area = (pi * radius * radius)
        print()
        print("Area:", area)
        print("________________")
    # Circle circumference
    elif choice == 1 and choice_two == 2:
        radius = (float(input("What is the radius ")))
        circumference = 2 * pi * radius
        print()
        print("circumference:",circumference)
        print("________________")
    # Circle radius
    elif choice == 1 and choice_two == 3:
        circumference = (float(input("Whats the circumference ")))
        radius = circumference / 2 * pi
        print()
        print("Radius:",radius)
        print("________________")
    # Square diameter
    elif choice == 1 and choice_two == 4:
        radius = (float(input("What is the radius ")))
        diameter = radius * 2
        print()
        print("Diameter:",diameter)
        print("________________")
    # Triangle
    if choice == 2:
        print()
        print("1 for area\n2 for height\n3 for base\n4 for perimeter ")
        choice_two = int(input("What type of problem "))
        print("________________")
    # Triange Area
    if choice == 2 and choice_two == 1:
        print()
        base = (float(input("What is the base ")))
        height = (float(input("What is the height ")))
        area = 0.5 * base * height
        print()
        print("Area:", area)
        print("________________")
    # Triangle height
    elif choice == 2 and choice_two == 2:
        print()
        base = (float(input("What is the base ")))
        area = (float(input("What is the area ")))
        height = 2 * area / base
        print()
        print("Height:",height)
        print("________________")
    # Triangle base
    elif choice == 2 and choice_two == 3:
        print()
        height = (float(input("What is the height ")))
        area = (float(input("What is the area ")))
        base = 2 * area/height
        print()
        print("Base:",base)
        print("________________")
        side_1 = (float("What is side one "))
        side_2 = (float("What is side two "))
        side_3 = (float("What is side three "))
        perimeter = side_1 + side_2 + side_3
        print()
        print("Perimeter:",perimeter)
        print("________________")
    # Square
    if choice == 3:
        print()
        print("1 for area\n2 for diagonal\n3 for perimeter")
        print("________________")
        choice_two = int(input("What type of problem "))
    # Square area
    if choice == 3 and choice_two == 1:
        side = (float(input("Whats the length of the side ")))
        area = side * side
        print()
        print("Area:", area)
        print("________________")
    # Square diagonal
    elif choice == 3 and choice_two == 2:
        area = (float(input("What is the area ")))
        diagonal = math.sqrt(2 * area)
        print()
        print("Diagonal:", diagonal)
        print("________________")
    # Square perimeter
    elif choice == 3 and choice_two == 3:
        area = (float(input("What is the area ")))
        perimeter = 4 * area
        print()
        print("Perimeter:",perimeter)
        print("________________")
def algebraic():
    print("Not Finished")
    print()
    print("1 to simplify an expression\n2 to solve equation\n3 for inequality")
    choice = int(input("What type of problem "))
    if choice == 1:
        print()
        constants = float(input("What are the constants "))
        variables = input("What are the variables ")
       
        # step if x in string
    
        # step 2 find index of x


        # step 3 extract value to the left of x
       




        # coefficent = float(input("What are the coefficents "))      
def trig():
    # Ahcene Amara - trig function
    print()
    problem = input("1 for sin\n2 for cos\n3 for tan\n4 for cosec\n5 sec\n6 cot  " )
    #sin calc
    if problem == 1:
        opp = int(input("what is the side opposite to theta "))
        hyp = int(input("what is the hypotenuse "))
        sin = opp/hyp
        print("Sin:",sin)
    #why god do you make coding so complicated
    elif (problem == "cosec"):
        opp = int(input("what is the side opposite to theta "))
        hyp = int(input("what is the hypotenuse "))
        sin = opp/hyp
        cosecp1 = 1/sin
        print (cosecp1)
    #cos
    if (problem == "cos"):
        adj = int(input("what is the number adjacetent to the theta"))
        hyp = int(input("what is the hypotenus"))
        cos = adj/hyp
        print (adj/hyp)  
    #is this a joke god?
    elif (problem == "sec"):
        adj = int(input("what is the number adjacetent to the theta"))
        hyp = int(input("what is the hypotenus"))
        cos = adj/hyp
        sec = 1/cos
        print(sec)
    #tan
    if (problem == "tan"):
        opp = int(input("what is the side opposite to theta "))
        adj = int(input("what is the number adjacetent to the theta"))
        tan = opp/adj
        print(opp/adj)
    #my existance is to spite you
    elif (problem == "cot"):
        opp = int(input("what is the side opposite to theta "))
        adj = int(input("what is the number adjacetent to the theta"))
        tan = opp/adj
        cot= 1/tan
def fincial():
    print("_______________________")
    print("1 for Stock dividend rate")    
    choice = input("What kind of problem")
    if choice == 1:
        print("_______________________")
        stockPrice = float(input("What is the stock price "))
        dividendYield = float(input("What is the dividend yield "))
        answer = dividendYield/stockPrice * 100
        print("Answer: ",answer)
def hypixel():
    #vincents a hoe
    while True:
        chance = float(input("what is the original dropchance "))
        magicfind = float(input("what is your magic find just the number "))
        chance = chance * (1+(magicfind/100)/100)

        print (f"""

            =====================================
            |                                   |
            |                                   |
            |      Chance: {chance:.02f}               |
            |                                   |
            |                                   |
            =====================================



            """)
        choice = input("do you want another calculation y/n ")
        if choice == "n":
            print("Stopping....")
            sys.exit(0)
        else:
            print("running program again...")

calcChoice = menu()
while True:
    if calcChoice == 1:
        math_()
    if calcChoice == 2:
        grade()
    if calcChoice == 3:
        percent()
    if calcChoice == 4:
        geometric()
    if calcChoice == 5:
        algebraic()
        print("Not finished ")
    if calcChoice == 6:
        trig()
    if calcChoice == 7:
        fincial()
    if calcChoice == 8:
        hypixel()
    if calcChoice == 0:
        sys.exit(0)
    if calcChoice < 0 or calcChoice > 8:
        print("Please enter correctly")
    time.sleep(5)
    calcChoice = menu()