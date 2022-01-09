import openpyxl

from Report import *
from openpyxl import *
from openpyxl.styles import Font
from openpyxl.worksheet.table import Table, TableStyleInfo
from openpyxl.worksheet.dimensions import ColumnDimension
import random

""" Functions for Excel Worksheet """

def autofitColumns():
    letters = 'ABCDEFGHIJ'  # to add more
    for x in range(len(letters)):
        each_letter = letters[x]
        ws.column_dimensions[each_letter].auto_size = True
def makeTableHeaders():
    letters = 'ABCDEFGHIJ'  # to add more
    count = 0

    if len(assigndict) > 0:
        ws[str(letters[count]) + "8"] = "AssignmentName"
        ws[str(letters[count + 1]) + "8"] = "AssignmentGrade"
        count += 2
    if len(quizdict) > 0:
        ws[str(letters[count]) + "8"] = "QuizName"
        ws[str(letters[count + 1]) + "8"] = "QuizGrade"
        count += 2
    if len(labdict) > 0:
        ws[str(letters[count]) + "8"] = "LabName"
        ws[str(letters[count + 1]) + "8"] = "LabGrade"
        count += 2
    if len(examdict) > 0:
        ws[str(letters[count]) + "8"] = "ExamName"
        ws[str(letters[count + 1]) + "8"] = "ExamGrade"

    return letters[count + 1]


def addToRows():
    letters = 'ABCDEFGHIJK'  # to add more
    l_count = 0
    num_count = 9
    max = 0

    if assigndict:
        for assignment in assigndict:
            # bolding names
            aName = ws[str(letters[l_count]) + str(num_count)]
            aName.font = Font(bold=True)
            aName.value = assignment

            ws[str(letters[l_count + 1]) + str(num_count)] = assigndict[assignment]
            num_count += 1
        if num_count > max:
            max = num_count

        num_count = 9
        l_count += 2

    if quizdict:
        for quiz in quizdict:
            aName = ws[str(letters[l_count]) + str(num_count)]
            aName.font = Font(bold=True)
            aName.value = quiz

            ws[str(letters[l_count + 1]) + str(num_count)] = quizdict[quiz]
            num_count += 1
        if num_count > max:
            max = num_count
        num_count = 9
        l_count += 2

    if labdict:
        num_count = 9
        for lab in labdict:
            aName = ws[str(letters[l_count]) + str(num_count)]
            aName.font = Font(bold=True)
            aName.value = lab

            ws[str(letters[l_count + 1]) + str(num_count)] = labdict[lab]
            num_count += 1
        if num_count > max:
            max = num_count

        num_count = 9
        l_count += 2

    if examdict:
        for exam in examdict:
            aName = ws[str(letters[l_count]) + str(num_count)]
            aName.font = Font(bold=True)
            aName.value = exam

            ws[str(letters[l_count + 1]) + str(num_count)] = examdict[exam]
            num_count += 1
        l_count += 2
        if num_count > max:
            max = num_count
        l_count += 2

    return str(max - 1)


"""Iterating data into Excel table"""
try:
    true = True
    while true:
        exsting_or_new = input("Are you adding to a existing Excel workbook (y/n): ")
        if exsting_or_new.lower() == "y":
            try:
                file = input("Enter filename (not including '.xlsx'): ")
                wb = load_workbook(file + ".xlsx")
                true = False
                ws = wb.create_sheet(className)
            except FileNotFoundError:
                print("Sorry unable to find the Excel file you have entered. Please try again")

        elif exsting_or_new.lower() == "n":
            file = input("What name would you like to save your workbook to? (not including '.xlsx'): ")
            wb = Workbook()
            ws = wb.active
            true = False
        else:
            print("Invalid entry, please try again.")

    # creating excel sheet
    # modifying existing workbook, to create workbook its different function
    # how to start sheet
    ws.title = className  # names sheet

    # names the Grade Report title
    ws.merge_cells('A1:F5')
    title = ws["A1"]
    title.value = "Grade Report for " + className
    title.font = Font(size=15,italic=True,bold=True, underline='single')

    max_column = makeTableHeaders()  # makes the table headers
    max_row = addToRows()
    autofitColumns()

    example = ws['J3']
    example.value = "slkajflksjdfklajfklajf"
    '''    try:
        randomNum = random.randint(0, 10000)
        tab = Table(displayName="GradesTablev" + str(randomNum),
                    ref="A8:" + max_column + max_row)  # calling header value calls last value form makingHeaders()
    except ValueError:
        randomNum = random.randint(0, 10000)
        tab = Table(displayName="GradesTablev" + str(randomNum),
                    ref="A8:" + max_column + max_row)

    # Add a default style with striped rows and banded columns
    style = TableStyleInfo(name="TableStyleMedium9", showFirstColumn=False,
                           showLastColumn=False, showRowStripes=True, showColumnStripes=True)
    tab.tableStyleInfo = style
    ws.add_table(tab)
    '''
    wb.save(file + ".xlsx")

except PermissionError:
    print("Unable to convert to Excel file. \nMake sure the workbook is closed and try again.")

except FileNotFoundError:
    print("Sorry unable to find the Excel file you have entered. Please try again")

except ValueError:
    print("Code Error. Please try again.")

