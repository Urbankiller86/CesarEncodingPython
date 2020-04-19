from encodingFuctions import encode
from encodingFuctions import decode

location=input("Insert file path: ")
with open(location, 'r') as file:
    data = file.read().replace('\n', '')
option=input("1 to encode. Other number to decode: ")
if int(option) == 1:
    data=data.upper()
    secretMessage=encode(data)
    writer=open(location,"w+")
    writer.write(secretMessage)
    writer.close()
else:
    originalMessage=decode(data)
    writer=open(location,"w+")
    writer.write(originalMessage)
    writer.close
