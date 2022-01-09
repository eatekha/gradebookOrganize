from selenium import webdriver

link = input("Enter gradebook link: ")
username_user = input("Please enter your Western username: ")
password_user = input("Please enter your Western password: ") # to be changed

# gathering raw data
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get(link)
# how to open link

username = driver.find_element_by_name("eid")
username.send_keys(username_user)

password = driver.find_element_by_name("pw")
password.send_keys(password_user)  # can be changed to input

login = driver.find_element_by_name("submit")
login.click()

className = driver.title

gradeScores = driver.find_elements_by_class_name("gb-summary-grade-score")
names = driver.find_elements_by_class_name("gb-summary-grade-title")
# gets all the grade scores of students

markslist = []
nameslist = []
outoflist = []

for name in names:
    nameslist.append(name.text)

for marks in gradeScores:
    eachMark = marks.find_element_by_class_name('gb-summary-grade-score-raw')
    outOf = marks.find_element_by_class_name('gb-summary-grade-score-outof')
    markslist.append(eachMark.text)
    outoflist.append(outOf.text[1:])

driver.quit()
