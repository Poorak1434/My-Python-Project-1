# Name: Poorak Pandey
# Enrollment Number: 2502140055

product_db = {}
master_pass = "ironman@123"


def login():
    attempts = 3
    while attempts > 0:
        pw = input("Enter the password to access the system: ")
        if pw == master_pass:
            print("Access granted.")
            return True
        else:
            attempts -= 1
            print(f"Incorrect password! Attempts left: {attempts}")

    print("Maximum attempts exhausted. Exiting program. Please Contact Poorak For the Password ")
    return False


def add_product():
    # Function to add a new item
    code = input("Enter product code: ")
    if code in product_db:
        print("Error: Product code already exists!")
        return

    name = input("Enter product name: ")
    try:
        price = float(input("Enter product price: "))
        stock = int(input("Enter product stock quantity: "))
    except ValueError:
        print("Invalid input for price or stock. Please enter numbers.")
        return

    if price <= 0 or stock < 0:
        print("Price must be positive and stock cannot be negative.")
        return

    product_db[code] = (name, price, stock)
    print(f"Product '{name}' added successfully.")


def modify_product():
    # Updates an existing product
    code = input("Enter product code to modify: ")
    if code in product_db:
        name = input("Enter new product name: ")
        try:
            price = float(input("Enter new price: "))
            stock = int(input("Enter new stock quantity: "))
        except ValueError:
            print("Invalid input for price or stock.")
            return

        if price <= 0 or stock < 0:
            print("Price must be positive and stock cannot be negative.")
            return

        product_db[code] = (name, price, stock)
        print("Product details updated.")
    else:
        print("Error: Product not found.")


def delete_product():
    # Deletes a product
    code = input("Enter product code to delete: ")
    if code in product_db:
        deleted_item = product_db.pop(code)  # Get item details before deleting
        print(f"Product '{deleted_item[0]}' deleted.")
    else:
        print("Error: Product not found.")


def view_products():
    # Shows current inventory
    print("\n--- CURRENT INVENTORY ---")
    print("CODE\tNAME\tPRICE\tQTY")
    print("-" * 40)
    if not product_db:
        print("No products in stock.")
        return

    for code, details in product_db.items():
        print(f"{code}\t{details[0]}\t{details[1]:.2f}\t{details[2]}")


def search_product():
    # Find a product by name or code
    query = input("Enter product name or code to search: ").lower()
    found_item = False

    # Unpack tuple directly in the loop
    for code, (name, price, stock) in product_db.items():
        if query == code.lower() or query == name.lower():
            print(f"Found: {code} - {name}, Price: {price:.2f}, Stock: {stock}")
            found_item = True

    if not found_item:
        print("Product not found.")


def generate_bill():
    # Creates a new bill for a customer
    current_bill = []
    print("--- New Bill --- (Type 'done' to finish)")

    while True:
        code = input("Enter product code: ")
        if code.lower() == "done":
            break

        if code not in product_db:
            print("Invalid code. Product not found.")
            continue

        # Check if already in bill (more "human" way than using a set)
        is_already_added = False
        for item in current_bill:
            if item['code'] == code:
                is_already_added = True
                break

        if is_already_added:
            print("Product already in bill. Please modify later if needed.")
            continue

        try:
            qty = int(input(f"Enter quantity for {product_db[code][0]}: "))
        except ValueError:
            print("Invalid quantity.")
            continue

        name, price, stock = product_db[code]

        # Check if quantity is valid
        if qty <= 0 or qty > stock:
            print(f"Invalid quantity (Must be > 0 and <= {stock})")
            continue

        bill_item = {"code": code, "name": name, "price": price, "qty": qty, "total": price * qty}
        current_bill.append(bill_item)

        # Update stock in main DB
        product_db[code] = (name, price, stock - qty)
        print(f"Added item: {name} (Qty: {qty})")

    # Print the final bill
    print("\n--- FINAL INVOICE ---")
    grand_total = 0
    print("CODE\tNAME\tPRICE\tQTY\tTOTAL")
    print("=" * 40)

    for item in current_bill:
        print(f"{item['code']}\t{item['name']}\t{item['price']:.2f}\t{item['qty']}\t{item['total']:.2f}")
        grand_total += item['total']

    print("-" * 40)
    print(f"GRAND TOTAL: Rs {grand_total:.2f}")
    print("Thank you for shopping!")


def main_menu():
    while True:
        print("\n==== Billing System Menu ====")
        print("1. Add New Product")
        print("2. Modify Product Details")
        print("3. Delete Product")
        print("4. View All Products")
        print("5. Search for a Product")
        print("6. Generate Bill")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            add_product()
        elif choice == "2":
            modify_product()
        elif choice == "3":
            delete_product()
        elif choice == "4":
            view_products()
        elif choice == "5":
            search_product()
        elif choice == "6":
            generate_bill()
        elif choice == "7":
            print("Logging out...")
            break
        else:
            print("Invalid option! Please try again.")


# Main program execution
if login():
    main_menu()