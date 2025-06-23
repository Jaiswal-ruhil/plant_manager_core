# manufacturer.py

from typing import Dict

# Global registry for manufacturers
MANUFACTURER_REGISTRY: Dict[str, 'Manufacturer'] = {}

class Manufacturer:
    def __init__(self, manufacturer_id: str, name: str, country: str):
        self.manufacturer_id = manufacturer_id
        self.name = name
        self.country = country
        MANUFACTURER_REGISTRY[self.manufacturer_id] = self

    def to_dict(self) -> Dict:
        return {
            "manufacturer_id": self.manufacturer_id,
            "name": self.name,
            "country": self.country
        }

    def __str__(self):
        return f"{self.name} ({self.country})"
