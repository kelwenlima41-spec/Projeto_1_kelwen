import random

def printTabuleiro(matriz):
    print("-------------------------------------")
    for i in range(len(matriz)):
        print("|", end="")
        for j in range(len(matriz[i])):
            print(f" {matriz[i][j]} |", end="")
        print("\n-------------------------------------")
            
def gerarTabuleiro( nivel):
    
    c = 0
    
    match nivel:
        case 1:
            c = 33
        
        case 2:
            c = 46
            
        case 3:
            c = 54
            
    matriz = gerar_tabuleiro()
    
    remover_numeros(matriz, c)
    
    return matriz
    
def verificarNumero(matriz, numero):
    return any(numero in linha for linha in matriz)

def preencherGrade(matriz, linha, coluna):
    numeros = list(range(1, 10))
    random.shuffle(numeros)
    for i in range(3):
        for j in range(3):
            matriz[linha+i][coluna+j] = numeros.pop()

def remover_numeros(tabuleiro, quant_remover):
    posicoes = [(i, j) for i in range(9) for j in range(9)]
    random.shuffle(posicoes)
    
    removidos = 0
    while removidos < quant_remover and posicoes:
        i, j = posicoes.pop()
        if tabuleiro[i][j] != 0:
            tabuleiro[i][j] = 0
            removidos += 1
            
    return tabuleiro

def gerar_tabuleiro():
    tabuleiro = [[0 for _ in range(9)] for _ in range(9)]
    # Preenche diagonal 3x3
    for k in range(0, 9, 3):
        preencherGrade(tabuleiro, k, k)
    # Resolve o restante
    resolver(tabuleiro)
    return tabuleiro

def resolver(tabuleiro):
    for i in range(9):
        for j in range(9):
            if tabuleiro[i][j] == 0:
                for num in range(1, 10):
                    if eh_valido(tabuleiro, i, j, num):
                        tabuleiro[i][j] = num
                        if resolver(tabuleiro):
                            return True
                        tabuleiro[i][j] = 0
                return False
    return True

def eh_valido(tabuleiro, linha, coluna, num):
    # Verifica linha e coluna
    for i in range(9):
        if tabuleiro[linha][i] == num or tabuleiro[i][coluna] == num:
            return False
    
    # Verifica bloco 3x3
    inicio_linha = (linha // 3) * 3
    inicio_coluna = (coluna // 3) * 3
    for i in range(3):
        for j in range(3):
            if tabuleiro[inicio_linha + i][inicio_coluna + j] == num:
                return False
    return True
