
customer_profiles = {"Kate": 20,"Tom": 32}

available_products = {
    "vitaminC": {"price": 12.0, "dr_prescription": "n"},
    "vitaminE": {"price": 14.5, "dr_prescription": "n"},
    "coldTablet": {"price": 6.4, "dr_prescription": "n"},
    "vaccine": {"price": 32.6, "dr_prescription": "y"},
    "fragrance": {"price": 25.0, "dr_prescription": "n"}
}

def make_purchase():
    while True:
        customer_name = input("Please enter the customer's name: ")

        if customer_name not in customer_profiles:
            customer_profiles[customer_name] = 0

        print("\nAvailable Products:")
        for product in available_products:
            print("-", product)

        product_names = input("Please enter the names of the products separated by commas: ").split(',')
        quantities = input("Please enter the quantities of the products separated by commas: ").split(',')

        products_ordered = []
        total_cost = 0
        reward_points = customer_profiles.get(customer_name, 0)  

        for product_name, quantity_str in zip(product_names, quantities):
            product_name = product_name.strip()
            quantity_str = quantity_str.strip()

            if product_name not in available_products:
                print(f"Invalid product name '{product_name}'. Please select from the available products.")
                continue

            if not quantity_str.isdigit():
                print(f"Invalid quantity '{quantity_str}'. Please enter a valid integer quantity.")
                continue

            quantity = int(quantity_str)
            if quantity <= 0:
                print("Please enter a positive quantity.")
                continue

            product_info = available_products[product_name]
            unit_price = product_info["price"]
            prescription_required = product_info["dr_prescription"]

            if prescription_required == "y":
                prescription = input(f"{product_name} requires a prescription. Do you have it? (y/n): ").lower()
                if prescription != "y":
                    print(f"Prescription required for {product_name}. Please try a different product.")
                    continue

            total_cost += unit_price * quantity
            reward_points += round(unit_price * quantity)
            products_ordered.append((product_name, unit_price, quantity))

        print("\n---------------------------------------------------------")
        print(" " * 20 + "Receipt")
        print("---------------------------------------------------------")
        print("Name:".ljust(30), customer_name)
        for product_name, unit_price, quantity in products_ordered:
            print("Product:".ljust(30), product_name)
            print("Unit Price:".ljust(30), "{:.2f}".format(unit_price), "(AUD)")
            print("Quantity:".ljust(30), quantity)
        print("---------------------------------------------------------")
        print("Total cost before points:".ljust(30), "{:.2f}".format(total_cost), "(AUD)")

        # Redeem reward points (every 100 points = $10 discount)
        usable_points = min(reward_points, int(reward_points // 100) * 100)  # Limit usable points to multiples of 100
        discount = usable_points // 100 * 10  # Convert points to discount amount
        total_cost -= discount

        print("Reward points used:".ljust(30), usable_points)
        print("Discount applied:".ljust(30), "{:.2f}".format(discount), "(AUD)")
        print("Total cost after discount:".ljust(30), "{:.2f}".format(total_cost), "(AUD)")

        print("---------------------------------------------------------")
        print("Total reward points earned:".ljust(30), reward_points)
        print("---------------------------------------------------------")

        # Update customer profile with remaining reward points after redemption
        customer_profiles[customer_name] = reward_points - usable_points

        choice = input("\nDo you want to process another receipt? (y/n): ").lower()
        if choice != "y":
            break

    print("Exiting purchase mode.")



def add_update_product():
    product_info = input("Please enter the product information (name price dr_prescription): ").split()

    if len(product_info) != 3:
        print("Invalid input format. Please enter name, price, and prescription status separated by spaces.")
        return

    product_name = product_info[0]
    try:
        price = float(product_info[1])
    except ValueError:
        print("Invalid price format. Please enter a valid number for the price.")
        return

    dr_prescription = product_info[2].lower()
    if dr_prescription not in ["y", "n"]:
        print("Invalid prescription status. Please enter 'y' or 'n' for prescription requirement.")
        return

    available_products[product_name] = {"price": price, "dr_prescription": dr_prescription}
    print("Product information updated successfully.")

    
def display_customers():
    print("\nExisting Customers and Their Reward Points:")
    if not customer_profiles:
        print("No customers found.")
    else:
        for customer, reward_points in customer_profiles.items():
            print(f"Customer: {customer}, Reward Points: {reward_points}")


def display_products():
    print("\nExisting Products:")
    if not available_products:
        print("No products found.")
    else:
        for product, info in available_products.items():
            prescription_required = "y" if info["dr_prescription"] == "y" else "n"
            print(f"Product: {product}, Price: ${info['price']}, Prescription Required: {prescription_required}")


def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. Make a purchase")
        print("2. Add/Update product information")
        print("3. Display existing customers")
        print("4. Display existing products")
        print("5. Exit")

        choice = input("Please enter your choice (1-5): ")

        if choice == "1":
            make_purchase()
        elif choice == "2":
            add_update_product()
        elif choice == "3":
            display_customers()
        elif choice == "4":
            display_products()
        elif choice == "5":
            print("need to be developed.")
        elif choice == "6":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

main_menu()

