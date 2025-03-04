import csv

# leer el archivo CSV
with open('products.csv', mode='r') as file:
    # gusrda el archivo en un diccionario
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(row) 
        
# mostrar el archivo CSV  por columnas  
with open('products.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(f"Producto : {row['name']}, precio: {row['price']}")
 