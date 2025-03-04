import csv

new_products = {
'name': 'Laptop', 
'price': 800, 
'quantity': 4, 
'brand': 'Apple',
'category': 'Technology', 
'entry_date': '2021-09-01', 
'total_value': 3200
 }
    # {'name': 'Keyboard', 'price': 50, 'quantity': 5, 'brand': 'Logitech', 'category': 'Technology', 'entry_date': '2021-09-02', 'total_value': 250},
    # {'name': 'Mouse', 'price': 20, 'quantity': 10, 'brand': 'Logitech', 'category': 'Technology', 'entry_date': '2021-09-03', 'total_value': 200},
    # {'name': 'Monitor', 'price': 200, 'quantity': 3, 'brand': 'Samsung', 'category': 'Technology', 'entry_date': '2021-09-04', 'total_value': 600}

# leer el archivo CSV
with open('products.csv', mode='a', newline='') as file:
    file.write('\n')
    csv_writer = csv.DictWriter(file, fieldnames=new_products.keys())
    csv_writer.writerow(new_products)
    print('Se han agregado los productos al archivo CSV')
    
