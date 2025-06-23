# system.py

from typing import List, Dict, Optional
from manufacturer import Manufacturer, MANUFACTURER_REGISTRY

class System:
    def __init__(
        self,
        access_key: str,
        manufacturer_sku: str,
        client_sku: str,
        description: str,
        manufacturer_id: str,
        datasheet: Optional[Dict] = None,
    ):
        self.access_key = access_key
        self.manufacturer_sku = manufacturer_sku
        self.client_sku = client_sku
        self.description = description
        self.manufacturer_id = manufacturer_id
        self.datasheet = datasheet or {}
        self.subsystems: List['System'] = []

    @property
    def manufacturer(self) -> Optional[Manufacturer]:
        return MANUFACTURER_REGISTRY.get(self.manufacturer_id)

    def add_subsystem(self, subsystem: 'System'):
        self.subsystems.append(subsystem)

    def to_dict(self) -> Dict:
        return {
            "access_key": self.access_key,
            "manufacturer_sku": self.manufacturer_sku,
            "client_sku": self.client_sku,
            "description": self.description,
            "datasheet": self.datasheet,
            "manufacturer": self.manufacturer.to_dict() if self.manufacturer else None,
            "subsystems": [s.to_dict() for s in self.subsystems]
        }

    def __str__(self):
        return f"System({self.access_key}, Manufacturer: {self.manufacturer}, Subsystems: {len(self.subsystems)})"


class Part(System):
    def __init__(
        self,
        access_key: str,
        manufacturer_id: str,
        manufacturer_sku: str = "",
        client_sku: str = "",
        description: str = "",
        datasheet: Optional[Dict] = None,
    ):
        # Enforce that access_key and manufacturer_id are mandatory
        if not access_key or not manufacturer_id:
            raise ValueError("Both 'access_key' and 'manufacturer_id' are required for a Part.")
        
        # Call the System constructor
        super().__init__(
            access_key=access_key,
            manufacturer_sku=manufacturer_sku,
            client_sku=client_sku,
            description=description,
            manufacturer_id=manufacturer_id,
            datasheet=datasheet
        )

    def __str__(self):
        return f"Part({self.access_key}, Manufacturer: {self.manufacturer})"