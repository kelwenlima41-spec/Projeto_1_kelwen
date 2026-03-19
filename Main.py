from Sudoku import printTabuleiro, gerarTabuleiro, verificarNumero, eh_valido
print('NIveís')
print('nivel 1=33')
print('nivel 2=36')
print('nivel 3=54')
nivel = int(input("Digite o nível: "))

matriz = gerarTabuleiro(nivel)

while (verificarNumero(matriz, 0)):
    
    printTabuleiro(matriz)
    
    entrada = int(input("Digite um número: "))
    l, c = input("Digite a Linha e Coluna: ").split()
    
    linha = int(l)
    coluna = int(c)
    
    linha -= 1
    coluna -= 1
    
    if (entrada == 0):
        matriz[linha][coluna] = 0
        print("Número removido!")
        continue
    
    elif(eh_valido(matriz, linha, coluna, entrada)):
        matriz[linha][coluna] = entrada
        print("Entrada válida")
        
    else:
        print("Entrada inválida")
        
printTabuleiro(matriz)
print("SUCESSO")
    