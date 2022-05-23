def binary_to_hex(binary):
    length = len(binary)
    decimal = []
    temp = []
    counter = 0
    for ii in range(0,length):
        temp.append(binary[ii])
        counter += 1
        if(counter == 4):
            temp.reverse()
            temp_length = len(temp)
            Sum = 0
            for jj in range(0,temp_length):
                Sum += temp[jj]*(2**jj)
            decimal.append(Sum)
            temp = []
            counter = 0
    hex = []
    hex.append("0")
    hex.append("x")
    length = len(decimal)
    for ii in range (0,length):
        number = decimal[ii]
        if(number == 0):
            hex.append("0")
        elif(number == 1):
            hex.append("1")
        elif(number == 2):
            hex.append("2")
        elif(number == 3):
            hex.append("3")
        elif(number == 4):
            hex.append("4")
        elif(number == 5):
            hex.append("5")
        elif(number == 6):
            hex.append("6")
        elif(number == 7):
            hex.append("7")
        elif(number == 8):
            hex.append("8")
        elif(number == 9):
            hex.append("9")
        elif(number == 10):
            hex.append("a")
        elif(number == 11):
            hex.append("b")
        elif(number == 12):
            hex.append("c")
        elif(number == 13):
            hex.append("d")
        elif(number == 14):
            hex.append("e")
        elif(number == 15):
            hex.append("f")
    hex_string = "".join(hex)
    return hex_string


