def display_menu(menu):
    print("\n========== MENU ==========")
    for item, price in menu.items():
        print(f"{item} - ₱{price}")
    print("===========================")