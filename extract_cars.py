import requests
import time
from bs4 import BeautifulSoup
import datetime
import re
from car_offer_obj import CarOffer

AUTO_BG_URL = 'https://www.auto.bg/obiavi/avtomobili-dzhipove/page/'
MOBILE_URL = 'https://www.mobile.bg/pcgi/mobile.cgi?act=3&amp;slink=szoboa&amp;f1='
START_NUMBER = 1
HAS_CARS = True

car_offers = []  # List to store CarOffer objects

while HAS_CARS:
    url = MOBILE_URL + str(START_NUMBER)
    page_response = requests.get(url)
    
    if page_response.status_code == 200:
        # Process the response here
        print(f"Request {START_NUMBER}: Success")

        soup = BeautifulSoup(page_response.content, 'lxml')
        cars = soup.find_all('table', class_ = 'tablereset', style='width:660px; margin-bottom:0px; border-top:#008FC6 1px solid; background:url(//www.mobile.bg/images/picturess/top_bg.gif); background-position:bottom; background-repeat:repeat-x;')
        for index, car in enumerate(cars):
            car_title = car.find('a', class_ = 'mmm')
            # car_name = car_title.text
            car_URL = car_title['href']
            car_price = car.find('span', class_ = 'price').text

            car_response = requests.get("https:" + car_URL)
            car_soup = BeautifulSoup(car_response.content, 'lxml')
            car_name = car_soup.find('strong').text
            car_data = car_soup.find('ul', class_ = 'dilarData')

            # Extracting kilometers using regular expressions
            kilometers = None
            location = None
            datePublished = None
            fuel = None
            transmision = None
            visited = car_soup.find('span', class_ = 'advact').text
            category = None
            year = None

            # Extracting ID using regular expressions
            car_ID = None
            match_ID = re.search(r'adv=(\d+)', car_URL)
            if match_ID:
                car_ID = match_ID.group(1)
            match_location = re.search(r'Регион:\s+(.*)$', str(car.find('td', colspan='3').text))
            if match_location:
                location = match_location.group(1)
            match = re.search(r'<li>Пробег \[км\]</li><li>([\d\s]+) км</li>', str(car_data))
            if match:
                kilometers = int(match.group(1).replace(" ", ""))
            match = re.search(r'<li>Тип двигател</li><li>(.*?)</li>', str(car_data))
            if match:
                fuel = match.group(1).replace(" ", "")
            match = re.search(r'<li>Скоростна кутия</li><li>(.*?)</li>', str(car_data))
            if match:
                transmision = match.group(1).replace(" ", "")
            match = re.search(r'<li>Категория</li><li>(.*?)</li>', str(car_data))
            if match:
                category = match.group(1).replace(" ", "")
            match = re.search(r'<li>Дата на производство</li><li>(.*?)</li>', str(car_data))
            if match:
                year = match.group(1)

            # Create CarOffer object
            car_offer = CarOffer(
                ID=car_ID,
                WIN=None,
                name=car_name,
                prices=[car_price],
                year=year,
                URL=car_URL,
                kilometers=kilometers,
                category=category,
                location=location,
                datePublished=None,
                isForSale=True,
                fuel=fuel,
                transmision=transmision,
                visited=visited
            )

            print(car_offer)
            
            car_offers.append(car_offer)  # Add the CarOffer object to the list
            break

    else:
        HAS_CARS = False
        print(f"Request {START_NUMBER}: Failed")
    
    START_NUMBER += 1
    
    break
