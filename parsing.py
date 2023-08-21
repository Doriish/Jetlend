import json
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

options = webdriver.ChromeOptions()
options.add_argument("--ignore-certificate-errors")
driver = webdriver.Chrome(options=options)

i = 0
url = 'https://jetlend.ru/invest/login/'

driver.get(url)
driver.implicitly_wait(10)
time.sleep(2)

login = '89220299019'
password = 'jetlend1234'

driver.find_element(By.ID,"_phone").send_keys(login)
driver.find_element(By.ID,"_password").send_keys(password)
driver.find_element(By.CLASS_NAME, "ant-btn.btn").click()
for item in driver.find_elements(By.CLASS_NAME, "iconButton_button__qMgc0"):
    i+=1
    if i == 2:
        item.click()
    else: 
        pass


driver.implicitly_wait(10)
time.sleep(10)


baba = 0
for item in driver.find_elements(By.CLASS_NAME,"MuiTableRow-root.MuiTableRow-hover.tss-5dt3z0-MUIDataTableBodyRow-root.undefined.tss-5dt3z0-MUIDataTableBodyRow-root.extendedTable_table-row__TwPlu.css-6npsar"):
    baba +=1
    if baba == 10: 
        driver.execute_script("arguments[0].scrollIntoView(true);", item)


driver.implicitly_wait(10)
time.sleep(5)
driver.find_element(By.CLASS_NAME, "MuiSelect-select.MuiTablePagination-select.MuiSelect-standard.MuiInputBase-input.css-1cccqvr").click()
time.sleep(5)
driver.find_element(By.XPATH, '//li[@data-value=100]').click()
time.sleep(5)
cool = driver.find_element(By.CLASS_NAME, "block_header__title__text__g9kpM")
driver.execute_script("arguments[0].scrollIntoView(true);", cool)

hfhfh = []
a = []
#ccompany = driver.find_elements(By.CLASS_NAME,'MuiPaper-root.MuiPaper-elevation.MuiPaper-rounded.MuiPaper-elevation4.tss-11quiee-MUIDataTable-paper.tss-1hm2qcx-MUIDataTable-root.css-ao8rxk')
names = driver.find_elements(By.XPATH,'//td[@data-colindex="0"]')
for company in names:
    name = company.find_element(By.CLASS_NAME,"companyCell_sub-title__5d4Uh").text
    name = name[7:]
    a.append(name)

a= a[::-1]
a= a[10:]
a= a[::-1]

mami = 0
bobo = 0
suuuuuuuuuuuuuuuuka = 0
ruka = []
gggggggggggggggggggggggggg = 0

for sup in driver.find_elements(By.CLASS_NAME,"MuiTableRow-root.MuiTableRow-hover.tss-5dt3z0-MUIDataTableBodyRow-root.undefined.tss-5dt3z0-MUIDataTableBodyRow-root.extendedTable_table-row__TwPlu.css-6npsar"):
    bobo +=1
    while suuuuuuuuuuuuuuuuka<len(a):
        if bobo >= 7: 
            driver.execute_script("arguments[0].scrollIntoView(true);", sup)
            time.sleep(2)
            dopa = '//a[@href="/invest/v3/company/' + str(a[suuuuuuuuuuuuuuuuka]) + '"]'
            print(dopa)
            driver.find_element(By.XPATH,dopa).click()
            name = driver.find_element(By.CLASS_NAME,"companyItem_title__e7co0").text
            print(name)
            ruka.append(name)
            for item in driver.find_elements(By.CLASS_NAME,"iconButton_button__qMgc0"):
                gggggggggggggggggggggggggg+=1
            if gggggggggggggggggggggggggg == 12:
                item.click()
            else: 
                pass
            gggggggggggggggggggggggggg = 0
            suuuuuuuuuuuuuuuuka+=1
        else:
            dopa = '//a[@href="/invest/v3/company/' + str(a[suuuuuuuuuuuuuuuuka]) + '"]'
            print(dopa)
            driver.find_element(By.XPATH,dopa).click()
            name = driver.find_element(By.CLASS_NAME,"companyItem_title__e7co0").text
            mami+=1
            print(name,mami)
            ruka.append(name)
            for item in driver.find_elements(By.CLASS_NAME,"iconButton_button__qMgc0"):
                gggggggggggggggggggggggggg+=1
            if gggggggggggggggggggggggggg == 12:
                item.click()
            else: 
                pass
            time.sleep(2)
            gggggggggggggggggggggggggg = 0
            suuuuuuuuuuuuuuuuka+=1



companysname = driver.find_elements(By.CLASS_NAME,"companyCell_title__EFwP5")
companyssum = driver.find_elements(By.XPATH, '//td[@data-colindex="1"]/div')
companystafka = driver.find_elements(By.XPATH, '//td[@data-colindex="2"]/div')
companysrok = driver.find_elements(By.XPATH, '//td[@data-colindex="4"]')


companyssum= companyssum[::-1]
companyssum= companyssum[10:]
companyssum= companyssum[::-1]
companystafka = companystafka[::-1]
companystafka = companystafka[10:]
companystafka = companystafka[::-1]
companysrok= companysrok[::-1]
companysrok= companysrok[10:]
companysrok= companysrok[::-1]
i = 0
b = []
c = []
e = []	
users2 = {}

j = 0
d = ''

for companyl in companyssum:
    sum = companyl.find_element(By.CLASS_NAME,"h-ws-nowrap").text
    b.append(sum)
for companyg in companystafka:
    stafka = companyg.find_element(By.CLASS_NAME,"badge_container__E0x1A").text
    c.append(stafka)
for companyh in companysrok:
    srok = companyh.find_element(By.CLASS_NAME,"tss-1qtl85h-MUIDataTableBodyCell-root.extendedTable_table-cell__8mq4F.extendedTable_table-cell--width-auto__vVQhT.extendedTable_table-cell--align-center__4QB8y").text
    e.append(srok)        


while i < len(ruka):
    hfhfh.append({
        'Name': ruka[i],
        'Summa': b[i],
        'Stafka': c[i],
        'Srok': e[i]
        })
    i = i + 1
print(hfhfh)

with open("data.json", "w", encoding='utf-8') as json_file:
    json.dump(hfhfh, json_file, ensure_ascii=False, indent=4)


