import os

# directorio actual
cwd = os.getcwd()
print('Directorio actual:', cwd)

# lista de archivos y directorios
files = os.listdir(cwd)
print(files)

#listar archivos y directorios con detalle
files = os.scandir(cwd)
for file in files:
    print(file.name, file.is_dir(), file.is_file())

# listar archivos TXT 
txt_files = [file for file in os.listdir(cwd) if file.endswith('.txt')]
print(txt_files)

# crear directorio
os.makedirs('nuevo_directorio', exist_ok=True)  # exist_ok=True para evitar error si ya existe

# renombrar directorio o archivo
os.rename('nuevo_directorio', 'directorio_renombrado')

# eliminar directorio o archivo
os.rmdir('directorio_renombrado')   # solo si está vacío
os.remove('archivo.txt')            # solo si es un archivo de texto    