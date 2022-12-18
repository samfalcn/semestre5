import json
import csv
import os
import matplotlib.pyplot as plt


rows = ['Store ID','Store_Area', 'Items_Available', 'Daily_Customer_Count', 'Store_Sales']
suministroscsv = []
suministros = {}

def menu(op):

    print("\n")
    print("1. Cargar suministros")
    print("2. TOP 10 de las tiendas mas visitadas")
    print("3. TOP 5 mejores ingresos")
    print("4. Promedio de ventas")
    print("5. Gasto promedio x cliente")
    print("6. Graficar \n\n")
    print("10. SALIR...")
    o = int(input("Opcion: "))

    return o



def op1():
    lineslist = []
    with open('Stores.csv','r') as csvfiler:
        lectura = csv.reader(csvfiler)
        for lines in lectura:
            lineslist.append(lines)
        cont = len(lineslist)
        i = 1
        while(i <= (cont-1)): 
            suministros[int(lineslist[i][0])] = {
            'Store_Area':int(lineslist[i][1]),
            'Items_Available':int(lineslist[i][2]),
            'Daily_Customer_Count' : int(lineslist[i][3]), 
            'Store_Sales':int(lineslist[i][4])}

            i= i + 1
 

def topvisited():
    a = len(suministros)
    n = 1
    daily_cost = []
    tops = []
    while (n <= a):
        daily_cost.append(suministros[n]['Daily_Customer_Count'])
        n = n + 1
    for i in daily_cost:
        top = max(daily_cost)  
        tops.append(top)
        daily_cost.remove(top)
    x = 9
    co = 0
    while (co <= x):
        print(f'Top {co+1}:  {tops[co]} ')
        co+=1
    
def topincomes():
    a = len(suministros)
    n = 1
    incomes = []
    topi = []
    top = 0
    while (n <= a):
        incomes.append(suministros[n]['Store_Sales'])
        n = n + 1
    for i in incomes:
        top = max(incomes)  
        topi.append(top)
        incomes.remove(top)
    x = 4
    co = 0
    while (co <= x):
        print(f'Top {co+1}:  {topi[co]} ')
        co+=1

def promedioventas():
    a = len(suministros)
    n = 1
    storesales = []
    while (n <= a):
        storesales.append(suministros[n]['Store_Sales'])
        n = n + 1
    b = len(storesales)
    c = sum(storesales)
    print(f' Promedio total: {(c / b)}')

def gastopromedioxcliente():
    a = len(suministros)
    n = 1
    storesales = []
    nclients = []
    while (n <= a):
        storesales.append(suministros[n]['Store_Sales'])
        nclients.append(suministros[n]['Daily_Customer_Count'])
        n = n + 1
    b = len(storesales)
    c = sum(storesales)
    d = sum(nclients)

    print(f'Promedio total de gasto por cliente del total de tiendas: {(c/d)}')

def graficas():
    suministrosnames = []
    cantidadsum = []
    i = 1
    n = len(suministros)
    opc = int(input("Escriba lo que desea graficar: \n 1. cantidad\n 2.precio \n\n Opcion: "))
    while (i <= n):
        if (opc == 1):
            a = suministros[i]['nombre']
            suministrosnames.append(a)
            b = suministros[i]['cantidad']
            cantidadsum.append(b)
            i = i +1
        elif (opc == 2):
            a = suministros[i]['nombre']
            suministrosnames.append(a)
            b = suministros[i]['precio']
            cantidadsum.append(b)
            i = i +1

    print("Enter para continuar")
    plt.bar(suministrosnames, cantidadsum)
    plt.show()

op = 0
while (op != 10):
    op = menu(op)
    if (op == 1):
        op1()
    elif (op == 2):
        topvisited()
    elif (op == 3):
        topincomes()
    elif (op == 4):
        promedioventas()
    elif (op == 5):
        gastopromedioxcliente()
    elif (op == 6):
        graficas()
 