import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText

# Web sayfası URL'si ve ürün seçici
URL = "https://www.example.com/product-page"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}

# Fiyatı çekmek için BeautifulSoup
def get_product_price():
    response = requests.get(URL, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Fiyatı çekmek için uygun HTML elemanını seç
    price = soup.find("span", {"class": "price-class"})  # Bu kısmı ürün sayfasındaki doğru sınıf ile değiştir
    if price:
        return float(price.get_text().replace("₺", "").strip().replace(",", "."))
    return None

# Kullanıcıya e-posta göndermek için
def send_email(price):
    sender_email = "your_email@example.com"
    receiver_email = "receiver_email@example.com"
    password = "your_password"

    subject = "Fiyat Düşüşü Bildirimi"
    body = f"Fiyat şimdi {price}₺. Fiyat düştü! Hemen alabilirsin."

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())

# Fiyatı kontrol et ve bildir
def check_price():
    current_price = get_product_price()
    if current_price and current_price < 1000:  # Burada 1000₺ fiyatı belirleyebilirsin
        send_email(current_price)

# Her gün kontrol etmek için
import time
while True:
    check_price()
    time.sleep(86400)  # 86400 saniye = 1 gün
