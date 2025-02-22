# leer un archiuvos de texto  linea por linea
# with open('cuento.txt','r') as file:
#     for line in file:
#         print(line.strip())

# leer todas las lineas de un archivo de texto en una lista
# with open('cuento.txt','r') as file:
#     lines = file.readlines()
#     print(lines)
#     print(type(lines))  
#     print(lines[0])

# escribir en un archivo de texto, con 'a' escribir al final del archivo, con 'w' sobreescribe el archivo 
# with open('cuento.txt','a') as file:
#     file.write('\n\n by: ChatGPT\n')

with open('cuento.txt','r') as file:
    nume_lineas = len(file.readlines())
    print(nume_lineas)
    