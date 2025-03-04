import csv

file_path = 'products.csv'
update_file_path = 'products_update.csv'


with open('products.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    # obtener los nombres de las columnas
    headers = csv_reader.fieldnames + ['total_value']
    # grabar los nombres de las columnas en el archivo de salida
    with open(update_file_path, mode='w', newline='') as update_file:
        csv_writer = csv.DictWriter(update_file, fieldnames=headers)
        csv_writer.writeheader() # grabar los nombres de las columnas
        # recorrer cada fila del archivo CSV
        for row in csv_reader:
            # calcular el valor total
            row['total_value'] = float(row['price']) * int(row['quantity'])
            # grabar la fila en el archivo de salida
            csv_writer.writerow(row)

print('Se ha actualizado el archivo CSV con la nueva columna total_value')