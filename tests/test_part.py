from system import Part
import pprint

# Create a part
part = Part(
    access_key="PART-001",
    manufacturer_id="M001",
    manufacturer_sku="ACME-P123",
    client_sku="CLIENT-PART1",
    description="Replacement part for control unit",
    datasheet={"material": "Aluminum", "weight": "1.2kg"}
)

print(part)
pprint.pprint(part.to_dict())
