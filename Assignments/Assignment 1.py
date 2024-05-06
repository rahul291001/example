#Name: Rahul Subhash Gouda  
#StudentID: s4063983

#The Existing Customers 
customers = {
    "Kate": {"reward_points": 20, "order_history": []},  
    "Tom": {"reward_points": 32, "order_history": []},
}
#The Existing Products
products = {
    "vitaminC": {"price": 12.0, "dr_prescription": "n"},
    "vitaminE": {"price": 14.5, "dr_prescription": "n"},
    "coldTablet": {"price": 6.4, "dr_prescription": "n"},
    "vaccine": {"price": 32.6, "dr_prescription": "y"},
    "fragrance": {"price": 25.0, "dr_prescription": "n"}
}


def make_purchase():
    while True: #Used loop for the whole function to use break statement or any to use similar actions
        while True: #Used while loop to check if the name input is in the proper format or to give the customer another chance to give a proper input
            C_name = input("Enter the customer name[eg: Rahul]: ").strip()
            # To check if the given user is in the customer profile else make them as a new user
            if not C_name.isalpha():            # isalpha checks if all the input are in alphabets or not 
                print("Do not give number for your name.")
            elif C_name not in customers:   #if the user name is not in the c_name it makes the user name be a new user with 0 reward points and no order history
                customers[C_name] = {"reward_points": 0, "order_history": []}
                break
            else:
                break

        print("\nAll the available products")
        for product in products:
            print("-", product)

        # Get Products and quantity from user
        while True:     #We use while loop here to check if the input products is valid with valid inputs
            product_names = [name.strip() for name in input("Enter the products purchased").split(',')]
            if all(name in products for name in product_names):
                break
            else:
                print("Enter valid products")

        while True:      #We use while loop here to check if the input quantities is valid with valid inputs
            quantities_input = input("Enter the quantity ").strip()
            quantities_str = quantities_input.split(',')
            if len(quantities_str) != len(product_names):
                print("number of quantities should be equal to products.")
            elif all(quantity.strip().isdigit() and int(quantity.strip()) > 0 for quantity in quantities_str):
                quantities = [int(quantity.strip()) for quantity in quantities_str]
                break
            else:
                print("IInvalid quantity")

        products_ordered = []
        total_cost = 0

        # Get existing reward points before purchase
        existing_points = customers[C_name]["reward_points"]
        # Get product name and quantity entered by user to send it to record the order history of a user
        for product_name, quantity in zip(product_names, quantities):   #We zip the product_name and quantity to store multiple data and do the calculations of each product one after the other
            product_info = products[product_name]
            unit_price = product_info["price"]
            prescription_required = product_info["dr_prescription"]

            if prescription_required == "y":        #We use if statement to check for the valid input if it is y prints reciept else terminates the process and goes back to the menu
                while True:
                    prescription = input(f"We need prescription for this products. do you have one?").lower()
                    if prescription in ["y", "n"]:
                        break
                    else:
                        print("Enter only 'y' or 'n' ")
                        
                if prescription != "y":
                    print(f"Without prescription you can not buy this product")
                    return

            total_cost += unit_price * quantity

            # Append purchased product to products_ordered list
            products_ordered.append((product_name, unit_price, quantity))




        # To print the receipt after taking the inputs from the user
        print("\n---------------------------------------------------------")
        print(" " * 20 + "Receipt")
        print("---------------------------------------------------------")
        print("Name:".ljust(30), C_name)
        for product_name, unit_price, quantity in products_ordered:
            print("Product:".ljust(30), product_name)
            print("Unit Price:".ljust(30), "{:.2f}".format(unit_price), "(AUD)")
            print("Quantity:".ljust(30), quantity)
        print("---------------------------------------------------------")
        print("Total cost before points:".ljust(30), "{:.2f}".format(total_cost), "(AUD)")

        # Calculate the earned points,usable points and discount received to the user
        earned_points = round(total_cost)
        usable_points = min(existing_points, int(existing_points // 100) * 100)
        discount = usable_points // 100 * 10
        total_cost -= discount

        # After calculating the results print the reward points details
        print("Reward points used:".ljust(30), usable_points)
        print("Discount applied:".ljust(30), "{:.2f}".format(discount), "(AUD)")
        print("Total cost after discount:".ljust(30), "{:.2f}".format(total_cost), "(AUD)")
        print("---------------------------------------------------------")
        print("Total reward points earned:".ljust(30), earned_points)
        print("---------------------------------------------------------")

        customers[C_name]["reward_points"] = (existing_points - usable_points) + earned_points

        # Zip the product name and quantities to let the other functions use the values
        current_order = dict(zip(product_names, quantities))

        customers[C_name]["order_history"].append(current_order)
        # To check if the user wants to print another receipt.
        break

    print("Exiting purchase mode.")





def add_update_product():
    while True:
        # The multiple input given by a user will be seperated by ","
        product_info_list = input("Please enter the information of products ").strip()

        valid = True
        for product_info in product_info_list.split(','):
            # If any spaces in the given inout strip removes the given spaces by the user 
            product_info = product_info.strip()
            try:
                # Check the inputs given by user if is in the correct format and valid inputs
                product_name, price_str, dr_prescription = product_info.split()
                price = float(price_str)
                if price <= 0:
                    raise ValueError("Price must be positive.")
                if dr_prescription.lower() not in ["y", "n"]:
                    raise ValueError("Invalid prescription requirement. Enter 'y' or 'n'.")
            except ValueError:
                print("Invalid product information format. Please try again.")
                valid = False
                break

        if valid:
            # If the inputs given by the user is valid it takes in the input and stores it in the array after splitting each input
            for product_info in product_info_list.split(','):
                product_info = product_info.strip()
                product_name, price, dr_prescription = product_info.split()
                products[product_name] = {"price": float(price), "dr_prescription": dr_prescription}
            print("Product information updated successfully.")
            break
    
def display_customers():
    # To DIsplay all the exisiting customers and their total preward points which they have earned 
    print("\nExisting Customers and Their Reward Points:")
    if not customers:
        print("No customers found.")
    else:
        for customer, profile in customers.items():
            print(f"Customer: {customer}, Reward Points: {profile['reward_points']}")


def display_products():
    # To display all the existing products with their price and if prescription are needed or not 
    print("\nExisting Products:")
    if not products:
        print("No products found.")
    else:
        for product, info in products.items():
            prescription_required = "y" if info["dr_prescription"] == "y" else "n"
            print(f"Product: {product}, Price: ${info['price']}, Prescription Required: {prescription_required}")

def display_customer_order_history():
    # To check if the user exists if yes then display all his recent purchases in order to homany times the reciept is generated 
    C_name = input("Enter the customer name: ").strip()
    order_history = get_customer_orders(C_name)

    if not order_history:
        print(f"Customer '{C_name}' has no order history yet.")
        return

    print(f"This is the order history of {C_name}.\n")
    print(" "*20,"Products".ljust(27), "Total Cost".rjust(20), "Earned Rewards".rjust(20))
    order_count = 1
    for order in order_history:
        products_info = []
        total_cost = 0

        # Using the product and quantity which we get from make purchase we calculate the total cost and total reward points
        for product, quantity in order.items():
            product_info = products[product]
            unit_price = float(product_info["price"])  
            total_cost += unit_price * int(quantity)
            products_info.append(f"{quantity} x {product}")

        total_reward_points = round(total_cost)

        # Display the order history which has been generated
        print(f"Order {order_count}", end=" " * 10)
        print(", ".join(products_info).ljust(30), f"{round(total_cost, 2):.2f} AUD".rjust(20), f"{total_reward_points} Points".rjust(20))

        order_count += 1



def get_customer_orders(C_name):
    # This function helps us to get the data like order history from the make_pruchase function and implement it to genrate the order history
    C_name = C_name.strip() 
    return customers.get(C_name, {}).get("order_history", [])


def main_menu():
    while True:
        # This is the menu by which a user can make his choise of operations they want to perform
        print("\nMain Menu:")
        print("1. Make a purchase")
        print("2. Add/Update information of products")
        print("3. Display existing customers")
        print("4. Display existing products")
        print("5. Display a customer order history")
        print("6. Exit")

        choice = input("Please enter your choice (1-6): ")
        # Each choice has its own function which is called according to the function mentiond in teh menu
        if choice == "1":
            make_purchase()
        elif choice == "2":
            add_update_product()
        elif choice == "3":
            display_customers()
        elif choice == "4":
            display_products()
        elif choice == "5":
            display_customer_order_history()
        elif choice == "6":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

main_menu()


#This program has 5 different funtions 
#1) make_purchase: In this function the user enters his name, the user gives all the information on their purchase like the product name and quantity once all the valid inputs are given the data is stored to be used later like product name and quantity of purchase.
#2) add_update_product: In this function the user or the person using the program can update the existing products like price and if prescription is required or not the user can even add new products.
#3) display_customers: In this fnction the person can see all the customers who have made a purchase in the pharmacy and what their existing reward points are .
#4) display_products: In this function the person can look at all the products available and what are their price and if the need any prescription to buy the product.
#5) display_customer_order_history: In this function the person can look at the user on what are the purchase he has made in the pharmacy and how many reward points did he earn during that purchase.
#6) I used an additional function which is get_customer_orders in that function the it retrives the data of a user like product name and quantites that the user bought from the make_purchase function and order history uses that data to print the order history of a particular user using the username.