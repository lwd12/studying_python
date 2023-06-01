import time


"""
a = "a:b:c:d"
b = a.split(":")
print(b)

c = "#".join(b)
print(c)
"""

"""
phoneNumber = "000-1111-2222"
address = "1234567-1234567"
splita = phoneNumber.split("-")
splitb = address.split("-")
print(splita)
print(splitb)
"""
"""
my_list = []
my_list = [1, 2, 3, 4, 5]
my_list = ["A string", 23, 100.32, "o"]
my_list = [x + 100 for x in range(1, 11)]

print(my_list)
"""

"""
aa = []
aa.append(100)
aa.append(200)
aa.append(300)
aa.append(400)
print("리스트변수 크기는 %d" % len(aa))
print(aa)
bb = []
for i in range(0, 100):
    bb.append(i)
print(bb)

for a in range(100, 0, -5):
    print(a)
"""
"""
aa = [10, 20, 30, 40]
print("aa[-1]은 %d aa[-2]는 %d" % (aa[-1], aa[-2]))
print(aa[0:2])
print(aa[2:4])
print(aa[0:])

my_list = [0, 1, 2, 3, 4, 5]
print(id(my_list))
my_list[1:3] = ["A", "B", "C"]
print(id(my_list))

print(my_list)
"""
"""
my_list = [0, 1, 2, 3, 4, 5]
print(id(my_list))

my_list[1:5] = ["A", "B"]
print(id(my_list))
print(my_list)
"""
"""
a = []
for i in range(1, 101):
    s = str(i)
    b = "(x)"

    count = 0
    for x in s:
        if (x == "3") or (x == "6") or (x == "9"):
            count = 1

    if count == 1:
        print(b, end=" ")
    else:
        print(s, end=" ")
"""

"""
aa = [30, 10, 20]
print("현재의 리스트: %s" % aa)
aa.append(40)

print("append의 리스트: %s" % aa)
aa.pop()

print("pop의 리스트: %s" % aa)
aa.sort()

print("sort의 리스트: %s" % aa)
aa.reverse()

print("reverse의 리스트: %s" % aa)

aa.insert(2, 222)
print("insert(2,222)의 리스트: %s" % aa)
print("20값의 위치 :%d" % aa.index(20))
aa.remove(222)
print("remove(222)의 리스트: %s" % aa)
aa.extend([77, 88, 77])
print("extend([77,88,77])의 리스트: %s" % aa)
print("77값의 개수 %d" % aa.count(77))
"""
"""
my_list = ["python", "beyoun", "hello", "compiler", "apple", "Apple"]
my_list.sort()
print(my_list)
"""
"""
a = [1, 2, 3]
print(id(a))

a = a + [4, 5]
print(id(a))
print(a)

b = [1, 2, 3]
print(id(b))

b.extend([4, 5])
print(id(b))
print(b)
"""
# aa = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 19, 11, 12]]
# print(aa[0])
# print(aa[0][0])
# print(aa[1][2])
# print(aa[1][1])

# str = "파이썬 문자열"
# print(str[0])
# print(str[-1])

# card = "red", 4, "python", True
# print(card)
# print(card[1])

# card = "red", 4, "python", True
# a, b, c, d = card
# print(a)
# print(b)
# print(c)
# print(d)
# d = False
# print(d)

"""
s = set()
s = {100, 55, 1, 1, 1, 1, 2, 3}
print(s)

k = {5, 6, 7}
k.add(1)
print(k)

A = {0, 2, 4, 6, 8}
B = {1, 2, 3, 4, 5}
print("합집합 :", A | B)
print("교집합 :", A & B)
print("차집합 :", A - B)
print("대칭차집합 :", A ^ B)
"""

d = {}
d = dict()
d = {
    "바나나": "외떡잎식물 생각목 파초과 바나나속에 속하는 식물의 총칭",
    "아이언맨": "여심을 사로잡는 매력적인 미소의 백만장자 플레이보이 토니 스타크",
    123: 456,
}

print(d["바나나"])


d1 = {"one": 1, "two": 2, "three": 3}
d2 = dict({"three": 3, "one": 1, "two": 2})
d3 = dict({"one": 1, "three": 3}, two=2)
d4 = dict(one=1, two=2, three=3)
d5 = dict([(2, "two"), ("one", 1), ("three", 3)])
d6 = dict(zip(["one", "two", "three"], [1, 2, 3]))
d7 = {"번호": 10, "성명": "코난", "나이": 23, "사는곳": "서울"}
print(d7["나이"])
d["직업"] = "탐정"
print(d2.keys())

print(d.values())
print(d6)


# a = {"A": 90, "B": 80, "c": 38}

# print(a["A"])
# print(a["B"])
# print(a["C"])
# print(a.get("C"))

# user_input = "65,45,2,3,45,8"
# sum = 0
# a = user_input.split(",")
# for b in a:
#     sum += int(b)
# print(sum)

"""
def draw_pyramid(num_lines):
    for i in range(1, num_lines + 1):
        for j in range(num_lines - i):
            print(" ", end="")
        for c in range(i * 2 - 1):
            print("*", end="")
        print()


draw_pyramid(5)
"""

"""
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fib(n - 2) + fib(n - 1)


print(fib(40))
"""
"""
fruits = []
fruits.append("Guava")
fruits.append("Durian")
fruits.append("Strawberry")
fruits.append("PineBerry")
fruits.append("Lime")

f = open("fruit.txt", "w")
for fruit in fruits:
    f.write(fruit)
    f.write("\n")
f.close


f = open("fruit.txt", "r")  # r 읽기모드
fruits = f.readlines()
f.close()
print(fruits)


r_fruits = []
for f in fruits:
    r_fruits.append(f.replace("\n", ""))
print(r_fruits)
"""
"""
f = open("sample.txt")
lines = f.readlines()
f.close()
print(lines)

r_fruits = []
average = 0
for f in lines:
    r_fruits.append(f.replace("\n", ""))
    average += int(f)
average = average / len(lines)
print(average)
f = open("result.txt", "w")
f.write(str(average))
f.close()
"""

"""
fruits = []
fruits.append("Guava")
fruits.append("Durian")
fruits.append("Strawberry")
fruits.append("PineBerry")
fruits.append("Lime")
filename = time.strftime("%Y %m %d_%H %M %S")
print(filename)

f = open(filename + ".txt", "w")
for fruit in fruits:
    f.write(fruit)
    f.write("\n")
f.close()
"""

"""
try:
    f = open("sample1.txt")
    lines = f.readlines()
    a = 0
    f.close()
except FileNotFoundError:
    print("파일이 없습니다. 파일명을 확인하세요")
"""

count = 0
aa = []
for aa in range(1, 101):
    aa = str(aa)
    if (aa == "3") or (aa == "6") or (aa == "9"):
        count = 1
    if count == 1:
        aa.append("(x)")
    print(aa, end=" ")
