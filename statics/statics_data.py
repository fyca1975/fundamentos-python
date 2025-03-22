import statistics
import csv

# leer los datos de ventas mensulaes de un archivo csv
monthly_sales = {}
with open('monthly_sales.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        month = row['month']
        sales = int(row['sales'])
        monthly_sales[month] = sales

sales = list(monthly_sales.values())
print(f"ventas : {sales}")


#hallar la media con la libreria
mean_sales = statistics.mean(sales)
print(f"la Media es {mean_sales}")

#hallar la mediana con la libreria
median_sales = statistics.median(sales)
print(f"la Mediana es {median_sales}")

#hallar la moda con la libreria
mode_sales = statistics.mode(sales)
print(f"la Moda es {mode_sales}")   # si hay mas de una moda, se obtiene un error   

#hallar la desviacion estandar con la libreria
stdev_sales = statistics.stdev(sales)
print(f"la Desviacion Estandar es {stdev_sales}")   # si hay mas de una moda, se obtiene un error

#hallar la varianza con la libreria 
variance_sales = statistics.variance(sales)
print(f"la Varianza es {variance_sales}")   # si hay mas de una moda, se obtiene un error

#hallar el maximo con la libreria
max_sales = max(sales)
print(f"el Maximo es {max_sales}")      

#hallar el minimo con la libreria
min_sales = min(sales)
print(f"el Minimo es {min_sales}")  
