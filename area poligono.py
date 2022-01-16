from math import pi, tan
def area_de_poligono(n, s):
    area=n*s**2/(4*tan(pi/n))
    return area



numero_lados = 5
longitud_lados = 12
print(area_de_poligono(numero_lados, longitud_lados))