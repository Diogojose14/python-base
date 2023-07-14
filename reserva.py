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

RESERVAS_FILE = "reservas.txt"
QUARTOS_FILE = "quartos.txt"

# Acesso ao banco de dados

# TODO: Usar pacote csv

ocupados = {} #acumulador
try:
    for line in open(RESERVAS_FILE):
        nome_cliente, num_quarto, dias = line.strip().split(",")
        ocupados[int(num_quarto)] = {
            "nome": nome_cliente,
            "dias": dias
        }
except FileNotFoundError:
    logging.error("Arquivo %s não existe", RESERVAS_FILE)
    sys.exit(1)

# TODO: Usar função para ler os arquivos

quartos = {}
try:
    for line in open(QUARTOS_FILE):
        num_quarto, nome_quarto, preco = line.strip().split(",")
        quartos[int(num_quarto)] = {
            "nome_quarto": nome_quarto,
            "preco": float(preco), #TODO:Usar Decimal
            "disponivel": False if int(num_quarto) in ocupados else True
        }
except FileNotFoundError:
    logging.error("Arquivo %s não existe", QUARTOS_FILE)
    sys.exit(1)


# programa principal
print("Reserva Hotel Pythonico")
print("-" * 52)
if len(ocupados) == len(quartos):
    print("Hotel Lotado")
    sys.exit(0)

nome_cliente = input("Nome do client: ").strip()
print()
print("Lista de Quartos: ")
print()
head = ["Número", "Nome do Quarto", "Preço", "Situação"]
print (f"{head[0]:<6} - {head[1]:<14} - R$ {head[2]:<9} - {head[3]:<10}")
for num_quarto, dados_quarto in quartos.items():
    nome_quarto = dados_quarto["nome_quarto"]
    preco = dados_quarto["preco"]
    disponivel = "Indisponivel!" if not dados_quarto['disponivel'] else "Disponivel!"
    # disponivel = dados ['disponivel'] and "disponivel" or "indisponivel"
    # TODO: Subistituir casa decimal por virgula
    print (f"{num_quarto:<6} - {nome_quarto:<14} - R$ {preco:<9.2f} - {disponivel}")


print("-" * 52)
# reserva

try:
    num_quarto = int(input("Número do quarto:").strip())
    if not quartos[num_quarto]["disponivel"]:
        print(f"O quarto {num_quarto} está ocupado, escolha outro")
        sys.exit(0)
except ValueError:
    logging.error("Número inválido, digite números validos.")
    sys.exit(1)
except KeyError:
    print(f"O quarto {num_quarto} não existe.")
    sys.exit(1)

try:
    dias= int(input("Quantos dias? ").strip())
except ValueError:
    logging.error("Número invalido, digite apenas digitos.")
    sys.exit(1)

nome_quarto = quartos[num_quarto]["nome_quarto"]
preco_quarto = quartos[num_quarto]["preco"]
disponivel = quartos[num_quarto]["disponivel"]
total = preco_quarto * dias

# print(",".join([nome, str(num_quarto), str(dias)]))

print(
    f"Olá {nome_cliente} você escolheu o quarto {nome_quarto} "
    f"e vai custar: R${total:.2f}"
)

if input ("Confirma? (digite y)").strip().lower() in ("y", "yes", "sim", "s"):
    with open(RESERVAS_FILE, "a") as reserva_file:
        reserva_file.write(f"{nome_cliente},{num_quarto},{dias}\n")
        print("Reserva efetuada com sucesso!")
