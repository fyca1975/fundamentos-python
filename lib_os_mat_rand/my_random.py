import random

#genera un numero aleatorio entre 1 y 10 
num = random.randint(1, 10)
print(num)

#elegir colores aleatorios  
colores = ['rojo', 'verde', 'azul', 'amarillo']
color = random.choice(colores)
print(color)

#barajar una lista de cartas    
cartas = ['corazon', 'diamante', 'trebol', 'pica']
random.shuffle(cartas)  #barajar
print(cartas)