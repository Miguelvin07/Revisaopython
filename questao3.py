
# Leia uma palavra (sem espaços) e descubra qual é o primeiro caractere que aparece duas ou mais vezes nela.
# Caso não exista nenhum caractere, imprima Nenhum caractere.

# Restrições: não use listas, dicionários, nem .count().

palavra = input("Digite a palavra: ")

for letra in palavra:
    contador = 0
    for i in palavra:
        if i == letra:
            contador +=1
    if contador >=2:
        print(f"A primeira letra que se repete 2 ou mais vezes é: {letra}, se repete {contador} vezes")
        break
else:
    print("Não existe caracteres repetidos")


