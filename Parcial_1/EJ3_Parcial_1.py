from pila import Pila

pila=Pila()

viajes=[{'Planeta':'A','Capturado':'a','Recompenza':1000},
        {'Planeta':'B','Capturado':'b','Recompenza':1000},
        {'Planeta':'Tierra','Capturado':'Han Solo','Recompenza':1000},
        {'Planeta':'D','Capturado':'d','Recompenza':1000},
        {'Planeta':'E','Capturado':'e','Recompenza':1000},
        {'Planeta':'F','Capturado':'Han Solo','Recompenza':1000}]

for i in viajes:
    pila.push(i)

cont=0
acum=0

while pila.size()>0:
    elem=pila.pop()
    acum+=elem['Recompenza']
    print('La misión del planeta ',elem['Planeta'],' fue la numero: ',(pila.size()+1))
    if elem['Capturado']=='Han Solo':
        cont+=1
        print('Han solo fue capturado en el planeta',elem['Planeta'])

print(f'La cantidad de creditos ganados es de {acum}')
print(f'Han solo fue capturado un total de {cont} veces')