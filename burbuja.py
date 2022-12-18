x = [22, 4, 13, 2, 6, 7, 3, 20, 11, 17, 1]

def bubble_sort(a):
    n = len(a)
    i = 1
    j = 0
    for i in range(n):
        for j in range(n-1):
            if a[j] > a[j+1]:
                aux = a[j]
                a[j] = a[j+1]
                a[j+1] = aux
    print(a)

bubble_sort(x)

