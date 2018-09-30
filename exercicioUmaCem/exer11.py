#a cada um metro dois litros de tinta

num1=float(input('Qual a largura da sua parede?'))
num2=float(input('Qual a altura da sua parede?'))

area=num1*num2
tinta=area*2

print ('A area da sua parede é de : {:.2f}m²'.format(area))
print ('Você gastará : {:.2f} litros de tinta para pinta esta parede'.format(tinta))

