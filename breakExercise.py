secretWord="chupacabra"
userWord=input("Insert a word")
while True:
    userWord=input("Insert another word")
    if userWord==secretWord:
        break
print("You've succesfully left the loop")