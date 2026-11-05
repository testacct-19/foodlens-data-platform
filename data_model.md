# Source Data Model (App / OLTP)

This is how the FoodLens app stores data: normalised tables linked by keys.
It is the *source* for the pipeline. The Snowflake warehouse model
(facts and dimensions) is documented separately.

Household
-----
household_id (PK)
name
email

        │
        │
        ▼

Purchase
---------
purchase_id (PK)
household_id (FK)
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