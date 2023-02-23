# Faça um programa que leia as notas referentes às duas avaliações de um aluno. Calcule e imprima a média semestral. Faça com que o algoritmo só aceite notas válidas (uma nota válida deve pertencer ao intervalo [0,10]). Cada nota deve ser validada separadamente.

# Entrada
# A entrada contém vários valores reais, positivos ou negativos. O programa deve ser encerrado quando forem lidas duas notas válidas.

# Saída
# Se uma nota inválida  for lida, deve ser impressa a mensagem "nota invalida".
# Quando duas notas válidas forem lidas, deve ser impressa a mensagem "media = " seguido do valor do cálculo. O valor deve ser apresentado com duas casas após o ponto decimal.

verficador = False
notas_sem = []

while verficador != True:
    nota = float(input())
    if 0 <= nota <=10:
        notas_sem.append(nota)
    else:
        print('nota invalida')
    
    if len(notas_sem) == 2:
        print('media = {:.2f}'.format((notas_sem[0] + notas_sem[1]) / 2))
        verficador = True
