import csv
import time
import html
import re

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

def extract_year(date_string):
    match = re.search(r'\d{2}\.\d{2}\.(\d{4})', date_string)
    if match:
        return match.group(1)
    return None


# Başlığı kullanıcıdan al
baslik = input("hangi başlığı aramak istiyorsunuz?\n")
fileName = baslik.replace(" ","_")
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
with open(f'{fileName}.csv', mode='w', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file, quoting=csv.QUOTE_ALL)
    writer.writerow(["İçerik","Tarih","Yıl"])  # İçerik ve tarih başlıkları

    # Her sayfa için içerikleri al
    for i in range(1, page_count + 1):
        # Sayfayı aç
        browser.get(url + "?p=" + str(i))
        time.sleep(3)  # Sayfanın yüklenmesini bekle
        source = browser.page_source
        soup = BeautifulSoup(source, "html.parser")
        
        entry_divs = soup.find_all("div", {"class": "content"})
        dates = soup.find_all("a", {"class": "entry-date permalink"})
        
        for entry, date in zip(entry_divs, dates):
            content = entry.text.strip()
            content = html.unescape(content)  # HTML karakterlerini düzelt
            date_text = date.text.strip()
            date_text = html.unescape(date_text)  # HTML karakterlerini düzelt
            year = extract_year(date_text)
            print(f"İçerik: {content}")
            print(f"Tarih: {date_text}")
            print("*" * 100)
            writer.writerow([content, date_text,year])  # CSV dosyasına içerik ve tarih yaz

# Tarayıcıyı kapat
browser.close()
