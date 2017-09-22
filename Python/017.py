'''Number letter counts'''
teens = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen"
}

dozens = {
    2: "twenty",
    3: "thirty",
    4: "forty",
    5: "fifty",
    6: "sixty",
    7: "seventy",
    8: "eighty",
    9: "ninety"
}

#working from 1 to 9999
def fromNumbertoWords(n, words=""):
    length = len(str(n))
    if ((length == 2 and n < 20) or length == 1):
        words += teens[n]
    elif (length == 2 and n >= 20):
        words += dozens[n / 10]
        if(n % 10 != 0):
            words += teens[n % 10]
    elif (length == 3 and n % 100 == 0):
        words += teens[n / 100]
        words += "hundred"
    elif (length == 3 and n % 100 != 0):
        words += teens[n / 100]
        words += "hundredand"
        temp = n % 100
        return fromNumbertoWords(temp, words)
    elif (length == 4 and n % 1000 == 0):
        words += teens[n / 1000]
        words += "thousand"
    elif (length == 4 and n % 1000 != 0):
        words += teens[n / 1000]
        words += "thousand"
        temp = n % 1000
        return fromNumbertoWords(temp, words)
    return words


def sumNumbersChars(n):
    letters = 0
    for i in range(1, n + 1):
        letters += len(fromNumbertoWords(i))
    print letters


sumNumbersChars(1000)
