# s.py

class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ShippingAddress:
    def __init__(self, street, city, country):
        self.street = street
        self.city = city
        self.country = country

class Order:
    def __init__(self, customer, items, shipping_address):
        self.customer = customer
        self.items = items
        self.shipping_address = shipping_address

    def calculate_total_cost(self):
        total_cost = sum(item.price for item in self.items)
        return total_cost

class OrderValidator:
    def validate_order(self, order):
        #validates order and checks customer email
        pass

class EmailSender:
    def send_confirmation_email(self, order):
        print("Sending order confirmation email to:", order.customer.email)
        print("Email sent successfully.")

class InventoryManager:
    def update_inventory(self, order):
        print("Updating inventory for order...")
        for item in order.items:
            print("Item:", item.name, "Quantity:", 1)
        print("Inventory updated successfully.")


def main():

    customer = Customer("Andrew Womack", "andwoma@siue.edu")
    items = [Item("Computer", 1500), Item("Monitor", 350)]
    shipping_address = ShippingAddress("123 Main St", "Edwardsville", "USA")

    order = Order(customer, items, shipping_address)

    total_cost = order.calculate_total_cost()
    print("Total order cost: $", total_cost)

    order_validator = OrderValidator()
    order_validator.validate_order(order)

    email_sender = EmailSender()
    email_sender.send_confirmation_email(order)

    inventory_manager = InventoryManager()
    inventory_manager.update_inventory(order)

if __name__ == "__main__":
    main()
#dummy data with no present for checking email or inventory