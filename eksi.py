import time
import csv
import html
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

# Başlığı kullanıcıdan al
baslik = input("hangi başlığı aramak istiyorsunuz?\n")

url = "https://eksisozluk.com/"

# Selenium ile tarayıcıyı başlat
browser = webdriver.Chrome()

time.sleep(3)

# Ana sayfayı aç
browser.get(url)

time.sleep(3)

# Arama alanını bul ve başlığı yaz
input_area = browser.find_element(By.XPATH, "//*[@id='search-textbox']")
button = browser.find_element(By.XPATH, "//*[@id='search-form']/button")

time.sleep(3)

input_area.send_keys(baslik)

time.sleep(2)

# Arama butonuna tıkla
button.click()

time.sleep(3)

# Geçerli URL'yi al
url = browser.current_url
source = browser.page_source

soup = BeautifulSoup(source, "html.parser")

# Sayfa sayısını bul
try:
    page_count = len(soup.find("div", {"class": "clearfix sub-title-container"}).find(
        "div", {"class": "pager"}).find_all("option"))
except:
    page_count = 1

print(f"Toplam sayfa sayısı: {page_count}")

# CSV dosyasını oluştur ve başlıkları yaz
with open('eksi_sozluk.csv', mode='w', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file)
    writer.writerow(["İçerik"])  # Sadece içerik başlığı

    # Her sayfa için içerikleri al
    for i in range(1, page_count + 1):
        # Sayfayı aç
        browser.get(url + "?p=" + str(i))
        time.sleep(3)  # Sayfanın yüklenmesini bekle
        source = browser.page_source
        soup = BeautifulSoup(source, "html.parser")
        
        entry_divs = soup.find_all("div", {"class": "content"})
        for entry in entry_divs:
            content = entry.text.strip()
            content = html.unescape(content)  # HTML karakterlerini düzelt
            print(content)  # İçeriği yazdır
            print("*" * 100)
            writer.writerow([content])  # CSV dosyasına yaz

# Tarayıcıyı kapat
browser.close()
