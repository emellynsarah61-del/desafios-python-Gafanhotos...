from datetime import date
ano = int(input('Digite o ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano
if idade < 18:
    faltam = 18 - idade
    print('Você ainda vai se alistar')
    print('Faltam {} anos para o alistamento'.format(faltam))
elif idade == 18:
    print('Já é hora de se alistar!')
else:
    passou = idade - 18
    print('Já passou do alistamento!')
    print('Passaram {} anos do prazo'.format(passou))
