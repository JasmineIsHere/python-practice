def getSevSegStr(number, minWidth = 0):
    number = str(number).zfill(minWidth) ##if you want to print "042" instead of just "42"

    rows = ["", "", ""]
    for i, numeral in enumerate(number):
        if numeral == '.': 
            #render the decimal point
            rows[0] += " "
            rows[1] += " "
            rows[2] += "."
            # continue
        elif numeral == "-":
            #render the negative sign
            rows[0] += "    "
            rows[1] += " __ "
            rows[2] += "    "
        elif numeral == "0":
            #render the 0
            rows[0] += " __ "
            rows[1] += "|  |"
            rows[2] += "|__|"
        elif numeral == "1":
            #render the 1
            rows[0] += "    "
            rows[1] += "   |"
            rows[2] += "   |"
        elif numeral == "2":
            #render the 2
            rows[0] += " __ "
            rows[1] += " __|"
            rows[2] += "|__ "
        elif numeral == "3":
            #render the 3
            rows[0] += " __ "
            rows[1] += " __|"
            rows[2] += " __|"
        elif numeral == "4":
            #render the 4
            rows[0] += "    "
            rows[1] += "|__|"
            rows[2] += "   |"
        elif numeral == "5":
            #render the 5
            rows[0] += " __ "
            rows[1] += "|__ "
            rows[2] += " __|"
        elif numeral == "6":
            #render the 6
            rows[0] += " __ "
            rows[1] += "|__ "
            rows[2] += "|__|"
        elif numeral == "7":
            #render the 7
            rows[0] += " __ "
            rows[1] += "   |"
            rows[2] += "   |"
        elif numeral == "8":
            #render the 8
            rows[0] += " __ "
            rows[1] += "|__|"
            rows[2] += "|__|"
        elif numeral == "9":
            #render the 9
            rows[0] += " __ "
            rows[1] += "|__|"
            rows[2] += " __|"
        
        if i != len(number) - 1:
            #render the space
            rows[0] += " "
            rows[1] += " "
            rows[2] += " "
        
    return '\n'.join(rows)

if __name__ == "__main__":
    print('''
A labeled seven-segment display, with each segment labeled A to G:

 __A__
|     |
F     B
|__G__|
|     |
E     C
|__D__|

Each digit in a seven segment display:
  __        __    __            __    __    __    __    __
 |  |   |   __|   __|   |__|   |__   |__      |  |__|  |__|
 |__|   |  |__    __|      |    __|  |__|     |  |__|   __|
 
''')
    num = input("what number to print? ")
    print( getSevSegStr(num))

