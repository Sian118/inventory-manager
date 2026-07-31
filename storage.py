import json
import os

file_path = "data/inventory.json"

def load_inventory():
    if not os.path.exists(file_path):
        return {}
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except:
        return {}

def save_inventory(inventory):
    with open(file_path, "w") as file:
        json.dump(inventory, file, indent=4)