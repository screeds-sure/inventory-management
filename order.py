from datetime import datetime

class Order:
    def __init__(self, order_id, products, customer_name):
        self.order_id = order_id
        self.products = products
        self.customer_name = customer_name
        self.order_date = datetime.now()

    def total_order_cost(self):
        return sum(product.price for product in self.products)

    def __str__(self):
        return f"Order ID: {self.order_id}, Customer: {self.customer_name}, Date: {self.order_date}, Total Cost: ${self.total_order_cost()}"
