n1 = int(input('Digite o primeiro lado: '))
n2 = int(input('Digite o segundo lado: '))
n3 = int(input('Digite o terceiro lado: '))
# Verificando se forma triângulo
#if porque são duas decisões diferentes
#“Isso pode formar um triângulo?”
#✔️ sim → continua
#❌ não → para aqui
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Forma um triângulo!')
    # Tipo do triângulo
    if n1 == n2 == n3:
        #Que tipo de triângulo é?
        print('EQUILÁTERO')
    elif n1 == n2 or n1 == n3 or n2 == n3:
        print('ISÓSCELES')
    else:
        print('ESCALENO')
else:
    print('Não forma triângulo!')

#Pense ASSIM:
#Pode existir?
#sim → qual tipo?
#não → acabou
