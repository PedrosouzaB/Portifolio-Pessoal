def dolar_para_real(valor):
    return valor * 5.20

def real_para_dolar(valor):
    return valor / 5.20

print("1 - Converter Dólar para Real")
print("2 - Converter Real para Dolar")

opcao = input("escolha uma opção (1 ou 2): ")

if opcao == "1":
    valor = float(input("Digite o valor em dolar"))
    print("Valor em Real: ", dolar_para_real(valor))
elif opcao == "2":
    valor = float(input("Digite o valor em real: "))
    print("valor em dolar:", real_para_dolar(valor))
else:
    print("Opção invalida")

                  