import requests
from bs4 import BeautifulSoup
import pprint
from notification_manager import SendingEmail
from datetime import datetime


URL="https://www.amazon.com/2022-Apple-MacBook-Laptop-chip/dp/B0B3C57XLR/ref=sr_1_1?keywords=macbook+pro+13+inch&qid=1661686779&sprefix=%2Caps%2C271&sr=8-1"

header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8,ru;q=0.7,tr;q=0.6,az;q=0.5",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
    "Referer":"https://www.amazon.com/"
}

response = requests.get(url=URL, headers=header)
web_page = response.content


soup = BeautifulSoup(web_page, 'html.parser')
# print(soup.prettify())

# getting price
price = soup.select_one('.a-price .a-offscreen').get_text()
price_without_currency = price.split('$')[1].replace(",","")
price_as_float = float(price_without_currency)

# getting title
title = soup.find(id="productTitle").get_text()
corrected_title = title.replace('  ','')

# getting email sender
sending_email = SendingEmail()

# getting datetime
now=datetime.now()
hour = now.hour
minute = now.minute


if hour == 18 and minute == 31:
    if price_as_float < 1240:  
        sending_email.sending_email(title=corrected_title, price=price_as_float, url=URL)
        print("Email was sent successfully")
    else:
        print("The price is not lower than expected")
