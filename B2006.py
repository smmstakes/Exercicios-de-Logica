cha = int(input())
aux = input().split()
palpites = [int(i) for i in aux]
acertos = 0

for n in palpites:
    if n == cha:
        acertos += 1

print(acertos)