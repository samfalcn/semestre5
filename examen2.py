import csv
import statistics
import string

print("Es un sistema de Inteligencia Empresarial BI.\nPorque su propósito es obtener tendencias y relaciones de datos") 

#lectura de datos
e= []
def lect():
    with open('dataset_examen2.csv','r') as csvfiler:
        for line in csv.DictReader(csvfiler):
            e.append(line)
lect()

#media, desviación estandar, máximos, mínimos
def estadisticas():
    a = len(e)
    n = 1
    UnitPrice = []
    while (n < a):
        UnitPrice.append(float(e[n]['UnitPrice']))
        n = n + 1
    b = len(UnitPrice)
    c = sum(UnitPrice)
    d = statistics.pstdev(UnitPrice)
    m = max(UnitPrice)
    mi = min(UnitPrice)
    print(f'Media de Unit Price: {(c/b)}')
    print(f'Desviación estandar de Unit Price: {d}')
    print(f'Máximo de Unit Price: {m}')
    print(f'Mínimo de Unit Price: {mi}')
estadisticas()

#precio total de los 10 primeros productos
def precio():
    a = 10
    n = 1
    UnitPrice = []
    while (n < a):
        UnitPrice.append(float(e[n]['UnitPrice']))
        n = n + 1
    c = sum(UnitPrice)
    print(f'Precio total de los 10 primeros productos: {(c)}')
precio()

#pedidos por países
def paises():
    a = len(e)
    n = 1
    pais = []
    while (n < a):
        pais.append(e[n]['Country'])
        n = n + 1
    print("Pedidos por países: ")
    c = dict()
    for n in pais:
        if n in c.keys():
            c[n] = c[n] + 1
        else:
            c[n] = 1
    for z in c:
        print(z ,":", str(c[z]))
paises()

#cliente con más compras
def cliente():
    a = len(e)
    n = 1
    clientes = []
    while (n < a-1):
        clientes.append(e[n]['CustomerID'])
        n = n + 1
    c = dict()
    for n in clientes:
        if n in c.keys():
            c[n] = c[n] + 1
        else:
            c[n] = 1
    #print(c)
    f = []
    for key, value in c.items():
        f.append(value)
    f.sort()
    for key, value in c.items():
# -2 porque el de -1 no tiene ID
        if value == f[-2]:
            w = key
    print("CUSTOMER ID: ", w)

    f = []
    #print(c)
    #print(e[0]['InvoiceNo'])
    """ for key, value in c.items():
        if w == value['CustomerID']:
            f.append(value['Invoic"eDate'])
    print("Primera compra: ", f[0])"""

cliente()

def cliente2():
    print("Pedidos por clientes: ")
    a = len(e)
    n = 0
    cl = []
    while (n <= a-1):
        cl.append(e[n]['CustomerID'])
        n = n + 1
    print("Pedidos por cliente: ")
    c = dict()
    for n in cl:
        if n in c.keys():
            c[n] = c[n] + 1
        else:
            c[n] = 1
    for z in c:
        print(z ,":", str(c[z]))
#cliente2()