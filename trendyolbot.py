#Gerekli modül ve dosyaları dahil ettiğim kısım:

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

#Giriş bilgilerini almak için
with open('girisbilgileri.txt', 'r', encoding= 'UTF-8') as file:
    bilgiler = file.readlines()
    email = bilgiler[0].strip()
    sifre = bilgiler[1].strip()
#İstenilen sorguları bulmak için:
with open('cumle.txt', 'r', encoding='UTF-8') as file:
    liste = file.readlines()
    for i in liste:
        liste[liste.index(i)] = i.strip()
while ('' in liste):
    liste.remove('')
print(liste)

    

#Tarayıcının açılması için 
driver = webdriver.Firefox() 
driver.get('https://www.trendyol.com/')
WebDriverWait(driver,40).until(expected_conditions.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[3]/div[4]/div/div/div/div/div[1]')))

#Başta gelen cinsiyet ekranını kapatmak için
gender_pick = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[3]/div[4]/div/div/div/div/div[1]')
gender_pick.click()

#Giriş yap kısmına girmek için
login = driver.find_element(by= By.XPATH, value= '/html/body/div[1]/div[1]/div/div[2]/div/div/div[3]/div/div/div/div[1]/div[1]/p')
login.click()

#Emaili gireceğimiz yeri seçmek ve doldurmak için
WebDriverWait(driver,40).until(expected_conditions.element_to_be_clickable((By.XPATH,'//*[@id="login-email"]')))

emailinput = driver.find_element(by= By.XPATH, value= '//*[@id="login-email"]')
emailinput.send_keys(email)
passwordinput = driver.find_element(by= By.XPATH, value= '//*[@id="login-password-input"]')
passwordinput.send_keys(sifre)
giris_yap = driver.find_element(by= By.XPATH, value= '/html/body/div[1]/div[3]/div[3]/div[1]/form/button')
giris_yap.click()

#Koleksiyon eklemek için:
WebDriverWait(driver,40).until(expected_conditions.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[1]/div/div[2]/div/div/div[3]/div/div/div/a/div')))
time.sleep(1)
favs = driver.find_element(by= By.XPATH, value= '/html/body/div[1]/div[1]/div/div[2]/div/div/div[3]/div/div/div/a/div')
favs.click()
time.sleep(1)
WebDriverWait(driver,40).until(expected_conditions.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[3]/div/div/div[1]/div/div[1]/a[2]')))

collections = driver.find_element(by= By.XPATH, value= '/html/body/div[1]/div[3]/div/div/div[1]/div/div[1]/a[2]')
collections.click()
time.sleep(1)
WebDriverWait(driver,40).until(expected_conditions.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[3]/div/div/div/div[2]/div/div/button')))
newcollection = driver.find_element(by= By.XPATH, value= '/html/body/div[1]/div[3]/div/div/div/div[2]/div/div/button')
newcollection.click()


writer =  open('collections.txt', 'a', encoding= 'UTF-8')
reader =  open('collections.txt', 'r', encoding= 'UTF-8')

names = reader.readlines()

reader.close()
time.sleep(1)
if len(names) == 0:
    WebDriverWait(driver,40).until(expected_conditions.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[3]/div/div/div[1]/div/div/div/div[2]/form/div[1]/div/input')))
    writer.writelines('1\n')
    collection_name = driver.find_element(by= By.XPATH, value= '/html/body/div[1]/div[3]/div/div/div[1]/div/div/div/div[2]/form/div[1]/div/input')
    collection_name.send_keys('Koleksiyon 1')
else:
    WebDriverWait(driver,40).until(expected_conditions.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[3]/div/div/div[1]/div/div/div/div[2]/form/div[1]/div/input')))
    collection_name = driver.find_element(by= By.XPATH, value= '/html/body/div[1]/div[3]/div/div/div[1]/div/div/div/div[2]/form/div[1]/div/input')
    collection_counter = int(names[-1]) + 1
    collection_name_temp = 'Koleksiyon' + ' ' + str(collection_counter)
    writer.writelines(str(collection_counter) + '\n')
    collection_name.send_keys(collection_name_temp)
writer.close()
new_collection_button = driver.find_element(by= By.XPATH, value= '/html/body/div[1]/div[3]/div/div/div[1]/div/div/div/div[2]/form/button')
new_collection_button.click()
time.sleep(0.7)
WebDriverWait(driver,40).until(expected_conditions.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[3]/div/div/div[1]/div/div/a')))

close = driver.find_element(by= By.XPATH, value= '/html/body/div[1]/div[3]/div/div/div[1]/div/div/a')
close.click()


#Sorguları aramak için döngü yapısı:
for i in liste:
    driver.get("https://www.trendyol.com/")
    WebDriverWait(driver,40).until(expected_conditions.element_to_be_clickable((By.XPATH,'//input[@class="vQI670rJ"]')))
    try:
        search = driver.find_element(by= By.XPATH, value= '//input[@class="vQI670rJ"]')
        search.clear()
        search.send_keys(i)
    except:
        continue
    search.send_keys(Keys.ENTER)
    time.sleep(1)
    

    
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
   
    time.sleep(1)
    try:
        driver.execute_script("return document.getElementsByClassName('popup')[0].remove();")
        driver.execute_script("return document.getElementsByClassName('overlay')[0].remove();")
        
    except:
        pass
    
    
    
    time.sleep(1)
   
    
    try:
        driver.execute_script("return document.getElementsByClassName('popup')[0].remove();")
        driver.execute_script("return document.getElementsByClassName('overlay')[0].remove();")
        
    except:
        pass
    driver.execute_script("window.scrollTo(0,0);")
    WebDriverWait(driver,40).until(expected_conditions.element_to_be_clickable((By.XPATH,'//div[@class="fltr-cntnr-ttl-area"]')))
    stars = driver.find_elements(by= By.XPATH, value= '//div[@class="fltr-cntnr-ttl-area"]')
    for i in stars:
        i.click()
    
    time.sleep(2)
    
    
    try:
        
        threestarred = driver.find_element(by= By.XPATH, value= "//*[contains(text(), 'Üç Yıldızlı Ürün')]")
        threestarred.click()
    except:
        pass
    
    try:
        
        driver.execute_script("return document.getElementsByClassName('popup')[0].remove();")
        driver.execute_script("return document.getElementsByClassName('overlay')[0].remove();")
        
    except:
        pass
    
    time.sleep(2)
    try:
        
        twostarred = driver.find_element(by= By.XPATH, value= "//*[contains(text(), 'İki Yıldızlı Ürün')]")
        twostarred.click()
    except:
        pass
    
    try:
        driver.execute_script("return document.getElementsByClassName('popup')[0].remove();")
        driver.execute_script("return document.getElementsByClassName('overlay')[0].remove();")
        
    except:
        pass
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    try:
        driver.execute_script("return document.getElementsByClassName('popup')[0].remove();")
        driver.execute_script("return document.getElementsByClassName('overlay')[0].remove();")
        
        
        
    except:
        pass
    count = driver.find_element(by= By.XPATH, value= '//div[@class="dscrptn"]')
    count_elements = count.text.split(" ")
    try:
        
        
        count_elements[3] = count_elements[3].replace(".", "")
    except:
        pass
    driver.execute_script('return document.getElementById("footer-container").remove();')
        
    driver.execute_script('return document.getElementById("marketing-internal-linking").remove();')
    
    SCROLL_PAUSE_TIME = 0.5

    #Aşağıya kaydırıp tüm ürünlerin yüklenmesi için gerekli olan algoritma:
    last_height = driver.execute_script("return document.body.scrollHeight")
    counter = 1
    
    if int(count_elements[3].rstrip("+")) >= 400:
        while counter < 16:
    
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    
            time.sleep(SCROLL_PAUSE_TIME)

    
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
            counter += 1
    else:
        while True:
    
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    
            time.sleep(SCROLL_PAUSE_TIME)

    
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
    time.sleep(1)
    products = driver.find_elements(by = By.XPATH , value='//div[@class="p-card-chldrn-cntnr card-border" and .//div[@class="low-price-in-last-month"]]')
    products.extend(driver.find_elements(by = By.XPATH , value='//div[@class="p-card-chldrn-cntnr card-border" and .//div[@class="low-price-in-last-month with-basket"]]'))
    if len(products) >30:
        products = products[:30]
    if len(products) > 0:
        for i in products:
            
            query = i.find_element(By.XPATH, value = './child::a')
            
            link = query.get_attribute('href')
            driver.execute_script("window.open('');")
            driver.switch_to.window(driver.window_handles[-1])
            driver.get(link)
        
            WebDriverWait(driver,40).until(expected_conditions.element_to_be_clickable((By.XPATH,'//div[@class="add-to-collection-button-wrapper"]')))
            try:
                addtocollection = driver.find_element(by = By.XPATH, value= '//div[@class="add-to-collection-button-wrapper"]')
                
                addtocollection.click()
            
            except:
                pass
            
            try:    
                driver.execute_script('followers = document.querySelector(".pdp-add-to-collection-modal");')
            except:
                pass
            try:
                WebDriverWait(driver,40).until(expected_conditions.element_to_be_clickable((By.XPATH,'//div[@class="add-to-collection-button-wrapper"]')))
                add = driver.find_element(by = By.XPATH, value= '/html/body/div[1]/div[5]/main/div[2]/div/div/div[2]/div/div/div[2]')
            
                add.click()
            except:
                pass
            time.sleep(0.2)
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            
    else:
        continue
       
    driver.execute_script("window.scrollTo(0,0);")
    
