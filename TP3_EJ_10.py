from Operaciones_cola import Cola
from Operaciones_Pilas import Pila
#10_ Dada una cola con las notificaciones de las aplicaciones de redes sociales de un Smartphone,
# de las cual se cuenta con la hora de la notificación, la aplicación que la emitió y el mensaje,resolver las siguientes actividades:
#A_escribir una función que elimine de la cola todas las notificaciones de Facebook;
#B_escribir una función que muestre todas las notificaciones de Twitter, cuyo mensaje incluya la palabra ‘Python’, si perder datos en la cola;
#C_utilizar una pila para almacenar temporáneamente las notificaciones producidas entre las 11:43 y las 15:57, y determinar cuántas son.

cola=Cola()
pila=Pila()
cola_nueva=Cola() #Contiene todas las notificaciones exeptuando las de Facebook
cola_twitter=Cola() #Contiene todas la notificaciones de twitter cuyo mensaje tenga la palabra Python

notificaciones=[{"hora":12.24,"app":"Facebook","mensaje":"hola"},
                {"hora":18.55,"app":"Twitter","mensaje":"aprendiste a programar en Python"},
                {"hora":15.43,"app":"Instagram","mensaje":"que haces?"},
                {"hora":14.30,"app":"Twitter","mensaje":"vamos a estudiar Python"},
                {"hora":10.45,"app":"WhatsApp","mensaje":"salimos a tomar unos mates?"},
                {"hora":13.00,"app":"Facebook","mensaje":"¿Hacemos algo hoy?"}]

for notificacion in notificaciones:
    cola.arrive(notificacion)

while cola.size()>0:
    noti=cola.atention()
    if (noti["app"]!="Facebook"):
        cola_nueva.arrive(noti)
    if (noti["app"]=="Twitter") and ("Python" in noti["mensaje"]):
        cola_twitter.arrive(noti)
        print(noti)
    if (noti["hora"]>11.43) and (noti["hora"]<15.57):
        pila.push(noti)
    
print(f'en la pila se almacenaron temporalmente {pila.size()} notifiaciones producidas entre las 11:43 y las 15:57')
    
        
        



