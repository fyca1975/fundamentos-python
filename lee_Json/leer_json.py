import json

new_products = {
'name': 'Laptop', 
'price': 800, 
'quantity': 4, 
'brand': 'Apple',
'category': 'Technology', 
'entry_date': '2021-09-01'
 }


# # Abre el archivo productos.json en modo lectura
# with open('productos.json', mode='r') as file:
#     products = json.load(file)

# # Imprime el contenido del archivo productos.json
# for product in products:
#     # print(product)
#     print(f"Nombre: {product['name']}, Precio: {product['price']}, Stock: {product['quantity']}")
#     # print()


# # Abre el archivo productos.json en modo escritura
with open('productos.json', mode='r') as file:
    products = json.load(file)

# Agrega un nuevo producto a la lista de productos y lo guarda en el archivo productos.json
products.append(new_products)

with open('productos.json', mode='w') as file:
    json.dump(products, file, indent=4)