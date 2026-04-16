idade = int(input('Digite sua idade: '))
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Então ele é \033[4;30;44mMIRIM!\033[m')
elif idade <= 14:
    print(' Então ele é \033[4;30;44mCRIANÇA/INFANTIL!\033[m')
elif idade <= 19:
    print('Então ele é \033[4;30;44mJUNIOR!\033[m')
elif idade <= 20:
    print('Então ele é \033[4;30;44mSENIOR!\033[m')
else:
    print('Então ele é \033[4;30;44mMASTER!\033[m')