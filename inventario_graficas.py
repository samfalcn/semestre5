import ast
import matplotlib.pyplot as plt

def op1(inv):
    x = int(input("Ingresar el id del suministro a mostrar: "))
    try:
        print(f"Tienes {inv[x]['cantidad']} {inv[x]['nombre']} de precio: {inv[x]['precio']}")
    except: 
        print("Suministro no disponible")

with open('inv.txt') as f:
    data = f.read()  
sum = ast.literal_eval(data)  
print(type(sum))
print(sum)

def op8():
    #declarar datos en x, y
    for i in range(len(sum)):
        x = sum[i+1]['cantidad']
        z = sum[i+1]['precio']
        print(x)
        print(z)
        plt.plot(x, z)

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
        'nombre' : nombre,
        'precio' : precio,
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


def op5():
    print("Salir")
    corre = False
    return corre


y = open('inv.txt', 'r')
sum = y.read()

def menu():
    print("MENU")
    print("1. Mostrar suministro")
    print("2. Agregar nuevo suministro")
    print("3. Modificar un suministro")
    print("5. Salir del menú")
    print("7. Guardar/Actualizar archivo de texto")
    print("8. Graficar")
     
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


    elif op == 7:
        sum = op7()

    elif op == 8:
        op8()