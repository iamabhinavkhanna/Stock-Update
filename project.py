import requests
import smtplib
from bs4 import *

URL = "https://www.amazon.com/Zojirushi-NS-LGC05XB-Cooker-uncooked-Stainless/dp/B01EVHWNVG/ref=sr_1_10?crid=2CLZPMZQKI4GE&keywords=rice+cooker&qid=1647106860&sprefix=rice+cooker%2Caps%2C75&sr=8-10"
headers = {
"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",
"Accept-Language": "en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7"
}
data = requests.get(url=URL, headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')
price_element = soup.find(name="span", class_="a-offscreen")
price_text = price_element.text

price_without_currency = price_text.split("$")[1]

price_as_float = float(price_without_currency)
current_price = price_as_float
target_price = 100

if current_price < 200:
    print("Buy it now Sir!")
    subject = "Price is low!!!"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user="khannaabhinav124@gmail.com", password="usuyxhrzxgfrhxcq")
        my_email="khannaabhinav124@gmail.com"
        connection.sendmail(from_addr=my_email,to_addrs="abhinavkhanna09062000@gmail.com",msg=f"Subject:{subject}\n\n" f"Price is {current_price}. Go buy it! {URL}")
    print("Your message is sent! Good Deal!")
elif current_price > 100:
    print("It's still so expensive")
else:
    print("Nothing changes")