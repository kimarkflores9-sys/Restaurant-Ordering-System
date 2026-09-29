from ordering_system import RestaurantSystem


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

    restaurant = RestaurantSystem(menu)
    restaurant.display_menu()

    choice = input("\nDo you want to order? (yes/no): ").lower()

    if choice == "no":
        print("Thank you! Goodbye!")
        return

    if choice == "yes":
        restaurant.take_orders()
        restaurant.print_receipt()
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()