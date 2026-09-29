def print_receipt(orders, menu, subtotal):
    print("\n================================")
    print("       RESTAURANT RECEIPT")
    print("================================")
    for order in orders:
        item = order[0]
        quantity = order[1]
        price = menu[item]
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