n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo: '))
n3 = int(input('Digite o terceiro: '))

# Menor
if n1 < n2 and n1 < n3:
    menor = n1
elif n2 < n1 and n2 < n3:
    menor = n2
else:
    menor = n3

# Maior
if n1 > n2 and n1 > n3:
    maior = n1
elif n2 > n1 and n2 > n3:
    maior = n2
else:
    maior = n3

print('O número menor é: {}'.format(menor))
print('O número maior é: {}'.format(maior))

