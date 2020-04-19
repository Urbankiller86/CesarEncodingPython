from encodingFuctions import encode
from encodingFuctions import decode
import os.path

location=input("Insert file path: ")
checkLocation = True
while checkLocation:
    if os.path.isfile(location):
        with open(location, 'r') as file:
            data = file.read().replace('\n', '')
        checkLocation=False
    else:
        location=input("Insert a valid path")
        
checkNumber=True
while checkNumber:
    try:
        option=input("1 to encode. Other number to decode: ")
        if int(option) == 1:
            data=data.upper()
            secretMessage=encode(data)
            writer=open(location,"w+")
            writer.write(secretMessage)
            writer.close()
            checkNumber=False
        else:
            originalMessage=decode(data)
            writer=open(location,"w+")
            writer.write(originalMessage)
            writer.close
        checkNumber=False
    except:
        checkNumber=True