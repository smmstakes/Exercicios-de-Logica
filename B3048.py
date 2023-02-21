# Entrada
# A primeira linha da entrada contém um inteiro N representando o tamanho da sequência. As N linhas seguintes contêm, cada uma, um inteiro Vi , para 1 ≤ i ≤ N, definindo a sequência de números desenhados no chão da calçada imperial.

# Saída
# Seu programa deve imprimir uma linha contendo um número inteiro representando a quantidade máxima de números da sequência que poderiam ser marcados com um círculo sem que haja dois números iguais consecutivos na sequência marcada.

# Restrições

# • 3 ≤ N ≤ 500

# • Vi é igual a 1 ou 2, para 1 ≤ i ≤ N

qtd_num = int(input())
sequencia = []
sequencia_marcada = 1

for num in range(qtd_num):
    sequencia.append(int(input()))

for i in range(len(sequencia) - 1):
    if sequencia[i] != sequencia[i+1]:
        sequencia_marcada += 1

print(sequencia_marcada)