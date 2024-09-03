def intToRoman(num : int) -> str:
    Roman_num = {
        "M" : 1000,
        "CM" : 900,
        "D" : 500,
        "CD" : 400,
        "C" : 100,
        "XC" : 90,
        "L" : 50,
        "XL" : 40,
        "X" : 10,
        "IX" : 9,
        "V" : 5,
        "IV" : 4,
        "I" : 1,
    }
    string = ""
    for roman , value in Roman_num.items():
        while num >= value:
            num -= value 
            string += roman
        print(string , num)
    print(string)
    return string 
print(intToRoman(124))