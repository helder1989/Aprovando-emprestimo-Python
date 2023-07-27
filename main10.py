casa = float(input("Valor da casa: R$"))

salario = float(input("Salário do comprador: R$"))

anos = int(input("Quantos anos de financiamento? "))

prestacao = casa / (anos * 12)

minimo = salario * 30 / 100 # estabelecendo o valor da parcela

print("Para pagar uma casa de R${:.2f} em {} anos".format(casa, anos), end="")
print(", a prestacão será de R${:.2f}".format(prestacao))

if prestacao <= minimo:
    print("Parabéns, empréstimo Aprovado!")

else:
    print("Empréstimo Negado!")




