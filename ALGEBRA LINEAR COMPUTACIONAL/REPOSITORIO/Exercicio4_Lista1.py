import numpy as np

def substituicao_regressiva(U, b):
    """
    Implementa o algoritmo de substituição regressiva para resolver Ux = b.
    Parâmetros:
    - U: matriz triangular superior (numpy.ndarray)
    - b: vetor coluna correspondente (numpy.ndarray)
    Retorna:
    - x: vetor solução (numpy.ndarray)
    """
    n = len(b)
    x = np.zeros(n)
    
    # Percorre as linhas de baixo para cima (de n-1 até 0)
    for i in range(n - 1, -1, -1):
        # Verifica se há elemento nulo na diagonal principal
        if U[i, i] == 0:
            raise ValueError(f"Erro: Elemento nulo encontrado na diagonal principal na posição [{i}, {i}]. A matriz é singular.")
            
        soma = 0
        for j in range(i + 1, n):
            soma += U[i, j] * x[j]
            
        x[i] = (b[i] - soma) / U[i, i]
        
    return x

# Exemplo de teste rápido para validar no Visual Studio:
if __name__ == "__main__":
    # Matriz triangular superior U
    U_teste = np.array([
        [2.0, 1.0, 1.0],
        [0.0, 4.0, 2.0],
        [0.0, 0.0, 3.0]
    ])
    
    # Vetor b
    b_teste = np.array([4.0, 8.0, 6.0])
    
    resultado = substituicao_regressiva(U_teste, b_teste)
    print("Vetor solução x:", resultado)