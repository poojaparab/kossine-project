def convert(value):
    global c
    c = " "


    roman = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    numeral = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    if (value <= 4000 and value >= 1):
        for i in range(0, len(numeral)):
            while (value >= numeral[i]):
                c = c + roman[i]
                value = value - numeral[i]
            i = i + 1
        print("roman numeral of given number is:" + c)
    else:
        print("number not valid")
    return c
convert(value = int(input("enter the number:")))

