import math
import numpy as np

def calcular_cinematica_robo(theta1_graus, theta2_graus):
    # 1. Converte os ângulos recebidos para radianos
    t1 = math.radians(theta1_graus)
    t2 = math.radians(theta2_graus)
    soma_t = t1 + t2
    
    # 2. Tamanhos dos elos fixados pelo enunciado
    L1 = 20.0
    L2 = 15.0
    
    # 3. Calcula as posições X e Y brutas
    x_u = L1 * math.cos(t1) + L2 * math.cos(soma_t)
    y_u = L1 * math.sin(t1) + L2 * math.sin(soma_t)
    
    # 4. Monta a Matriz de Transformação Homogênea 3x3
    matriz_T = np.array([
        [math.cos(soma_t), -math.sin(soma_t), x_u],
        [math.sin(soma_t),  math.cos(soma_t), y_u],
        [0.0,               0.0,              1.0]
    ])
    
    # 5. Prepara os resultados com 1 casa decimal
    x_final = round(x_u, 1)
    y_final = round(y_u, 1)
    matriz_final = np.round(matriz_T, 1)
    
    return x_final, y_final, matriz_final


# --- BLOCO INTERATIVO DO CONSOLE ---
if __name__ == "__main__":
    print("=" * 50)
    print(" CÁLCULO DO ROBÔ PLANAR (LETRAS A e B)")
    print("=" * 50)
    
    # Recebe os dados do usuário
    entrada_theta1 = float(input("Digite o ângulo da junta 1 (theta 1) em graus: "))
    entrada_theta2 = float(input("Digite o ângulo da junta 2 (theta 2) em graus: "))
    
    # Executa a função unificada
    x, y, matriz = calcular_cinematica_robo(entrada_theta1, entrada_theta2)
    
    # --- DIVISÃO DA LETRA A ---
    print("\n" + "-" * 50)
    print(" LETRA A: POSIÇÃO DO EFETUADOR (X, Y)")
    print("-" * 50)
    print("Coordenadas físicas onde a 'mão' do robô parou:")
    print(f"Eixo X_u: {x} cm")
    print(f"Eixo Y_u: {y} cm")
    
    # --- DIVISÃO DA LETRA B ---
    print("\n" + "-" * 50)
    print(" LETRA B: MATRIZ DE TRANSFORMAÇÃO COMPLETA (3x3)")
    print("-" * 50)
    print("Tradutor de coordenadas (Rotação do efetuador + Posição):")
    print(matriz)
    print("=" * 50)