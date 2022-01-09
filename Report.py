from WebScrapper import *


"""goal to make gradebook more organized"""



maindict = dict()
assigndict = dict()
quizdict = dict()
labdict = dict()
examdict = dict()


def is_float(element):
    try:
        float(element)
        return True
    except ValueError:
        return False


def percent(x, y):
    if is_float(x) and is_float(y):
        grade = str((float(x) / float(y)) * 100)
        if grade[grade.index(".") + 1:] == "0":
            grade = int(grade[:-2])
        else:
            grade = round(float(grade), 2)
        return grade
    return "-"  # fix this for decimals not workking rn


for x in range(len(nameslist)):
    name = nameslist[x]
    grade = percent(markslist[x], outoflist[x])
    maindict[name] = grade

for name in sorted(nameslist):  # maybe change to function
    regversion = maindict[name]
    strversion = str(regversion)
    if "assignment" in name.lower():
        assigndict[name] = strversion + "%"
    if "quiz" in name.lower():
        quizdict[name] = strversion + "%"
    if "lab" in name.lower():
        labdict[name] = strversion + "%"
    if ("midterm" in name.lower()) or ("final" in name.lower()) or ("test" in name.lower()):
        examdict[name] = strversion + "%"
try:
    count = 0
    for x in range(len(className) - 3):
        if className[x].isdigit():
            count += 1
            if count == 4:
                if className[x + 1] == ' ':
                    endName = x + 1  # this means up to and not including, important for slicing
                else:
                    endName = x + 2  # same thing, makes sure to end at space char

    className = className[6:endName]
except IndexError:
    className = input("Please enter classname: ")
except:
    print("Unknown Error please contact atekhaeseosa@gmail.com")
