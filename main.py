from storage import load_inventory, save_inventory
from inventory import add_item, update_quantity, mark_out_of_stock
from search import search_by_category, search_by_price_range

def main():
    inventory = load_inventory()
    while True:
        print("Inventory Management System")
        print("1. Add Item")
        print("2. Update Quantity")
        print("3. Mark Item as Out of Stock")
        print("4. Search by Category")
        print("5. Search by Price Range")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
          add_item(inventory)
        elif choice == "2":
          update_quantity(inventory)
        elif choice == "3":
          mark_out_of_stock(inventory)
        elif choice == "4":
            search_by_category(inventory)
        elif choice == "5":
            search_by_price_range(inventory)
        elif choice == "6":
            save_inventory(inventory)
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

main()