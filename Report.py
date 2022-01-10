from WebScrapper import *
"""goal to make gradebook more organized"""

maindict = dict()
assigndict = {"AssignmentName":"AssignmentGrade"}
quizdict = {"QuizName":"QuizGrade"}
labdict = {"LabName":"LabGrade"}
examdict = {"ExamName":"ExamGrade"}
otherdict = {"Name":"Grade"}

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
    return '-'  # fix this for decimals not workking rn


for x in range(len(nameslist)):
    name = nameslist[x]
    grade = percent(markslist[x], outoflist[x])
    maindict[name] = grade

    #yea
for name in sorted(nameslist): 
    regversion = maindict[name]
    strversion = str(regversion)
    if strversion != '-':
        if "assignment" in name.lower():
            assigndict[name] = strversion + "%"
        elif "quiz" in name.lower():
            quizdict[name] = strversion + "%"
        elif "lab" in name.lower():
            labdict[name] = strversion + "%"
        elif ("midterm" in name.lower()) or ("final" in name.lower()) or ("test" in name.lower()):
            examdict[name] = strversion + "%"
        else:
            otherdict[name] = strversion + "%"
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
