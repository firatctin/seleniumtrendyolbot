#Gerekli modül ve dosyaları dahil ettiğim kısım:

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#Giriş bilgilerini almak için
with open('girisbilgileri.txt', 'r', encoding='UTF-8') as file:
    bilgiler = file.readlines()
    email = bilgiler[0].strip()
    sifre = bilgiler[1].strip()
#İstenilen sorguları bulmak için:
with open('cumle.txt', 'r', encoding='UTF-8') as file:
    liste = file.readlines()
    for i in liste:
        liste[liste.index(i)] = i.strip()

print(liste)

    

#Tarayıcının açılması için 
driver = webdriver.Firefox() 
driver.get('https://www.trendyol.com/')
time.sleep(3)
#Başta gelen cinsiyet ekranını kapatmak için
gender_pick = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[3]/div[4]/div/div/div/div/div[1]')
gender_pick.click()

#Giriş yap kısmına girmek için
login = driver.find_element(by= By.XPATH, value= '/html/body/div[1]/div[1]/div/div[2]/div/div/div[3]/div/div/div/div[1]/div[1]/p')
login.click()

#Emaili gireceğimiz yeri seçmek ve doldurmak için

emailinput = driver.find_element(by= By.XPATH, value= '//*[@id="login-email"]')
emailinput.send_keys(email)
passwordinput = driver.find_element(by= By.XPATH, value= '//*[@id="login-password-input"]')
passwordinput.send_keys(sifre)
giris_yap = driver.find_element(by= By.XPATH, value= '/html/body/div[1]/div[3]/div[3]/div[1]/form/button')
giris_yap.click()
time.sleep(5)

#Sorguları aramak için döngü yapısı:
for i in liste:
    search = driver.find_element(by= By.XPATH, value= '/html/body/div[1]/div[1]/div/div[2]/div/div/div[2]/div/div/div/input')
    search.clear()
    search.send_keys(i)
    search.send_keys(Keys.ENTER)
    time.sleep(2)
    stars = driver.find_element(by= By.XPATH, value= '/html/body/div[1]/div[3]/div[2]/div[2]/div/div/div/div[1]/div[1]/div/div/div[5]/div[1]/div[1]')
    stars.click()
    time.sleep(2)
    threestarred = driver.find_element(by= By.XPATH, value= '/html/body/div[1]/div[3]/div[2]/div[2]/div/div/div/div[1]/div[1]/div/div/div[5]/div[2]/a[1]/div[1]')
    threestarred.click()
    time.sleep(2)
    twostarred = driver.find_element(by= By.XPATH, value= '/html/body/div[1]/div[3]/div[2]/div[2]/div/div/div/div[1]/div[1]/div/div/div[5]/div[2]/a[2]/div[1]')
    twostarred.click()
    time.sleep(10)