import datetime

class CarOffer:
    def __init__(self, ID, WIN, name, prices, URL, description, kilometers, specifications, location, datePublished, isForSale, fuel, transmision):
        self._ID = ID
        self._WIN = WIN
        self._name = name
        self._prices = prices
        self._URL = URL
        self._description = description
        self._kilometers = kilometers
        self._specifications = specifications
        self._location = location
        self._datePublished = datePublished
        self._isForSale = isForSale
        self._fuel = fuel
        self._transmision = transmision

    # Getterss
    def get_id(self):
        return self._ID
    def get_WIN(self):
        return self._WIN
    def get_name(self):
        return self._name
    def get_prices(self):
        return self._prices
    def get_URL(self):
        return self._URL
    def get_description(self):
        return self._description
    def get_kilometers(self):
        return self._kilometers
    def get_specifications(self):
        return self._specifications
    def get_location(self):
        return self._location
    def get_datePublished(self):
        return self._datePublished
    def get_isForSale(self):
        return self._isForSale
    def get_fuel(self):
        return self._fuel
    def get_transmision(self):
        return self._transmision
    

    # Setters
    def set_isForSale(self, value):
        self._isForSale = value
    def set_prices(self, value):
        self._prices.append(value)
    def set_kilometers(self, value):
        self._kilometers = value

    # Properties for attributes
    id = property(get_id)
    WIN = property(get_WIN)
    name = property(get_name)
    prices = property(get_prices, set_prices)
    URL = property(get_URL)
    description = property(get_description)
    kilometers = property(get_kilometers, set_kilometers)
    specifications = property(get_specifications)
    location = property(get_location)
    datePublished = property(get_datePublished)
    isForSale = property(get_isForSale, set_isForSale)
    fuel = property(get_fuel)
    transmision = property(get_transmision)

    # Set publication days
    def count_car_offers_today(car_offers):
        today = datetime.date.today()
        count = 0

        for car_offer in car_offers:
            if car_offer.datePublished.date() == today:
                count += 1

        return count