distancia = float(input('Distancia da viagem: '))
if distancia <= 200:
    d = distancia * 0.5
    print('O valor será {}'.format(d))
else:
    p = distancia * 0.45
    print('O valor será {}'.format(p))
