times=('Flamengo', 'Palmeiras', 'Santos', 'Corinthians', 'São Paulo', 'Grêmio', 'Bahia', 'Internacional', 'Goiás', 'Athletico-PR', 'Vasco da Gama',
'Atlético', 'Botafogo', 'Fluminense', 'Fortaleza', 'Ceará', 'CSA', 'Cruzeiro', 'Avaí','Chapecoense')

print('=-'*80)
print(f'Primeiros 5 colocados da tabela foram: {times[0:5]}')
print('=-'*80)
print(f'Últimos 4 colocados: {times[16:]}') ## ou times[-4:] dá o mesmo resultado
print(f'Times em ordem alfabética: {sorted(times)}')
print(f'O Chapecoense está na {times.index("Chapecoense")+1}ª posição')

