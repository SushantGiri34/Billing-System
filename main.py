import os
from datetime import datetime

# Make a folder to save bills
if not os.path.exists("bills"):
    os.mkdir("bills")

def create_bill():
    customer_name = input("Enter Customer Name: ")
    items = []
    
    while True:
        item = input("Enter item name: ")
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price: "))
        items.append((item, quantity, price))

        more = input("Add more items? (y/n): ").lower()
        if more != 'y':
            break

    # Bill calculations
    total = 0
    for item in items:
        total += item[1] * item[2]
    
    gst = total * 0.18
    grand_total = total + gst

    # Save to file
    time_now = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"bills/{customer_name}_{time_now}.txt"
    
    with open(filename, "w") as f:
        f.write(f"Customer: {customer_name}\n")
        f.write(f"Date: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}\n")
        f.write("-" * 40 + "\n")
        f.write("Item\tQty\tPrice\n")
        f.write("-" * 40 + "\n")
        for item in items:
            f.write(f"{item[0]}\t{item[1]}\t{item[2]}\n")
        f.write("-" * 40 + "\n")
        f.write(f"Subtotal:\t\t{total:.2f}\n")
        f.write(f"GST (18%):\t\t{gst:.2f}\n")
        f.write(f"Total:\t\t{grand_total:.2f}\n")
    
    print("Bill saved successfully.")

def view_bills():
    files = os.listdir("bills")
    if not files:
        print("No bills found.")
        return
    
    print("\nAvailable Bills:")
    for i, file in enumerate(files):
        print(f"{i+1}. {file}")
    
    choice = int(input("Enter number to view bill: ")) - 1
    if 0 <= choice < len(files):
        with open(f"bills/{files[choice]}", "r") as f:
            print("\n" + f.read())
    else:
        print("Invalid choice.")

# Main Menu
while True:
    print("\n--- Simple Billing System ---")
    print("1. Create New Bill")
    print("2. View Existing Bills")
    print("3. Exit")
    
    user_choice = input("Choose an option: ")
    
    if user_choice == '1':
        create_bill()
    elif user_choice == '2':
        view_bills()
    elif user_choice == '3':
        print("Thank you!")
        break
    else:
        print("Invalid choice. Try again.")
def view_bills():
    files = os.listdir("bills")
    if not files:
        print("No bills found.")
        return

    print("\nAvailable Bills:")
    for i, file in enumerate(files):
        print(f"{i+1}. {file}")

    try:
        choice = int(input("Enter number to view bill: ")) - 1
        if 0 <= choice < len(files):
            file_path = f"bills/{files[choice]}"
            with open(file_path, "r") as f:
                lines = f.readlines()

                # Print summary only (last 3 lines usually)
                print("\n" + "-"*30)
                print("BILL SUMMARY")
                print("-"*30)
                for line in lines[-3:]:  # last 3 lines contain totals
                    print(line.strip())

            delete = input("\nDo you want to delete this bill? (y/n): ")
            if delete.lower() == 'y':
                os.remove(file_path)
                print("Bill deleted.")
            else:
                print("Bill not deleted.")

        else:
            print("Invalid choice.")
    except Exception as e:
        print("Error:", e)
