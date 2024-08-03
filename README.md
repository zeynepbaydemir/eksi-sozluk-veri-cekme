# Ekşi Sözlük Scraper

Bu proje, Selenium ve BeautifulSoup kullanarak Ekşi Sözlük'ten belirli bir başlığın içeriklerini toplamak için hazırlanmıştır. İçerikler CSV dosyasına kaydedilir.

## Kullanım

1. Proje dizinine gidin ve Python dosyasını çalıştırın:
```
python eksi_sozluk_scraper.py
```

1. Alternatif olarak, VS Code kullanıyorsanız, dosyayı açtıktan sonra sağ tıklayıp "Run Python File in Terminal" seçeneğini seçerek de çalıştırabilirsiniz.
    
3. Çalıştırıldığında, sizden bir başlık girmeniz istenecektir. Aramak istediğiniz başlığı girin ve `Enter` tuşuna basın.
    
4. Kod, arama sonuçlarını alacak, sayfa sayısını belirleyecek ve her sayfadaki içerikleri toplayarak `eksi_sozluk.csv` dosyasına kaydedecektir.

## Headers kısmı için:
- **Tarayıcıyı Açın ve "İncele" (Inspect) Seçeneğini Açın**:
    
    - Sağ tıklayıp "İncele" (Inspect) seçeneğine tıklayın veya `F12` tuşuna basın.
- **"Network" Sekmesine Geçin**:
    
    - Açılan geliştirici araçlarında üstteki sekmelerden "Network" sekmesine tıklayın.
- **Sayfayı Yenileyin**:
    
    - Sayfanın yeniden yüklenmesi için `F5` tuşuna basın. Bu, tüm ağ isteklerini görmenizi sağlar.
- **İlk İsteği Bulun**:
    
    - Yüklenen sayfa isteği tamamlandığında, "Name" sütununda listeyi göreceksiniz. İlk isteği (genellikle en üstteki satır) sağ tıklayın.
- **"Copy as cURL" Seçeneğini Seçin**:
    
    - Sağ tıkladığınızda açılan menüde "Copy" seçeneğine gidin ve ardından "Copy as cURL" seçeneğine tıklayın. Bu, isteği cURL formatında kopyalar.
- **Metin Düzenleyicisine Yapıştırın**:
    
    - Kopyalanan cURL komutunu bir metin düzenleyicisine yapıştırın. Burada `User-Agent` bilgisi de dahil olmak üzere tüm başlıkları göreceksiniz.
- **`User-Agent` Bilgisini Kopyalayın**:
    
    - Kopyaladığınız cURL komutunun içinde `-H 'User-Agent: ...'` kısmını bulun ve bu değeri Python kodunuza ekleyebilirsiniz.
