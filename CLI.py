import sys
import os

# This tells Python to look in the current folder for your modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# 1. IMPORT the service function here
from authentication.Models.repo import InventoryRepo 
from authentication.Models.class_file import Product 
from authentication.services.ser import fetch_from_openfoodfacts
repo = InventoryRepo()

def main_menu():
    print("\n --- Retail Inventory System ---")
    print("1. View Inventory")
    print("2. Add Product (via Barcode)")
    print("3. Delete Product")
    print("4. Exit")
    
    choice = input("Select an option: ")
    
    if choice == '1':
        items = repo.get_all()
        if not items:
            print("Inventory is currently empty.")
        for i in items: 
            print(f"ID: {i['id']} | {i['product_name']} | Stock: {i['stock']}")
        
    elif choice == '2':
        barcode = input("Enter Barcode: ")
        details = fetch_from_openfoodfacts(barcode)
        
        if details:
            try:gcd
                price = float(input("Enter Price: "))
                stock = int(input("Enter Stock: "))
                # We use 'Product' here to match our Model
                p = Product(barcode=barcode, price=price, stock=stock, **details)
                repo.add(p)
                print("Product Added Successfully!")
            except ValueError:
                print("Invalid input for price or stock.")
        else:
            print("Product not found in OpenFoodFacts API.")

    elif choice == '3':
        p_id = input("Enter ID to delete: ")
        if repo.delete(p_id):
            print(f"Product {p_id} deleted.")
        else:
            print("Product ID not found.")

    elif choice == '4':
        sys.exit()

if __name__ == "__main__":
    while True:
        main_menu()