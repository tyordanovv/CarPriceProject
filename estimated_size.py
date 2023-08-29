import json
from car_offer_obj import CarOffer

class CarOfferEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, CarOffer):
            return obj.__dict__  
        return super().default(obj)
    
car_offer = CarOffer(
    ID=1234567890,
    VIN="1234567890QWE", 
    name="Audi A6",
    prices=[12345, 12345],  
    year=12/1/2001,
    URL="https://suchen.mobile.de/fahrzeuge/details.html?id=373271149&damageUnrepaired=NO_DAMAGE_UNREPAIRED&isSearchRequest=true&pageNumber=2&scopeId=C&sortOption.sortBy=creationTime&sortOption.sortOrder=DESCENDING&searchId=0f0dd5b2-4f56-e425-ea40-baf2567f6261&ref=srp",
    kilometers=12345678,
    category="Limosine",
    location="Burgas Bulgaria",  
    datePublished=12/1/2001,  
    isForSale=True,  
    fuel="Dizel",
    transmision="Manual",
    visited=12/1/2001, 
    ps=1234,
    source="AUTO.BG"
)
serialized_data = json.dumps(car_offer, cls=CarOfferEncoder)
serialized_size_bytes = len(serialized_data.encode('utf-8'))

max_message_size_bytes = 256 * 1024

estimated_message_count = max_message_size_bytes // serialized_size_bytes

print(f"Serialized Size: {serialized_size_bytes} bytes")
print(f"Estimated Messages in One SQS Message: {estimated_message_count}")