nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
print('Se a primeira nota é {:.1f} e a segunda nota é {:.1f} a media foi de {:.1f} '.format(nota1, nota2, media))
if media >= 7.0:
    print('\033[30;42mAPROVADO!\033[m')
    print('Sua nota final foi {}'.format(media))
elif media < 5.0:
    print('\033[0;30;41mREPROVADO!\033[m')
    print('Sua nota final foi {}'.format(media))
else:
    print('\033[1;35;43mRECUPERAÇÃO!\033[m')
    print('Sua nota final foi {}'.format(media))
