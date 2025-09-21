import math

def rectangulo(base, altura):
	area = base * altura
	perimetro = 2 * (base + altura)
	return area, perimetro
#print (rectangulo (17,18))

def circulo(radio):
	area = radio**2 * math.pi
	perimetro = 2 *math.pi * radio
	return area, perimetro
#print (circulo(2))

def triangulo(base, altura):
	area = (base * altura)/2
	cateto= math.sqrt(base**2+ altura**2)
	perimetro= base + altura + cateto
	return area, perimetro
#print (triangulo (17,18))
