from selenium import webdriver
from selenium.webdriver.common.by import By
import time

print("""
İnstagram Botuna Hoş Geldiniz...
1) Takip
2) Beğeni
3) Yorum
""")

secim = input("Seçiminiz : ")
takipkontrol = 0
begenikontrol = 0
yorumkontrol = 0
if secim == "1":
    ad = input("Kullanıcı Adı : ")
    takipkontrol = 1
elif secim == "2":
    link = input("Gönderi Linki : ")
    begenikontrol = 1
elif secim == "3":
    link = input("Gönderi Linki : ")
    yorum = input("Atmak İstediğiniz Yorum : ")
    yorumkontrol = 1

ayarlar = webdriver.FirefoxOptions()
ayarlar.headless = True

#geckodriver.exe'nin adresini yazınız!
path = ''

browser = webdriver.Firefox(options=ayarlar,executable_path=path)

browser.get("https://instagram.com/")
time.sleep(5)
kullanici = browser.find_element(By.XPATH,"//input[contains(@class,'_2hvTZ pexuQ')]")
sifre = browser.find_element(By.XPATH,"(//input[contains(@class,'_2hvTZ pexuQ')])[2]")

#kullanici ve sifre alanlarını doldurunuz!
kullanici.send_keys("kullanici")
sifre.send_keys("sifre")
browser.find_element(By.XPATH,"//div[text()='Giriş Yap']").click()
time.sleep(10)
if takipkontrol == 1:
    print("Takip Ediliyor")
    browser.get("https://www.instagram.com/" + ad )
    time.sleep(10)
    browser.find_element(By.XPATH, "//button[contains(@class,'_acan _acap')]").click()

if begenikontrol == 1:
    print("Beğeni Yapılıyor")
    browser.get(link)
    time.sleep(10)
    browser.find_element(By.XPATH, "(//button[@class='_abl-'])[2]").click()

if yorumkontrol == 1:
    print("Beğeni Yapılıyor")
    browser.get(link)
    time.sleep(5)
    browser.find_element(By.XPATH, "(//button[@class='_abl-'])[3]").click()
    time.sleep(2)
    browser.find_element(By.XPATH, "//textarea[contains(@class,'_ablz _aaoc')]").send_keys(yorum)
    time.sleep(2)
    browser.find_element(By.XPATH, "//div[text()='Paylaş']").click()

time.sleep(5)
browser.get("https://www.instagram.com/"+kullanici+"/")
time.sleep(3)
browser.find_element(By.XPATH,"//header/section[1]/div[1]/div[2]/button[1]").click()
browser.find_element(By.XPATH,"//button[contains(text(),'Çıkış Yap')]").click()
print("İşlem Başarılı")
browser.close()
