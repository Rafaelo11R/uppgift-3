import csv
import os
import locale

def load_data(filename):
    products = [] 
    
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            id = int(row['id'])
            name = row['name']
            desc = row['desc']
            price = float(row['price'])
            quantity = int(row['quantity'])
            
            products.append(
                {                   
                    "id": id,       
                    "name": name,
                    "desc": desc,
                    "price": price,
                    "quantity": quantity
                }
            )
    return products

def remove_product(products, id):
    temp_product = None

    for product in products:
        if product['id'] == id:
            temp_product = product
            break

        if temp_product:
            products.remove(temp_product)
            return f"{temp_product['name']} togs bort"
        else:
            return f"Kunde inte hitta produkt"


def view_product(products, product_id):
    for product in products:
        if product['id'] == product_id:
            return f"{product['name']} \t {product['desc']} \t {locale.currency(product['price'], grouping=True)}"
            break
    return "Product not found"

def add_product(products, product):
    products.append(product)


def remove_product(products, product_id):
    for product in products:
        if product['id'] == product_id:
            products.remove(product)
            print('Product removed!')
            break

    else:
        print("Product not found")
            


def get_products(products):
    product_list = []
    for index,  product in enumerate(products,1):
        product_info = f"{index}. {product['name']} \t {product['desc']} \t {locale.currency(product['price'], grouping=True)}"
        product_list.append(product_info)
    
    return "\n".join(product_list)

locale.setlocale(locale.LC_ALL, 'sv_SE.UTF-8')  

os.system('cls' if os.name == 'nt' else 'clear')  # Clear terminal screen
products = load_data('db_products.csv')

while True:
    try:
        os.system("cls")
        print(get_products(products))
        id = int(input("Vilken"))
        print(remove_product(products, id))

        choice = ("vill du (T)a bort eller (V)isa produkt").strip().upper()

       
        if choice == "T":
                id = int(input("Vilken produkt vill du ta bort? "))

            
        if choice in ["T", "V"]:
            if id >= 1 and id <= len(products):
                selected_product = products[id -1]

                id = selected_product['id']

                remove_product(products, id)

                print(remove_product(products, id))




    except:
        print("You need to type in numbers")
        continue


