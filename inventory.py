
def list_all_items(inventory):
    if not inventory:
        print("Inventory is empty.")
        return
    for item_id, item in inventory.items():
        print(f"ID: {item_id}, Name: {item['name']}, Quantity: {item['quantity']}, Price: {item['price']}, Category: {item['category']}, Status: {item['status']}")
def add_item(inventory):
    try:
        item_id = input("Enter the ID of the item: ")
        name = input("Enter the name of the item: ")
        quantity = int(input("Enter the quantity of the item: "))
        price = float(input("Enter the price of the item: "))
        category = input("Enter the category of the item: ")

        if quantity < 0 or price < 0:
            print("Quantity and price cannot be negative.")
            return

        inventory[item_id] = {
            "name": name,
            "quantity": quantity,
            "price": price,
            "category": category,
            "status": "in stock"
        }
        print("Item added successfully.")
    except ValueError:
        print("Invalid input. Quantity and price must be numbers.")

def update_quantity(inventory):
    item_id = input("Enter item ID to update: ")
    if item_id not in inventory:
        print("Item not found.")
        return
    try:
        change = int(input("Enter quantity to add (or negative to remove): "))
        inventory[item_id]["quantity"] += change
        if inventory[item_id]["quantity"] <= 0:
            inventory[item_id]["status"] = "out of stock"
        print("Quantity updated.")
    except ValueError:
        print("Invalid number entered.")

def mark_out_of_stock(inventory):
    item_id = input("Enter the item you want to mark out of stock: ")
    if item_id not in inventory:
        print("Item not found.")
        return
    inventory[item_id]["status"] = "out of stock"
    print("Item marked as out of stock.")
def delete_item(inventory):
    item_id = input("Enter the item ID to delete: ")
    if item_id not in inventory:
        print("Item not found.")
        return
    del inventory[item_id]
    print("Item deleted successfully.")