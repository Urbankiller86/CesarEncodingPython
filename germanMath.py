c0=int(input("Echa el numero cabron: "))
counter=0
while c0 != 1:
    if(c0%2==0):
        c0=c0/2
        print(c0)
    else:
        c0=3*c0 +1
        print(c0)
    counter=counter+1
print("Count: ",counter)