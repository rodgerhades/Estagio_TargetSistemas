def calcula_soma():
    INDICE = 12
    SOMA = 0
    K = 1

    while K < INDICE:
        K = K + 1
        SOMA = SOMA + K

    return SOMA

resultado = calcula_soma()
print(f"O valor da variável SOMA é: {resultado}")