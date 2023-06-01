import math

dic = {
    ".-": "A",
    "-...": "B",
    "-.-.": "C",
    "-..": "D",
    ".": "E",
    "..-.": "F",
    "--.": "G",
    "....": "H",
    "..": "I",
    ".---": "J",
    "-.-": "K",
    ".-..": "L",
    "--": "M",
    "-.": "N",
    "---": "O",
    ".--.": "P",
    "--.-": "Q",
    ".-.": "R",
    "...": "S",
    "-": "T",
    "..-": "U",
    "...-": "V",
    ".--": "W",
    "-..-": "X",
    "-.--": "Y",
    "--..": "Z",
}
DICT = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
}

"""
def english(word):
    morse_code = []
    for s in word:
        if s == " ":
            morse_code.append(" ")
        else:
            morse_code.append(DICT[s.upper()] + " ")
    return "".join(morse_code)


print(english("HELLO"))


def morse(src):
    result = []
    for word in src.split(" "):
        for char in word.split(" "):
            result.append(dic[char])
        result.append(" ")
    return "".join(result)


print(morse("-.-- --- ..- .- .-. . .- --. . -. .. ..- ..."))
print(english("hello"))
"""

"""
class Circle:
    def __init__(self, x, y, r):
        self.r = r
        self.x = x
        self.y = y

    def is_inside(self, x1, y1):
        r1 = math.pow(self.r, 2)
        ans = math.pow(x1 - self.x, 2) + math.pow(y1 - self.y, 2)
        if ans < r1:
            return True
        else:
            return False


my_circle = Circle(1.0, 1.5, 0.8)
print(my_circle.is_inside(1.5, 0.9))  # True
print(my_circle.is_inside(0.4, 0.5))  # Fasle
"""

"""
class Calculator:
    def __init__(self, num):
        self.num = num

    def sum(self):
        sum1 = 0
        for x in self.num:
            sum1 += x
        return sum1

    def avg(self):
        return self.sum() / len(self.num)

cal1 = Calculator([1, 2, 3, 4, 5])
print(cal1.sum())  # 15
print(cal1.avg())  # 3.0
cal2 = Calculator([6, 7, 8, 9, 10, 11])
print(cal2.sum())  # 51
print(cal2.avg())  # 8.5
"""


class MorseCodeTrans:
    def __init__(self):
        self.morse_dict = {
            "A": ".-",
            "B": "-...",
            "C": "-.-.",
            "D": "-..",
            "E": ".",
            "F": "..-.",
            "G": "--.",
            "H": "....",
            "I": "..",
            "J": ".---",
            "K": "-.-",
            "L": ".-..",
            "M": "--",
            "N": "-.",
            "O": "---",
            "P": ".--.",
            "Q": "--.-",
            "R": ".-.",
            "S": "...",
            "T": "-",
            "U": "..-",
            "V": "...-",
            "W": ".--",
            "X": "-..-",
            "Y": "-.--",
            "Z": "--..",
        }
        self.english_dict = {value: key for key, value in self.morse_dict.items()}

    def english_to_morse(self, english_text):
        morse_code = []
        for s in english_text:
            if s == " ":
                morse_code.append(" ")
            else:
                morse_code.append(self.morse_dict[s.upper()] + " ")
        return "".join(morse_code)

    def morse_to_english(self, morse_text):
        result = []
        for word in morse_text.split(" "):
            for char in word.split(" "):
                result.append(self.english_dict[char])
            result.append(" ")
        return "".join(result)


"""
morse_translator = MorseCodeTrans()
morse_text = morse_translator.english_to_morse("coding time")
english_text = morse_translator.morse_to_english(
    "-.-- --- ..- .- .-. . .- --. . -. .. ..- ..."
)

print("morse =", morse_text)
print("english = ", english_text)
"""
