normalOrder=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
cesarOrder=['D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C']

def encode(originalText):
    encodedMessage=""
    lengtText=len(originalText)
    for a in range(lengtText):
        letter=originalText[a]
        for i in range(26):
            if(letter == str(normalOrder[i])):
                encodedMessage+=str(cesarOrder[i])
    return encodedMessage


def decode(encodedText):
    decodedMessage=""
    lengtText=len(encodedText)
    for a in range(lengtText):
        letter=encodedText[a]
        for i in range(26):
            if(letter == str(cesarOrder[i])):
                decodedMessage+=str(normalOrder[i])
    return decodedMessage