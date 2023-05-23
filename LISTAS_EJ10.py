from Operaciones_Lista import Lista
from Operaciones_Lista import criterio_comparacion

#Se dispone de una lista de canciones de Spotify, de las cuales se sabe su nombre, banda o artista, 
# duración y cantidad de reproducciones durante el último mes. Desarrollar un algoritmo que
# permita realizar las siguientes actividades:
#a. obtener la información de la canción más larga;
#b. obtener el TOP 5, TOP 10 y TOP 40 de canciones más escuchadas;
#c. obtener todas las canciones de la banda Arctic Monkeys;
#d. mostrar los nombres de las bandas o artistas que solo son de una palabra.

class Spotify():
    def __init__(self, nombre, autor, duracion, reproducciones):
        self.nombre=nombre
        self.autor=autor
        self.duracion=duracion
        self.reproducciones=reproducciones

    def __str__(self):
        return f'{self.nombre} - {self.autor} - {self.duracion}'

lista=Lista()

cancion1 = Spotify('Cancion 1','Maneskin', 3.9, 10000 )
cancion2 = Spotify('Cancion 2','Queen', 3.2, 250000 )
cancion3 = Spotify('Cancion 3','Arctic Monkeys', 4.5, 3500000 )
cancion4 = Spotify('Cancion 4','Imagin Dragon', 3.1, 2400000 )
cancion5 = Spotify('Cancion 5','Arctic Monkeys', 2.9, 23500000 )
cancion6 = Spotify('Cancion 6','Banda', 5, 1000000 )

lista.insert(cancion1, 'reproducciones')
lista.insert(cancion2, 'reproducciones')
lista.insert(cancion3, 'reproducciones')
lista.insert(cancion4, 'reproducciones')
lista.insert(cancion5, 'reproducciones')
lista.insert(cancion6, 'reproducciones')

#a
print ()
largo = 0
posicion = 0
for i in range(0,lista.size()):
    if (lista.get_element_by_index(i).duracion >= largo):
        largo = lista.get_element_by_index(i).duracion
        posicion = i
print ('La canción más larga es: ', lista.get_element_by_index(posicion))
print ()

#b
for i in range(lista.size() - 1, -1, -1):
    print (lista.get_element_by_index(i))
print ()

#c
for i in range(lista.size()):
    if lista.get_element_by_index(i).autor=='Arctic Monkeys':
        print(lista.get_element_by_index(i).nombre)
print()


print('//////////')
#e
for i in range (lista.size()):
    if ' ' not in lista.get_element_by_index(i).autor:
        print(lista.get_element_by_index(i).autor)