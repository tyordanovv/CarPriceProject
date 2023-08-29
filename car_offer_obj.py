import datetime

class CarOffer:
    def __init__(self, ID, VIN, name, prices, year, URL, kilometers, category, location, datePublished, isForSale, fuel, transmision, visited, ps, source, lastChange):
        self._ID = ID
        self._VIN = VIN
        self._name = name
        self._prices = prices
        self._year = year
        self._URL = URL
        self._kilometers = kilometers
        self._category = category
        self._location = location
        self._datePublished = datePublished
        self._isForSale = isForSale
        self._fuel = fuel 
        self._transmision = transmision 
        self._visited = visited
        self._ps = ps
        self._source = source
        self._lastChange = lastChange

    # Getterss
    def get_id(self):
        return self._ID
    def get_VIN(self):
        return self._VIN
    def get_name(self):
        return self._name
    def get_prices(self):
        return self._prices
    def get_URL(self):
        return self._URL
    def get_year(self):
        return self._year
    def get_kilometers(self):
        return self._kilometers
    def get_category(self):
        return self._category
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
    def get_visited(self):
        return self._visited
    def get_ps(self):
        return self._ps
    def get_source(self):
        return self._source
    def get_lastChange(self):
        return self._lastChange
    

    # Setters
    def set_isForSale(self, value):
        self._isForSale = value
    def set_prices(self, value):
        self._prices.append(value)
    def set_kilometers(self, value):
        self._kilometers = value
    def set_visited(self, value):
        self._visited = value
    def set_lastChange(self, value):
        self._lastChange = value

    # Properties for attributes
    id = property(get_id)
    VIN = property(get_VIN)
    name = property(get_name)
    prices = property(get_prices, set_prices)
    year = property(get_year)
    URL = property(get_URL)
    kilometers = property(get_kilometers, set_kilometers)
    category = property(get_category)
    location = property(get_location)
    datePublished = property(get_datePublished)
    isForSale = property(get_isForSale, set_isForSale)
    fuel = property(get_fuel)
    transmision = property(get_transmision)
    visited = property(get_visited, set_visited)
    ps = property(get_ps)
    source = property(get_source)
    lastChange = property(get_lastChange, set_lastChange)
    def as_dict(self):
        return {
            "ID": self._ID,
            "VIN": self._VIN,
            "name": self._name,
            "prices": self._prices,
            "year": self._year,
            "URL": self._URL,
            "kilometers": self._kilometers,
            "category": self._category,
            "location": self._location,
            "datePublished": self._datePublished,
            "isForSale": self._isForSale,
            "fuel": self._fuel,
            "transmission": self._transmision,
            "visited": self._visited,
            "ps": self._ps,
            "source": self._source,
            "lastChange": self._lastChange
        }
    # Set publication days
    def count_car_offers_today(car_offers):
        today = datetime.date.today()
        count = 0

        for car_offer in car_offers:
            if car_offer.datePublished.date() == today:
                count += 1

        return count