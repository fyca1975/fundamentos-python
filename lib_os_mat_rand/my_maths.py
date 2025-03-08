import math

#hallar area y perimetro de un circulo
def area_circulo(radio):
    return math.pi * radio**2   #area   

def perimetro_circulo(radio):
    return 2 * math.pi * radio  #hallar  perimetro de un circulo

 

print('Area del circulo (5):',area_circulo(5))
print('Perimetro de circulo (5):',perimetro_circulo(5)) 