def getSoundEx(str):
    charList = list(str.upper())
    soundExStr = charList[0]
    charList.pop(0)
    soundExCodes = {
        'aehiouwy' : False,
        'bfpv' : '1',
        'cgjkqsxz' : '2',
        'dt' : '3',
        'l' : '4',
        'mn' : '5',
        'r' : '6'
    }

    for item in charList:
        currentCode = item
        for key, value in soundExCodes.items():
            if currentCode in list(key.upper()):
                currentCode = value
        if currentCode and currentCode != soundExStr[-1]:
            soundExStr += currentCode

    return (soundExStr + '0000')[:4]
