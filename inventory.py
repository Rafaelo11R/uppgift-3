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

def view_product(products, product_id):
    for product in products:
        if product['id'] == product_id:
            return f"{product['name']} \t {product['desc']} \t {locale.currency(product['price'], grouping=True)}"
            break
    return "Product not found"

def add_product(products, product):
    products.append(product)


def delete_product(products, product_id):
    for product in products:
        if product['id'] == product_id:
            products.remove(product)
            print('Product removed!')
            break

    else:
        print("Product not found")
            


def get_products(products):
    product_list = []
    for product in products:
        product_info = f"{product['name']} \t {product['desc']} \t {locale.currency(product['price'], grouping=True)}"
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
        print(delete_product(products, id))

    except:
        print("You need to type in numbers")
        continue


