lista_numeros = [1, 2, 3]

lista_numeros.append(4)

print(lista_numeros)

lista_numeros.insert(0,0)

print(lista_numeros)

removido = lista_numeros.pop() 

print(lista_numeros) 
print(removido)

lista_numeros.sort(reverse=True)

print(lista_numeros)

lista_numeros.sort()

print(lista_numeros)

posicao = lista_numeros.index(3)

print(posicao)

print(lista_numeros.count(2))

lista_numeros.remove(0)

print(lista_numeros)

for i, numero in enumerate(lista_numeros, 1):
    print(f"{i}:{numero}")

    nu = 1
    na = 2
    print(na>nu)

numeros = [76, 13, 4, 7, 90, 9, 22, 3, 13]
unidades = []
for i in numeros:
    if i < 10:
        unidades.append(i+1)

print(unidades)
unidades = [x+1 for x in numeros if x<10]
print(unidades)

pares = [x for x in range(10)]
print(pares)  # [0, 2, 4, 6, 8]

rotulo = ["par" if x % 2 == 0 else "ímpar" for x in range(5)]
print(rotulo)

