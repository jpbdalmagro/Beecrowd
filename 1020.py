dia = int(input())

ano = dia // 365
dia = dia % 365
mes = dia // 30
dia = dia % 30

print('''{} ano(s)
{} mes(es)
{} dia(s)'''.format(ano, mes, dia))
