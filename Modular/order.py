def get_orders(menu):
    orders = []
    while True:
        item = input("\nEnter item: ").title()
        if item not in menu:
            print("Item not available.")
            continue

        try:
            quantity = int(input("Enter quantity: "))
        except ValueError:
            print("Invalid quantity! Please enter a number.")
            continue

        orders.append([item, quantity])
        another = input("Order another item? (yes/no): ").lower()
        if another == "no":
            break
    return orders


def calculate_total(orders, menu):
    subtotal = 0
    for order in orders:
        item = order[0]
        quantity = order[1]
        subtotal += menu[item] * quantity
    return subtotal