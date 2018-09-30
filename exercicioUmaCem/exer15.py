#R$60 reais por dia
#R$0,15 por quilometro rodado

ndias=float(input('Quantos dias você quer alugar o carro?'))
km=float(input('Quantos quilometros foram rodados?'))

calcdias=ndias*60
km=0.15*km

result=calcdias+km

print ('VOCÊ TERÁ DE PAGAR: R${:.2f} '.format(result))



