User
-----
user_id (PK)
name
email

        │
        │
        ▼

Purchase
---------
purchase_id (PK)
user_id (FK)
product_id (FK)
quantity
purchase_date

        ▲
        │

Product
--------
product_id (PK)
product_name
category
avg_shelf_life_days

        │
        ▼

Inventory
----------
inventory_id (PK)
purchase_id (FK)
expiry_date
quantity_remaining
status

        │
        ▼

Waste
------
waste_id (PK)
inventory_id (FK)
quantity_wasted
waste_reason
waste_date