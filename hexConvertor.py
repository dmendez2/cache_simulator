def hex_to_binary(hex_string):
    binary = []
    length = len(hex_string)
    for ii in range(2,length):
       char = hex_string[ii]
       if(char == '0'):
           binary.append(0)
           binary.append(0)
           binary.append(0)
           binary.append(0)
       elif(char == '1'):
           binary.append(0)
           binary.append(0)
           binary.append(0)
           binary.append(1)
       elif(char == '2'):
           binary.append(0)
           binary.append(0)
           binary.append(1)
           binary.append(0)
       elif(char == '3'):
           binary.append(0)
           binary.append(0)
           binary.append(1)
           binary.append(1)
       elif(char == '4'):
           binary.append(0)
           binary.append(1)
           binary.append(0)
           binary.append(0)
       elif(char == '5'):
           binary.append(0)
           binary.append(1)
           binary.append(0)
           binary.append(1)
       elif(char == '6'):
           binary.append(0)
           binary.append(1)
           binary.append(1)
           binary.append(0)
       elif(char == '7'):
           binary.append(0)
           binary.append(1)
           binary.append(1)
           binary.append(1)
       elif(char == '8'):
           binary.append(1)
           binary.append(0)
           binary.append(0)
           binary.append(0)
       elif(char == '9'):
           binary.append(1)
           binary.append(0)
           binary.append(0)
           binary.append(1)
       elif(char == 'a' or char == 'A'):
           binary.append(1)
           binary.append(0)
           binary.append(1)
           binary.append(0)
       elif(char == 'b' or char == 'B'): 
           binary.append(1)
           binary.append(0)
           binary.append(1)
           binary.append(1)
       elif(char == 'c' or char == 'C'):
           binary.append(1)
           binary.append(1)
           binary.append(0)
           binary.append(0)
       elif(char == 'd' or char == 'D'):
           binary.append(1)
           binary.append(1)
           binary.append(0)
           binary.append(1)
       elif(char == 'e' or char == 'E'):
           binary.append(1)
           binary.append(1)
           binary.append(1)
           binary.append(0)
       elif(char == 'f' or char == 'F'):
           binary.append(1)
           binary.append(1)
           binary.append(1)
           binary.append(1)
    return binary