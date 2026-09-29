class RestaurantSystem:

    def __init__(self, menu):
        self.menu = menu
        self.orders = []

    def display_menu(self):
        print("\n========== MENU ==========")
        for item, price in self.menu.items():
            print(f"{item} - ₱{price}")
        print("===========================")

    def take_orders(self):
        while True:
            item = input("\nEnter item: ").title()
            if item not in self.menu:
                print("Item not available.")
                continue

            try:
                quantity = int(input("Enter quantity: "))
            except ValueError:
                print("Invalid quantity! Please enter a number.")
                continue

            self.orders.append([item, quantity])
            another = input("Order another item? (yes/no): ").lower()
            if another == "no":
                break

    def calculate_total(self):
        subtotal = 0
        for order in self.orders:
            item = order[0]
            quantity = order[1]
            subtotal += self.menu[item] * quantity
        return subtotal

    def print_receipt(self):
        subtotal = self.calculate_total()
        print("\n================================")
        print("       RESTAURANT RECEIPT")
        print("================================")
        for order in self.orders:
            item = order[0]
            quantity = order[1]
            price = self.menu[item]
            total_price = price * quantity

            print(item)
            print("Quantity:", quantity)
            print("Price:", "₱", price)
            print("Total:", "₱", total_price)
            print("--------------------------------")

        print("TOTAL ORDER: ₱", subtotal)
        print("================================")
        print("     THANK YOU FOR ORDERING!")
        print("================================")