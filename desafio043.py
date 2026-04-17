peso = float(input('Qual o seu peso?: '))
altura = float(input('Qual a sua altura?: '))
imc = peso / (altura ** 2)
print(' O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('\033[1;35;43mAbaixo do peso\033[m')
elif 18.5 <= imc < 25:
    print('\033[30;42mPeso ideal\033[m')
elif 25 <= imc < 30:
    print('\033[4;33;44mSobrepeso\033[m')
elif 30 <= imc < 40:
    print('\033[1;35;43mObesidade\033[m')
else:
    print('\033[0;30;41mObesidade Mórbida, CUIDADO\033[m!!!')