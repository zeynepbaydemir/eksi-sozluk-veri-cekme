import time
import csv
import html
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

# Yazarı kullanıcıdan al
baslik = input("hangi yazari aramak istiyorsunuz?(@yazaradi seklinde arayiniz.)\n")

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

# Yazarın entry'lerini almak için yazar sayfasına git
browser.get(url)

# Daha önce kaydedilen entry'leri tutmak için bir set oluştur
unique_entries = set()

# CSV dosyasını oluştur ve başlıkları yaz
with open('eksi_yazar_entry.csv', mode='w', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["İçerik"])  # Sadece içerik başlığı

    while True:
        # Sayfanın yüklenmesini bekle
        time.sleep(3)
        
        # Sayfa kaynağını al ve BeautifulSoup ile parse et
        source = browser.page_source
        soup = BeautifulSoup(source, "html.parser")
        
        # Entry'leri bul
        entry_divs = soup.find_all("div", {"class": "content"})
        for entry in entry_divs:
            content = entry.text.strip()
            content = html.unescape(content)  # HTML karakterlerini düzelt
            
            # İstenmeyen ifadeleri filtrele (örneğin "görsel") ve tekrarlı entry'leri kontrol et
            if "görsel" not in content.lower() and content not in unique_entries:
                unique_entries.add(content)  # Yeni entry'yi sete ekle
                print(content)  # İçeriği yazdır
                print("*" * 100)
                writer.writerow([content])  # CSV dosyasına yaz

        try:
            # "Daha fazla göster" butonunu bul ve tıkla
            more_button = browser.find_element(By.XPATH, "//a[@class='load-more-entries']")
            browser.execute_script("arguments[0].scrollIntoView();", more_button)
            more_button.click()
            time.sleep(3)  # Sayfanın yüklenmesini bekle
        except:
            print("Tüm entry'ler çekildi.")
            break  # Eğer buton yoksa döngüyü kır

# Tarayıcıyı kapat
browser.close()

