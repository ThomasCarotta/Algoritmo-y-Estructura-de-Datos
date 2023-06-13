# 2_Dada una lista con nombres de personajes de la saga de Avengers
# ordenados por nombre del superhéroes, de los cuales se conoce:
# nombre del superhéroe, nombre del personaje (puede ser vacio),
# grupo al que (perteneces puede ser vacio), año de aparición, por
# ejemplo (Star Lord – Peter Quill – Guardianes de la galaxia - 1976).
# Resolver las siguientes tareas:
#A_Determinar si “Capitana Marvel” está en la lista y mostrar su nombre de personaje;
#B_Almacenar los superhéroes que pertenezcan al grupo “Guardianes de la galaxia” en una cola e indicar cuantos son.
#C_ Mostrar de manera descendente los superhéroes que pertenecen al grupo “Los cuatro fantásticos” y “Guardoanes de la galaxia”.
#D_Listar los superhéroes que tengan nombre de personajes cuyo año de aparición sea posterior a 1960.
#E_Hemos detectado que la superhéroe “Black Widow” está mal cargada por un error de tipeo, figura como “Vlanck Widow”, modifique dicho superhéroe para solucionar este problema.
#F_Dada una lista auxiliar con los siguientes personajes (‘Black Cat’, ‘Hulk’, ‘Rocket Racoonn’, ‘Loki’, complete el resto de la información), 
# agregarlos a la lista principal en el caso de no estar cargados.
#G_ Mostrar todos los personajes que comienzan con C, P o S.
#H_ Cargue al menos 20 superheroes a la lista.

from lista import Lista
from cola import Cola

class SuperHero:
    def __init__(self,nombreSuperheroe,nombrePersonaje,grupo,anio):
        self.nombreSuperheroe=nombreSuperheroe
        self.nombrePersonaje=nombrePersonaje
        self.grupo=grupo
        self.anio=anio

    def __str__(self):
        return f'{self.nombreSuperheroe} - {self.nombrePersonaje} - {self.grupo} - {self.anio}'

personaje1= SuperHero('Capitana Marvel','Carol Danvers','Guardianes de las Galaxias',1995)
personaje2=SuperHero('StarLord','Peter Quill','Guardianes de las Galaxias',1976)
personaje3=SuperHero('Groot','Groot','Guardianes de las Galaxias',1976)
personaje4=SuperHero('Gamora','Gamora','Guardianes de las Galaxias',1976)
personaje5=SuperHero('Vlanck Widow','Natasha Romanoff','Vengadores',1964)
personaje6=SuperHero('Sr.Fantastico','Reed Richards','Los Cuatro Fantasticos',1976)
personaje7=SuperHero('Mjujer Invisible','Susan Storm','Los Cuatro Fantasticos',1976)
personaje8=SuperHero('La Cosa','Ben Grimm','Los Cuatro Fantasticos',1976)
personaje9=SuperHero('Antorcha Humana','Johnny Storm','Los Cuatro Fantasticos',1976)
personaje10=SuperHero('C','C','C',1)
personaje11=SuperHero('D','D','D',2)
personaje12=SuperHero('E','E','E',3)
personaje13=SuperHero('F','F','F',4)
personaje14=SuperHero('G','G','G',5)
personaje15=SuperHero('H','H','H',6)


lista=Lista()
cola=Cola()
lista.insert(personaje1,'nombreSuperheroe')
lista.insert(personaje2,'nombreSuperheroe')
lista.insert(personaje3,'nombreSuperheroe')
lista.insert(personaje4,'nombreSuperheroe')
lista.insert(personaje5,'nombreSuperheroe')
lista.insert(personaje6,'nombreSuperheroe')
lista.insert(personaje7,'nombreSuperheroe')
lista.insert(personaje8,'nombreSuperheroe')
lista.insert(personaje9,'nombreSuperheroe')
lista.insert(personaje10,'nombreSuperheroe')
lista.insert(personaje11,'nombreSuperheroe')
lista.insert(personaje12,'nombreSuperheroe')
lista.insert(personaje13,'nombreSuperheroe')
lista.insert(personaje14,'nombreSuperheroe')
lista.insert(personaje15,'nombreSuperheroe')

# listaAuxiliar=[{'nombreSuperheroe':'Black Cat','nombrePersonaje':'Felicia Hardy','grupo':'','anio':1979},
#                {'nombreSuperheroe':'Hulk','nombrePersonaje':'Bruce Banne','grupo':'Vengadores','anio':1962},
#                {'nombreSuperheroe':'Rocket Racoonn','nombrePersonaje':'Rocket Racoonn','grupo':'Guardianes de las Galaxias','anio':1976},
#                {'nombreSuperheroe':'Loki','nombrePersonaje':'Loki','grupo':'','anio':1949},]

#a
buscado1=lista.search('Capitana Marvel','nombreSuperheroe')
if buscado1!=None:
    print('Nombre de la Capitana Marvel: ',lista.get_element_by_index(buscado1).nombrePersonaje)
print()
#b
cont=0
for i in range (lista.size()):
    if lista.get_element_by_index(i).grupo=='Guardianes de las Galaxias':
        cont+=1
        cola.arrive(lista.get_element_by_index(i))

print(f'Hay un total de {cont} personajes de Guardianes de las Galaxias')
print()
#c
cosa=['Guardianes de las Galaxias','Los Cuatro Fantasticos']
listaSecundaria=Lista()
for i in range (lista.size()):
    if lista.get_element_by_index(i).grupo in cosa:
        listaSecundaria.insert(lista.get_element_by_index(i),'nombreSuperheroe')
listaSecundaria.order_by('nombreSuperheroe',True)
listaSecundaria.barrido()
print()
#d
for i in range (lista.size()):
    if lista.get_element_by_index(i).anio>1960:
        print('Posterior a 1960: ',lista.get_element_by_index(i))
print()
#e
buscado2=lista.search('Vlanck Widow','nombreSuperheroe')
if buscado2!=None:
    lista.delete('Vlanck Widow','nombreSuperheroe')
    personaje16=SuperHero('Black Widow','Natasha Romanoff','Vengadores',1964)
    lista.insert(personaje16,'nombreSuperheroe')
print()
#g
comienzo=['C','P','S']
for i in range(lista.size()):
    if (lista.get_element_by_index(i).nombreSuperheroe[0] in comienzo) or (lista.get_element_by_index(i).nombrePersonaje[0] in comienzo):
        print(lista.get_element_by_index(i))

