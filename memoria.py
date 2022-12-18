memoria = [False, True, False, True, False, True, True, True, True, True, False, False, True, False, True, True, True, True, False, True]
k = 4
z = 0
""" for i in range(len(memoria)):
    if memoria[i] == True:
        z = z + 1
        if z >= k:
            break
    else: z = 0 """

i = 0
while i < len(memoria) and z < k:
    if memoria[i] == True:
        z+=1
    else: z = 0
    i+=1


#for j in range(i-z+1, i+1):
 #   memoria[j] = 0

for j in range(i,i-z,-1):
    memoria[j] = 0

if z >= k:
    print("Espacio suficiente")
else:
     print("Espacio insuficiente")

print(f"z:{z} i:{i}")
print(memoria)