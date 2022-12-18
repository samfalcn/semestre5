import ast
sum = {
    1: {
        'cantidad': 20,
        'nombre': 'platos',
        'precio': 50.0
    },
    2: {
        'cantidad': 90,
        'nombre': 'vasos',
        'precio': 70.0
    }  
}

def op1(inv):
    x = int(input("Ingresar el id del suministro a mostrar: "))
    try:
        print(f"Tienes {inv[x]['cantidad']} {inv[x]['nombre']} de precio: {inv[x]['precio']}")
    except: 
        print("Suministro no disponible")

def op7():
    o = open("inv.txt", "w")
    ast.literal_eval(str(sum))
    st = str(sum)
    o.write(st)
    return sum

def op2():
    print("Agregar suministro al inventario")
    cantidad= input("Agregar cantidad: ")
    nombre= input("Agregar nombre: ")
    precio= input("Agregar precio: ")
    x = len(sum) 
    sum[x+1] = {
        'cantidad' : cantidad,
        'precio' : precio,
        'nombre' : nombre
    }
    return sum 

    
def op3():
    print("Modificar suministro existente en el inventario")
    print("1. Modificar cantidad")
    print("2. Modificar precio")    
    x = int(input("id del suministro a modificar: "))
    m = int(input("Ingrese opción: "))
    print(f"Tienes {sum[x]['cantidad']} {sum[x]['nombre']} de precio: {sum[x]['precio']}")
    if m == 1: 
        sum[x]['cantidad'] = int(input("Cantidad nueva: "))
    elif m == 2: 
        sum[x]['precio'] = int(input("Precio nuevo: "))
    print(sum[m])
    return sum

def op4():
    total_final = 0
    for j in range(len(sum)):
        print(sum[j+1])
        precio = sum[j+1]['precio']
        cantidad = sum[j+1]['cantidad']
        total = precio * cantidad
        print(total)
        total_final = total + total_final
    print("Cantidad total: ", total_final)
    return sum

def op5():
    print("Salir")
    corre = False
    return corre

def op6():
    print("tendencias: ")
    pmayor = 0
    cmayor = 0
    pmenor = 1000000
    cmenor = 10000
    for i in range(len(sum)):
        if sum[i+1]['precio'] > pmayor:
            pmayor = sum[i+1]['precio']

    for x in range(len(sum)):
        if sum[x+1]['precio'] < pmenor:
            pmenor = sum[x+1]['precio']
            id = x+1

    print("Precio más alto: ", pmayor)
    print("Precio más bajo: ", pmenor)

    for j in range(len(sum)):
        if sum[j+1]['cantidad'] > cmayor:
            cmayor = sum[j+1]['cantidad']

    for m in range(len(sum)):
        if sum[m+1]['cantidad'] < cmenor:
            cmenor = sum[m+1]['cantidad']
    print("menor cantidad: ", cmenor)
    print("Mayor cantidad: ", cmayor)

def menu():
    print("MENU")
    print("1. Mostrar suministro")
    print("2. Agregar nuevo suministro")
    print("3. Modificar un suministro")
    print("4. Costos totales")
    print("5. Salir del menú")
    print("6. tendencia")
    print("7. Crear archivo de texto")
     
corre = True


while corre:
    menu()
    op = int(input("Seleccionar opcion del menú: "))

    if op == 1:
        op1(sum)
   
    elif op == 2:
        sum = op2()

    elif op == 5:
        corre = op5()

    elif op == 3:
        op3()

    elif op == 4:
        sum = op4()

    elif op == 6: 
        op6()

    elif op == 7:
        sum = op7()

