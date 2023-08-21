import json
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
#добавляем драйвер селениума
options = webdriver.ChromeOptions()
options.add_argument("--ignore-certificate-errors")
driver = webdriver.Chrome(options=options)

i = 0
url = 'https://jetlend.ru/invest/login/'
#выбираем сайт на который нужно зайти
driver.get(url)
driver.implicitly_wait(10)
time.sleep(2)

login = '89220299019'
password = 'jetlend1234'
#происходит авторизация
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

#перемотка вниз чтобы переключить с показа 10 компаний на 100 компаний
srollinglist = 0
for item in driver.find_elements(By.CLASS_NAME,"MuiTableRow-root.MuiTableRow-hover.tss-5dt3z0-MUIDataTableBodyRow-root.undefined.tss-5dt3z0-MUIDataTableBodyRow-root.extendedTable_table-row__TwPlu.css-6npsar"):
    srollinglist +=1
    if srollinglist == 10: 
        driver.execute_script("arguments[0].scrollIntoView(true);", item)

#переключение с 0 на 100
driver.implicitly_wait(10)
time.sleep(5)
driver.find_element(By.CLASS_NAME, "MuiSelect-select.MuiTablePagination-select.MuiSelect-standard.MuiInputBase-input.css-1cccqvr").click()
time.sleep(5)
driver.find_element(By.XPATH, '//li[@data-value=100]').click()
time.sleep(5)
# перемотка на верх что бы запарсить саму карточку
codofcompany = driver.find_element(By.CLASS_NAME, "block_header__title__text__g9kpM")
driver.execute_script("arguments[0].scrollIntoView(true);", codofcompany)

blockofcompany = []
code = []

names = driver.find_elements(By.XPATH,'//td[@data-colindex="0"]')
for company in names:
    name = company.find_element(By.CLASS_NAME,"companyCell_sub-title__5d4Uh").text
    name = name[7:]
    code.append(name)

code= code[::-1]
code= code[10:]
code= code[::-1]

bobo = 0 #нужно для выполнения условия. при котором начнётся скроллинг карточек компании. Если его не сделать, то программа не сможет нажать на эти карточки 
suka = 0 #обычный счетчик для while который нужен для перебирания массива
nameofcopmany = []
buttonclick = 0 # переменная созданнная для перебирания кнопок 
# следующий код - парсинг Оригинальных!!! названий
for sup in driver.find_elements(By.CLASS_NAME,"MuiTableRow-root.MuiTableRow-hover.tss-5dt3z0-MUIDataTableBodyRow-root.undefined.tss-5dt3z0-MUIDataTableBodyRow-root.extendedTable_table-row__TwPlu.css-6npsar"):
    bobo +=1
    while suka<len(code):
        if bobo >= 7: 
            #скроллинг сайта для захода на странички компаний
            driver.execute_script("arguments[0].scrollIntoView(true);", sup)
            time.sleep(2)
            dopa = '//a[@href="/invest/v3/company/' + str(code[suka]) + '"]' #здесь создаётся ссылка на карточку компании
            driver.find_element(By.XPATH,dopa).click() #нажимаем на ссылку и мы переносимся на профиль компании
            name = driver.find_element(By.CLASS_NAME,"companyItem_title__e7co0").text #парсим название компании
            nameofcopmany.append(name)#сохраняем название в массив
            for item in driver.find_elements(By.CLASS_NAME,"iconButton_button__qMgc0"): #теперь нам нужно выйти из профиля компании. Просто нажать на кнопку не получится, так как у всех 12 кнопок на сайте одинаковые классы, поэтому мы перебираем эти кнопки в цикле, чтобы нажать на нужную кнопку для выхода из профиля, которая является 12 по счёту
                buttonclick+=1
            if buttonclick == 12:
                item.click()
            else: 
                pass
            buttonclick = 0
            suka+=1
        else:
            #парсинг
            dopa = '//a[@href="/invest/v3/company/' + str(code[suka]) + '"]'
            driver.find_element(By.XPATH,dopa).click()
            name = driver.find_element(By.CLASS_NAME,"companyItem_title__e7co0").text
            nameofcopmany.append(name)
            for item in driver.find_elements(By.CLASS_NAME,"iconButton_button__qMgc0"):
                buttonclick+=1
            if buttonclick == 12:
                item.click()
            else: 
                pass
            time.sleep(2)
            buttonclick = 0
            suka+=1


#парсинг всего остального
companyssum = driver.find_elements(By.XPATH, '//td[@data-colindex="1"]/div')
companystafka = driver.find_elements(By.XPATH, '//td[@data-colindex="2"]/div')
companysrok = driver.find_elements(By.XPATH, '//td[@data-colindex="4"]')

#обрезание вторичного рынка(10)
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
#все что ниже это парсинг оставшихся данных и в дальнейшем занесения их в массив
summaa = []
stafkaa = []
srook = []	



for companyl in companyssum:
    sum = companyl.find_element(By.CLASS_NAME,"h-ws-nowrap").text
    summaa.append(sum)
for companyg in companystafka:
    stafka = companyg.find_element(By.CLASS_NAME,"badge_container__E0x1A").text
    stafkaa.append(stafka)
for companyh in companysrok:
    srok = companyh.find_element(By.CLASS_NAME,"tss-1qtl85h-MUIDataTableBodyCell-root.extendedTable_table-cell__8mq4F.extendedTable_table-cell--width-auto__vVQhT.extendedTable_table-cell--align-center__4QB8y").text
    srook.append(srok)        


while i < len(nameofcopmany):
    blockofcompany.append({
        'Name': nameofcopmany[i],
        'Summa': summaa[i],
        'Stafka': stafkaa[i],
        'Srok': srook[i]
        })
    i = i + 1
print(blockofcompany)
#занесение в json
with open("data.json", "w", encoding='utf-8') as json_file:
    json.dump(blockofcompany, json_file, ensure_ascii=False, indent=4)


