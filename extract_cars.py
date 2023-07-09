import requests
import time
from bs4 import BeautifulSoup

AUTO_BG_URL = 'https://www.auto.bg/obiavi/avtomobili-dzhipove/page/'
MOBILE_URL = 'https://www.mobile.bg/pcgi/mobile.cgi?act=3&amp;slink=szoboa&amp;f1='
START_NUMBER = 1
HAS_CARS = True

while HAS_CARS:
    url = MOBILE_URL + str(START_NUMBER)
    response = requests.get(url)
    
    if response.status_code == 200:
        # Process the response here
        print(f"Request {START_NUMBER}: Success")
    else:
        HAS_CARS = False
        print(f"Request {START_NUMBER}: Failed")
    
    START_NUMBER += 1

    soup = BeautifulSoup(response.content, 'lxml')
    print(soup.prettify())

    # decoded_text = response.content.decode('cp1251')  # Replace 'utf-8' with the correct character encoding

    # print(decoded_text)
    # with open("output.html", "w", encoding="iso-8859-1") as file:
    #     file.write(response.content.decode("iso-8859-1"))
    #     print("HTML content saved to output.html")
    break
    time.sleep
