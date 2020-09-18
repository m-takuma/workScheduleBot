from selenium import webdriver
from time import sleep
import chromedriver_binary
import datetime

today = datetime.date.today()
thisMonth = today.month
nextMonth = 0
year = today.year

if thisMonth == 12:
    nextMonth = 1
else: nextMonth = thisMonth + 1

lastDay = 0
if thisMonth == 1 or thisMonth == 3 or thisMonth == 5 or thisMonth == 7 or thisMonth == 8 or thisMonth == 10 or thisMonth == 12:
    lastDay = 31
elif thisMonth == 2:
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        lastDay = 29
    else:
        lastDay = 28
else:
    lastDay = 30


URL = 'https://calendar.yahoo.co.jp/'
MyUserName = ''
MyPasswd = ''
#バイトの日付を下記のリストに入力する
WorkScheduleDays = []


thisMonthWorkDays = []
nextMonthWorkDays = []

driver = webdriver.Chrome()
def login(username,passwd,url):
    driver.get(url)
    name = driver.find_element_by_name('login')
    name.send_keys(username)   
    sleep(1)
    button = driver.find_element_by_name('btnNext')
    button.click()
    sleep(1)
    password = driver.find_element_by_name('passwd')
    password.send_keys(passwd)
    sleep(1)
    buttonsubmit = driver.find_element_by_name('btnSubmit')
    buttonsubmit.click()
    sleep(1)

login(MyUserName,MyPasswd,URL)

for i in WorkScheduleDays:
    if i > lastDay:
        thisMonthWorkDays = []
        nextMonthWorkDays = []
        print(f'エラーが発生しました。日付が間違っています。{i}')
    if i >20:
        thisMonthWorkDays.append(i)
    else:
        nextMonthWorkDays.append(i)

thisMonthXpath = f''
nextMonthXpath = f''

if thisMonth > 9:
    thisMonthXpath = f'{thisMonth}'
else:
    thisMonthXpath = f'0{thisMonth}'

if nextMonth >9:
    nextMonthXpath = f'{nextMonth}'
else:
    nextMonthXpath = f'0{nextMonth}'

for i in thisMonthWorkDays:
    start = driver.find_element_by_xpath(f'//a[@href="/day?date={year}{thisMonthXpath}{i}"]')
    start = start.find_element_by_xpath("../../..")
    start.click()
    sleep(1)
    eventName = driver.find_element_by_name('eventTitle')
    eventName.send_keys('バイト')
    sleep(1)
    eventMinTime = driver.find_element_by_name('miniEdStartTime')
    eventMinTime.clear()
    eventMinTime.send_keys('18:00')
    eventEndTime = driver.find_element_by_name('miniEdEndTime')
    sleep(1)
    eventEndTime.clear()
    eventEndTime.send_keys('23:00')
    sleep(1)
    addButton = driver.find_element_by_xpath('//li/button[@class="BasicButton BasicButton--blue js-BasicButton--submit l-right"]')
    sleep(1)
    addButton.click()
    sleep(2)

toNextMonth = driver.find_element_by_xpath('//div[@class="bc-left bc-button bc-button-next bc-state-default bc-corner-right"]')
toNextMonth.click()
sleep(1)

for i in nextMonthWorkDays:
    if i < 10:
        i = f'0{i}'

    if nextMonth == 1:
        year = year + 1

    start = driver.find_element_by_xpath(f'//a[@href="/day?date={year}{nextMonthXpath}{i}"]')
    start = start.find_element_by_xpath("../../..")
    start.click()
    sleep(1)
    eventName = driver.find_element_by_name('eventTitle')
    eventName.send_keys('バイト')
    sleep(1)
    eventMinTime = driver.find_element_by_name('miniEdStartTime')
    eventMinTime.clear()
    eventMinTime.send_keys('18:00')
    eventEndTime = driver.find_element_by_name('miniEdEndTime')
    sleep(1)
    eventEndTime.clear()
    eventEndTime.send_keys('23:00')
    sleep(1)
    addButton = driver.find_element_by_xpath('//li/button[@class="BasicButton BasicButton--blue js-BasicButton--submit l-right"]')
    sleep(1)
    addButton.click()
    sleep(2)

driver.close()
