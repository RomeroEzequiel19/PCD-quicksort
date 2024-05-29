def partition(lista, low, high):
    # Si low es mayor o igual a high, la sublista tiene 0 o 1 elementos y retorna la lista
    if(low >= high): return lista

    i = low
    j = high
    # Se elige el primer elemento de la sublista como pivote
    s = lista[low]

    while i < j:
        # Se decrementa j mientras los elementos sean mayores que el pivote
        while lista[j] > s:
            j -= 1
        lista[i] = lista[j]

        # Se incrementa i mientras los elementos sean menores o iguales al pivote
        while i < j and lista[i] <= s:
            i += 1
        lista[j] = lista[i]

    lista[i] = s

    # Llama recursivamente a quicksort para las sublistas a la izquierda y a la derecha del pivote.
    partition(lista, low, i - 1)
    partition(lista, i + 1, high)

    return(lista)


# Ordena la lista usando el algoritmo quicksort
def quicksort(lista):
    # Muestra la lista oroginal
    print("Lista original: ", lista)
    # Pasamos los parámetros a la lista a ordenar
    print("Lista ordenada con quicksort: ", partition(lista, 0, len(lista) - 1))
    print("Lista ordenada con quicksort: ", partition(lista, 0, len(lista) - 3))
    print("Lista ordenada con quicksort: ", partition(lista, 3, len(lista) - 1))

# Lista de prueba
lista = [1,5,2,8,-2,6,0,70,3]

# Pasamos la lista como argumento a la función
quicksort(lista)




