import requests
import datetime
import locale
from bs4 import BeautifulSoup
from car_offer_obj import CarOffer
from car_constants import CarConstants

url = 'https://www.auto.bg/obiavi/avtomobili-dzhipove/page/2'
HAS_CARS = True
SOURCE = "AUTO.BG"


def formatCarFuel(car_fuel):
    if "бензин" in car_fuel.lower():
        return CarConstants.ENGINE_GAS
    elif "дизел" in car_fuel.lower():
        return CarConstants.ENGINE_DIESEL
    elif "електрически" in car_fuel.lower():
        return CarConstants.ENGINE_DIESEL
    elif "хибриден" in car_fuel.lower():
        return CarConstants.ENGINE_DIESEL
    elif "plug-in хибрид" in car_fuel.lower():
        return CarConstants.ENGINE_DIESEL
    else:
        return car_fuel

def formatCarTransmition(car_transmition):
    if "автоматична" in car_transmition.lower():
        return CarConstants.TRANSMISSION_AUTOMATIC
    elif "полуавтоматична" in car_transmition.lower():
        return CarConstants.TRANSMISSION_SEMIAUTOMATIC
    elif "ръчна" in car_transmition.lower():
        return CarConstants.TRANSMISSION_MANUAL
    else:
        return car_transmition

def formatCarCategory(car_category):
    if car_category.lower() == "ван":
        return CarConstants.BODY_MINIVAN
    elif car_category.lower() == "джип":
        return CarConstants.BODY_SUV
    elif car_category.lower() == "кабрио":
        return CarConstants.BODY_CABRIO
    elif car_category.lower() == "комби":
        return CarConstants.BODY_WAGON
    elif car_category.lower() == "купе":
        return CarConstants.BODY_COUPE
    elif car_category.lower() == "миниван":
        return CarConstants.BODY_MINIVAN
    elif car_category.lower() == "пикап":
        return CarConstants.BODY_PICKUP_TRUCK
    elif car_category.lower() == "седан":
        return CarConstants.BODY_SEDAN
    elif car_category.lower() == "стреч лимозина":
        return CarConstants.BODY_SEDAN
    elif car_category.lower() == "хечбек":
        return CarConstants.BODY_HATCHBACK
    else:
        return car_category

def formatCarYear(car_year):
    locale.setlocale(locale.LC_ALL, 'bg_BG')
    date_object = datetime.datetime.strptime(car_year, "%B %Y г.")
    date_only = date_object.date()
    return date_only

def extract_car_info(html):
    soup = BeautifulSoup(html, 'lxml')
    car_divs = soup.find_all('div', class_='resultItem')

    car_offers = []  # List to store CarOffer objects

    for car_div in car_divs:
        car_url = car_div.find('a', class_='num')['href']
        car_id = car_url.split('/')[-2]
        print(f"CAR_URL: {car_url}")
        print(f"ID: {car_id}")

        car_response = requests.get(car_url)
        car_soup = BeautifulSoup(car_response.content, 'lxml')

        # Extract other car attributes here
        car_name = car_soup.find('td', class_='secColumn').text.strip()
        print(car_name)

        car_price = car_soup.find('th', string='Цена').find_next_sibling('td').text.strip()
        print(car_price)

        car_category = car_soup.find('th', string='Тип').find_next_sibling('td').text.strip()
        car_category = formatCarCategory(car_category)
        print(car_category)

        car_year = car_soup.find('th', string='Произведено').find_next_sibling('td').text.strip()
        car_year = formatCarYear(car_year)
        print(car_year)

        car_ps = car_soup.find('th', string='Мощност[к.с.]').find_next_sibling('td').text.strip()
        print(car_ps)

        car_fuel = car_soup.find('th', string='Тип двигател').find_next_sibling('td').text.strip()
        car_fuel = formatCarFuel(car_fuel)
        print(car_fuel)

        car_transmission = car_soup.find('th', string='Скоростна кутия').find_next_sibling('td').text.strip()
        car_transmission = formatCarTransmition(car_transmission)
        print(car_transmission)

        car_kilometers = car_soup.find('th', string='Пробег').find_next_sibling('td').text.strip()
        print(car_kilometers)

        car_offer = CarOffer(
            ID=car_id,
            VIN=None, 
            name=car_name,
            prices=[car_price],  
            year=car_year,
            URL=car_url,
            kilometers=car_kilometers,
            category=car_category,
            location=None,  
            datePublished=None,  
            isForSale=True,  
            fuel=car_fuel,
            transmision=car_transmission,
            visited=None, 
            ps=car_ps,
            source=SOURCE
        )

        car_offers.append(car_offer)
        break

    return car_offers

while HAS_CARS:
    response = requests.get(url)

    if response.status_code == 200:
        extract_car_info(response.content)
    else:
        print(f"Failed to fetch the page. Status code: {response.status_code}")
        HAS_CARS = False
    
    HAS_CARS = False


