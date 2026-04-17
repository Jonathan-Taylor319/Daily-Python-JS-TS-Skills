# new month same challenges

# 🐍 Challenge 9 — Mini Store Inventory
# Build a small store inventory system.
# 1. add_item(inventory, name, price, quantity) — adds item, name should be lowercased
# 2. sell_item(inventory, name, quantity) — reduces quantity when sold, handle: item not found, not enough stock, wrong input type
# 3. restock_item(inventory, name, quantity) — increases quantity, handle: item not found
# 4. total_inventory_value(inventory) — returns total value of ALL stock (price × quantity for each item, added together)
# 5. low_stock(inventory) — returns list of items with quantity 5 or below
# 6. most_valuable_item(inventory) — returns item with highest total value (price × quantity)

mini_store = {}

def add_item(inventory, name, price, quantity):
        name = name.lower()
        inventory[name] = {"price": price, "quantity": quantity}
        return inventory

add_item(mini_store, "Monster", 2.99, 20)
add_item(mini_store, "Red Bull", 2.99, 30)
add_item(mini_store, "Milk 2%", 4.99, 10)
add_item(mini_store, "Milk Chocolate", 1.99, 25)
add_item(mini_store, "Monster Rehab - Berry Tea", 2.99, 45)
add_item(mini_store, "Milk Strawberry", 1.99, 50)
add_item(mini_store, "Doritos", 2.50, 68)


def simple_inventory_list(inventory):
        for name, details in inventory.items():
                print(name, details)

simple_inventory_list(mini_store)

def sell_item(inventory, name, sold_ammount):
        if name in inventory:
                current_ammount = inventory[name]["quantity"]
                if current_ammount > 0 and sold_ammount < current_ammount:
                        inventory[name]["quantity"] = current_ammount - sold_ammount
                else:
                        return "Either not enough in stock or too much sold"
        else:
                return f"{name} not in inventory"
        
def restock_item(inventory, name, amount_stocked):
        if name in inventory:
                current_ammount = inventory[name]["quantity"]
                inventory[name]["quantity"] = current_ammount + amount_stocked
        else:
                return f"{name} is not in your inventory - please add properly first"
        
def total_inventory_value(inventory):
        total = 0
        for _, details in inventory.items():
                total = total + (details["price"] * details["quantity"])
        return f"total amount of inventory: ${total:.2f}" # adding the :.2f floats decimal to tenths

print(total_inventory_value(mini_store))

def low_stock(inventory):
        low_stock = []
        for name, details in inventory.items():
                stock = details["quantity"]
                if stock <= 5:
                        low_stock.append(name)
        return low_stock

def most_valuable_item(inventory):
        most_val = max(inventory, key=lambda name: inventory[name]["price"] * inventory[name]["quantity"])
        return f"the most valuable thing in stock is {most_val}"

print(most_valuable_item(mini_store))
        
                

                        


