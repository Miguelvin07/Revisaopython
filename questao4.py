# Questão 4 : Validação de PIN do cartão
# Um cartão tem o PIN correto igual a 1234. O usuário tem no máximo 3 tentativas para digitar o PIN correto.

# Implemente o laço de tentativas:

# Se acertar antes de estourar as tentativas, imprima ACESSO LIBERADO em N tentativa(s).
# Se errar 3 vezes seguidas, imprima CARTAO BLOQUEADO.
# A cada erro, mostre quantas tentativas restam


for i in range(3):
    pin = input("Digite o pin: ")
    if pin != "1234":
        print(f"O número do pin está incorreto: Restam {3-(i+1)} tentativas")
    else:
        break
if pin == "1234":
    print(f"Acesso liberado em {i+1} tentativa(s)")
else:
    print("CARTÃO BLOQUEADO")