"""
Façca um programa de terminal que exibe ao usuário uma lista dos quartos disponiveis 
para alugar e o preço de cada quarto, esta informação está disponivel em um arquivo
de tesxto separdo por virgulas.

`quartos.txt`
# codigo, nome, preço
1,Suite Master,500
2,Quarto Familia,200
3,Quarto Single,100
4,Quarto Simples,50

O programa pergunta ao usuário o nome, qual o número do quarto a ser reservado
e a quantidade de dias e no final exibe o valor estimado s ser pago.

O programa deve salvar esta escolha em outro arquivo contedo as reservas

`reservas.txt`
# cliente, quarto, dias
Bruno,3,12

Se outro usuário tentar reservar o mesmo quarto o programa deve exibir uma
mensagem informando que já está reservado.
"""
import sys
import logging


ocupados = {}
try:
    for line in open("reservas.txt"):
        nome, num_quarto, dias = line.strip().split(",")
        ocupados[int(num_quartos)] = {
            "nome": nome,
            "dias": dias
        }
except FileNotFoundError:
    logging.error("Arquivo reserva.txt nao existe")
    sys.exit(1)


quartos = {}
try:
    for line in open("quartos.txt"):
        codigo, nome, preco = line.strip().split(",")
        quartos[int(codigo)] = {
            "nome": nome,
            "preco": float(preco), #TODO: Decimal
            "disponivel": False if int(codigo) in ocupados else True
        }
except FileNotFoundError:
    logging.error("Arquivo quartos.txt não existe")
    sys.exit(1)



print("Reserva Hotel Pythonico")
print("-" * 40)
if len(ocupados) == len(quartos):
    print("Hotel Lotado")
    sys.exit(1)

nome = input("Nome do client: ").strip()


print("Lista de Quartos: ")
for codigo, dados in quartos.items():
    nome_quarto = dados["nome"]
    preco = dados["preco"]
    disponivel = "Indisponivel!" if not dados['disponivel'] else "Disponivel!"
    # disponivel = dados ['disponivel'] and "disponivel" or "indisponivel"
    # TODO: Subistituir casa decimal por virgula
    print (f"{codigo} - {nome_quarto} - R$ {preco:.2f} - {disponivel}")


print("-" * 40)
try:
    num_quarto = int(input("Número do quarto:").strip())
    if not quartos[num_quarto]["disponivel"]:
        print(f"O quarto {num_quarto} está ocupado.")
        sys.exit(1)
except ValueError:
    logging.error("Número inválido, digite apenas digitos.")
    sys.exit(1)
except KeyError:
    print(f"O quarto {num_quarto} não existe.")
    sys.exit(1)

try:
    dias= int(input("Quantos dias?: ").strip())
except ValueError:
    logging.error("Número invalido, digite apenas digitos.")
    sys.exit(1)

nome_quarto = quartos[num_quarto]["nome"]
preco_quarto = quartos[num_quarto]["preco"]
disponivel = quartos[num_quarto]["disponivel"]
total = preco_quarto * dias

# print(",".join([nome, str(num_quarto), str(dias)]))

with open("reservas.txt", "a") as file_:
    file_.write(f"{nome},{num_quarto},{dias}\n")

print(f"{nome} você escolheu o quarto {nome_quarto} e vai custar: R${total:.2f}")
