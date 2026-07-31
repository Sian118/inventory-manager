def add_item(inventory):
    try:
        item_id = input("Enter the ID of the item: ")
        name = input("Enter the name of the item: ")
        quantity = int(input("Enter the quantity of the item: "))
        price = float(input("Enter the price of the item: "))
        category = input("Enter the category of the item: ")
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