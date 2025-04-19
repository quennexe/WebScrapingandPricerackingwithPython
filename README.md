# WebScrapingandPricerackingwithPython
# Python ile Web Scraping ve Fiyat Takibi

Bu proje, belirli bir e-ticaret sitesinden fiyatları çekip bu fiyatları takip etmek için Python kullanır. Uygulama, ürün fiyatlarının belirli bir seviyeye düştüğünde kullanıcıya e-posta bildirimleri gönderir.

## Özellikler
- Web sayfasından ürün fiyatlarını çeker.
- Belirtilen bir fiyat seviyesine düştüğünde, kullanıcıya e-posta bildirimi gönderir.
- Fiyat kontrolü, her gün otomatik olarak yapılır.
- Kullanıcı, fiyatın belirli bir seviyenin altına düşüp düşmediğini takip edebilir.

## Kullanılan Teknolojiler
- **Python**: Programlama dili.
- **BeautifulSoup**: Web sayfalarını analiz etmek için kullanılır.
- **Requests**: HTTP istekleri göndermek için kullanılır.
- **Smtplib**: E-posta göndermek için kullanılır.
- **Time**: Belirli aralıklarla işlem yapmak için kullanılır.

## Nasıl Çalışır?
1. **OpenWeatherMap API Anahtarınızı Alın**: Bir e-ticaret sitesinden belirli ürünlerin fiyatlarını takip etmek için Python ile web scraping yapıyoruz.
2. **HTML Yapısını İnceleyin**: Ürünün fiyat bilgilerini çekebilmek için web sayfasındaki doğru HTML elementlerini seçin.
3. **API Anahtarını Değiştirin**: `script.py` dosyasındaki `YOUR_API_KEY` kısmını kendi API anahtarınızla değiştirin.
4. **E-posta Hesabınızı Bağlayın**: Kullanıcıya bildirim gönderebilmek için e-posta bilgilerinizi (e-posta adresi ve şifre) `send_email` fonksiyonuna ekleyin.
5. **Uygulamayı Çalıştırın**: Python dosyasını çalıştırarak, belirli aralıklarla fiyat takibini yapın.

## Kullanım Adımları
1. **Python Paketlerini Yükleyin**:

    pip install requests beautifulsoup4
   

2. **API Anahtarınızı ve E-posta Bilgilerinizi Girin**:
    - `script.py` dosyasındaki API anahtarınızı ve e-posta bilgilerinizi güncelleyin.

3. **Uygulamayı Çalıştırın**:
    - Python dosyasını çalıştırarak, ürün fiyatını kontrol etmek ve bildirim almak için:
 
    python script.py
  

