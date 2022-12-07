from bs4 import BeautifulSoup
import requests
import lxml
import smtplib

EMAIL = "mTEMAIL@gmail.com"
SMTP_ADDRESS = "smtp.gmail.com"
PASSWORD = "*****"

URL = "https://www.amazon.com/UGEE-11-9-Inch-Drawing-Tablets-sRGB-Anti-Glare-8192-Levels-Battery-Free-Drawing-Monitor/dp/B09MLRKLQX/ref=sr_1_1_sspa?crid=3BATZFVGP632M&keywords=graphic+tablets+for+drawing&qid=1659345000&sprefix=graphic+tab%2Caps%2C466&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyVEhVRzNHME5JR0hBJmVuY3J5cHRlZElkPUEwODc1Mzk3OExUQzdFMUs2WjNVJmVuY3J5cHRlZEFkSWQ9QTA1MzcwNjMxMlhKSk1HSVdBRlBGJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=="

headers = {
    "Accept-Language" : "en-US,en;q=0.9",
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.71",
}

response = requests.get(url=URL, headers=headers)

soup = BeautifulSoup(response.content, "lxml")
# price_locator = soup.find(class_="a-offscreen")
# price = price_locator.getText()
# print(price)
#
# # print(soup.prettify())

price = soup.find(class_="a-offscreen").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)


title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 170

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP(SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}"
        )