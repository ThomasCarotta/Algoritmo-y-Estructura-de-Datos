#1_ Desarrollar una función recursiva que permita contar cuantas veces aparece una determinada palabra, en un vector de palabras.

vector=['perro','mochila','casa','auto','comida','parcial','mochila','mochila','casa','casa','casa','perro']

palabra=input('Ingrese palabra a buscar: ')

def contador_palabra(vector,palabra):
    if len(vector)==0:
        return 0
    elif vector[-1]==palabra:
        return 1 + contador_palabra(vector[:-1],palabra)
    else:
        return contador_palabra(vector[:-1],palabra)

contar= contador_palabra(vector,palabra)
print(contar)