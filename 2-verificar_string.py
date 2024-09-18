def verifica_letra_a(string):

    contagem = string.lower().count('a')

    if contagem > 0:
        return f"A letra 'a' aparece {contagem} vezes na string."
    else:
        return "A letra 'a' não foi encontrada na string."

texto = input("Informe uma string: ")
resultado = verifica_letra_a(texto)
print(resultado)