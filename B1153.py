def fatorial(numero:int):
    if numero != 1:
        fat = numero * fatorial(numero - 1)
        return fat
    elif numero == 1:
        return 1

n = int(input())
print(fatorial(n))
