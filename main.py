from product import Product
from order import Order
from inventory import Inventory

# Sample usage
inventory = Inventory()

laptop = Product("P1", "Laptop", 999.99, 10)
phone = Product("P2", "Smartphone", 499.99, 20)

inventory.add_product(laptop)
inventory.add_product(phone)

order_products = [laptop, phone]
order = Order("O1", order_products, "John Doe")

print("Inventory:")
inventory.display_inventory()

print("\nPlacing Order:")
print(order)

