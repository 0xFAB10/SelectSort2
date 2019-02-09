import matplotlib as mpl
from random import randint
mpl.use('Agg')
import matplotlib.pyplot as plt
import timeit

def desenhaGrafico(x,y1,y2, yl = "Saídas",xl = "Entradas"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x,y1, label = "Melhor Tempo")
    ax.plot(x,y2, label = "Melhor Tempo")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig(yl+'_graph.png')
 
def geraLista(tam):
    lista = []
    while len(lista) < tam:
        n = randint(1,1*tam)
        if n not in lista: lista.append(n)
    return lista

def select2(xb):
  count = 0
  while len(lis2) > 1:
    minimo = lis2[0]
    aux=0
    for a in range(len(lis2)):
      if (minimo > lis2[a]):
        aux = a
        minimo = lis2[a]
      count=count+1
    lis2.pop(aux)
    lisFinal.append(minimo)
  return count

def select1(xb):
  count = 0
  aux = 0
  for a in range(xb):
    minimo = lis[a]
    for b in range(a+1,xb):
      if (minimo > lis[b]):
        aux = lis[b]
        lis[b] = minimo
        minimo = aux
      count=count+1
      lis[a] = minimo
  return count

x = [100, 200, 400, 600]
y1 = []
z1 = []
y2 = []
z2 = []
for i in range(len(x)):
  lis = geraLista(x[i])
  lis2 = lis[:]
  lisFinal = []
  y1.append(select1(x[i]))
  z1.append(timeit.timeit('select1({})'.format(x[i]),setup="from __main__ import select1",number=1))
  y2.append(select2(x[i]))
  z2.append(timeit.timeit('select2({})'.format(x[i]),setup="from __main__ import select2",number=1))
print(y1)
print(y2)
print(z1)
print(z2)
desenhaGrafico(x,y1,y2, "nops")
desenhaGrafico(x,z1,z2, "Tempo")