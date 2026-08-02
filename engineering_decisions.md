# Engineering Decisions

## Decision 1

### Why is expiry_date stored in Inventory instead of Product?

Products have an average shelf life, but each purchase has a different expiry date depending on when it was bought.

Therefore, actual expiry belongs to Inventory.