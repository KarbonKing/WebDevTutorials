#Python Fundamentals - Variables, Functions, Loops, Arithmetic Operations

#Variables
City = "Brooklyn"


#Functions
Always indent the commands within your funtions!!! DONT FORGET
def <FUNCTION>(Param1, Param2):
    global <Variable> #Global Variables can be called within functions using the following syntax

    print(Param1)
    print("Stuff" + Param2)
    #etc...


#If-Then functions
variable = True
if  variable == True:            #Or False
    print("Some Stuff")
#Check if certain words are located in strings
txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")


#Loops
for <LOOP> in range(<int>):
    print(stuff)
    print("More stuff")


#Division
#If you're dividing decimals (floats) you can use a double slash '//'
#to round the division to a whole number
9.5 / 2 = 4.75
9.5 // 2 = 4.0



#Modular Division - divides numbers and provides the remainder as the answer

9 % 3 = 0
10 % 3 = 1
