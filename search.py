def search_by_category(inventory):
    category = input("Enter the category you want to search for: ")
    found = False
    for item_id, item in inventory.items():
        if item["category"].lower() == category.lower():
            print(f"Item ID: {item_id}, Name: {item['name']}, Quantity: {item['quantity']}, Price: {item['price']}, Status: {item['status']}")
            found = True
    if not found:
        print("No items found in the specified category.")

def search_by_price_range(inventory):
    try:
        low = float(input("Enter minimum price: "))
        high = float(input("Enter maximum price: "))
        found = False
        for item_id, item in inventory.items():
            if low <= item["price"] <= high:
                print(item_id, item)
                found = True
        if not found:
            print("No items found in that price range.")
    except ValueError:
        print("Invalid price entered.")