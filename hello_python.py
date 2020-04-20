""""
ProgramWithFriends v 0.1
by Seri    2020.04.18

Program was make for practice
"""
print ('Hello word \n*hello word*')      # made hsss
a = 3                                    # static value
b = 4                                    # static Value

print("It's an integer")
count = input("Write number = ")         # assign an input value
try:                                     # check value
    count = int(count)                   # if value integer
    print("Valid value", a + b + count)  # output this message and go to line 28
except ValueError:                       # if not integer
    print('Write again', end=" = ")      # output this message and start cycle

    while 1:                             # start cycle
        count = input()                  # loop execution condition
        try:                             # check value
            count = int(count)           # if value integer
            break                        # the cycle ends and go to line 26
        except ValueError:               # if not integer
            print("Write again", end=" = ")  # output this message and start cycle
    print("Valid value", a + b + count)  # output this message and go to line 28

handle = open(r"C:\Users\Urbankiller86\Desktop\perro.txt", "r")  #check file and download
data = handle.readlines()  #method read all file
print(data) #text output
handle.close()