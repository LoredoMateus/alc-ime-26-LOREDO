import numpy as np

#Questão 5 - Prova de ALC - MATEUS BARROS LOREDO - ED25204

def resolve_lu(A, b):
    # Ver o tamanho da Matriz
    n = len(A)
    
    L = np.eye(n) # id
    U = np.zeros((n, n)) # matriz de zeros
    
    # Copia os valores de A para U (para não sobrepor a matriz original/testando outras coisas)
    for i in range(n):
        for j in range(n):
            U[i][j] = float(A[i][j])
            
    
    # 1 passo é a FATORIZAÇÃO LU >> Gauss sem fazer pivoteamento
   
    for i in range(n): # 'i' para olhar para linha atual
        
        # Exceção caso o pivô seja zero 
        if U[i][i] == 0.0:
            
            raise Exception(f"Pivô nulo encontrado na posição a_{i+1},{i+1}. Sugere-se utilizar uma função alternativa que aplique pivoteamento parcial (como a scipy.linalg.lu) para a solução deste sistema.")
            
        # Zerar os elementos abaixo do pivô
        for j in range(i + 1, n):
            
            # O multiplicador usado na eliminação (O meu alvo dividido pelo pivô)
            multiplicador = U[j][i] / U[i][i]
            
            # Guardo esse multiplicador na matriz L
            L[j][i] = multiplicador    
            
            # Atualiza a linha inteira da matriz U
            for k in range(i, n):
                U[j][k] = U[j][k] - (multiplicador * U[i][k])
                
                #NÃO preciso me preocupar com os sinais para a matriz L
    
    # 2 passo é fazer a SUBSTITUIÇÃO PROGRESSIVA (Resolver L * y = b)
    
    y = np.zeros(n)
    
    for i in range(n):
        soma = 0.0
        # Multiplica os elementos achados anteriormente de y pelos coeficientes de L
        for j in range(i):
            soma = soma + (L[i][j] * y[j])
            
        # Isola a incógnita 
        y[i] = b[i] - soma
        

    
    # 3 passo é a SUBSTITUIÇÃO REGRESSIVA (Resolver U * x = y)
    x = np.zeros(n)
    
    # Começa de baixo para cima 
    for i in range(n - 1, -1, -1):
        soma = 0.0
        # Multiplica os elementos já descobertos de x pelos coeficientes de U
        for j in range(i + 1, n):
            soma = soma + (U[i][j] * x[j])
            
        # Isola a incógnita dividindo pelo pivô (que vai ser o elemento da diagonal de U)
        x[i] = (y[i] - soma) / U[i][i]
        
    return L, U, x   # retorna os valores achados


# TESTES (Para validar o funcionamento)
if __name__ == "__main__":
    
    # ADICIONADO AQUI: Força o numpy a imprimir sempre com 1 casa decimal
    np.set_printoptions(formatter={'float': '{:.1f}'.format})
    
    print(">>>>>>>> TESTE 1: SISTEMA COM SOLUÇÃO VÁLIDA <<<<<<<<<")

    # Exemplo simples sem trocar linhas 
    A_sucesso = np.array([
        [2.0,  1.0, 1.0],
        [4.0, -6.0, 0.0],
        [-2.0, 7.0, 2.0]
    ])
    b_sucesso = np.array([5.0, -2.0, 9.0])
    
    try:
        L, U, x = resolve_lu(A_sucesso, b_sucesso)
        print("Matriz L:")
        print(L)
        print("\nMatriz U:")
        print(U)
        print("\nVetor Solução (x):")
        print(x)
        print("\n-> STATUS: Teste 1 FEITO")
    except Exception as erro:
        print(f"Erro no Teste 1: {erro}")


    print("\n>>>>>>>> TESTE 2: SISTEMA QUE GERA EXCEÇÃO (PIVÔ NULO) <<<<<<<<<")
    # Coloquei 0 na posição [0][0] para forçar a falha do pivô logo de início
    A_falha = np.array([
        [0.0,  2.0, 3.0],
        [1.0,  5.0, 1.0],
        [-1.0, 1.0, 4.0]
    ])
    b_falha = np.array([1.0, 2.0, 3.0])
    
    try:
        L, U, x = resolve_lu(A_falha, b_falha)
        print("O código falhou em lançar a exceção!")
    except Exception as erro:
        print("-> STATUS: Exceção capturada com sucesso")
        print(f"-> MENSAGEM DO SISTEMA: {erro}")
