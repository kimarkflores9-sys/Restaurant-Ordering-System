from menu import display_menu
from order import get_orders, calculate_total
from receipt import print_receipt


def main():
    menu = {
        "Chickenjoy": 99,
        "Spaghetti": 65,
        "Yumburger": 45,
        "Burger Steak": 75,
        "Fries": 55,
        "Coke": 35,
    }

    print("\nWELCOME TO OUR RESTAURANT!")
    display_menu(menu)

    choice = input("\nDo you want to order? (yes/no): ").lower()

    if choice == "no":
        print("Thank you! Goodbye!")
        return

    if choice == "yes":
        orders = get_orders(menu)
        subtotal = calculate_total(orders, menu)
        print_receipt(orders, menu, subtotal)
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()