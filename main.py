from storage import load_inventory, save_inventory
from inventory import add_item, update_quantity, mark_out_of_stock, list_all_items
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
       print("6. List All Items")
       print("7. Exit")
       choice = input("Enter your choice: ")
       

main()