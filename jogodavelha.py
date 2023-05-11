matriz = [[' '] * 3 for i in range(3)]

for lin in range(3):
    for col in range(3):
        print(matriz[lin][col], end="|")
    print("\n-------")
print("Digite a linha")
jogadalin = int(input())
print("Digite a coluna")
jogadacol = int(input())
matriz[jogadalin-1][jogadacol-1] = "x"
