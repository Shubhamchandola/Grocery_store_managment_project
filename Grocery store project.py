# Grocery Store Application

# Welcome message to Customer...!

user_name = input("Please Input Your Name = ")
Welcome_message = f"Welcome to Our Store {user_name}"
Wlmsg = len(Welcome_message)
print("*"*Wlmsg)
print(Welcome_message)
print("*"*Wlmsg)

# Function to display the available items and their prices
def display_all_items(items):
    print("Available items in our store :")
    
    for item, price in items.items():
        print(f"{item}: Rs{price}")

# Function to add items to the shopping cart
def add_to_cart(cart, items, item_name, quantity):
    if item_name in items:
        price = items[item_name]
        if item_name in cart:
            cart[item_name] += quantity
        else:
            cart[item_name] = quantity
        print(f"Added {quantity} {item_name}(s) to the cart.")
    else:
        print("Item not available.")

# Function to remove items from the shopping cart
def remove_from_cart(cart, item_name, quantity):
    if item_name in cart:
        if cart[item_name] >= quantity:
            cart[item_name] -= quantity
            print(f"Removed {quantity} {item_name}(s) from the cart.")
            if cart[item_name] == 0:
                del cart[item_name]
        else:
            print(f"Not enough {item_name} in the cart.")
    else:
        print(f"{item_name} not found in the cart.")

# Function to calculate the total cost of items in the cart
def calculate_total(cart, items):
    total = 0
    for item_name, quantity in cart.items():
        if item_name in items:
            price = items[item_name]
            total += price * quantity
    return total

# Main program
def main():
    # Available items and their prices
    items = {
        "oil": 145,
        "aata": 380,
        "rice": 40,
        "bread": 25,
        "milk": 33,
        "sugar": 42,

    }

    cart = {}

    while True:
        print("\n1. Display available items")
        print("2. Add item to cart")
        print("3. Remove item from cart")
        print("4. Calculate total cost")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            display_all_items(items)
        elif choice == "2":
            item_name = input("Enter the item name: ")
            quantity = int(input("Enter the quantity: "))
            add_to_cart(cart, items, item_name, quantity)
        elif choice == "3":
            item_name = input("Please Enter the item name: ")
            quantity = int(input("Please Enter the quantity: "))
            remove_from_cart(cart, item_name, quantity)
        elif choice == "4":
            total = calculate_total(cart, items)
            print(f"Your Total Bill is **************: Rs {total}")
        elif choice == "5":
            print("Thank you for shopping Please Visit again ")
            break
        else:
            print("Opps you choose a Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()

# Code write by shubham and this code is under testing for further expermental !