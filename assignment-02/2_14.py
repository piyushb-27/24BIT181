'''
Name: Piyush Bajaj
Roll no: 24BIT181
Branch: Information and Communication Technology (ICT)
'''


# 14. Marks, total, average, pass/fail, grade using if-else
m1 = 75
m2 = 65
m3 = 38
total = m1 + m2 + m3
average = total / 3
print("total:", total)
print("average:", average)

if m1 <= 39 or m2 <= 39 or m3 <= 39:
    print("fail")
else:
    print("pass")

def grade(m):
    if m == "Absent":
        return "NA"
    elif m <= 39:
        return "F"
    elif m <= 44:
        return "P"
    elif m <= 49:
        return "C"
    elif m <= 54:
        return "B"
    elif m <= 59:
        return "B+"
    elif m <= 69:
        return "A"
    elif m <= 79:
        return "A+"
    elif m <= 100:
        return "O"
    else:
        return "Invalid"

print(grade(m1))
print(grade(m2))
print(grade(m3))
