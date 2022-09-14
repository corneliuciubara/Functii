def creare_lista():
    n = int(input("Nr. de elemente:"))
    lista_locala = []
    for i in range(n):
        elem = int(input('Elem' +str(i)+ 'este:'))
        lista_locala.append(elem)
    return lista_locala
def afisare_lista(x):
    for i in x:
        print(i)