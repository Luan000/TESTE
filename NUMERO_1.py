import cont
p = '\033[m'
am = '\033[33m'
text = 'SOMA DAS DESPESAS E LUCROS DA LOJA'
print(f'{am}='*len(text))
print(text)
print('='*len(text), f'{p}')

vendas = ['ÓCULOS', 'ÓCULOS DE DESCANSO', 'BONÉS', 'CUECAS', 'MEIAS', 'CORTA VENTO', 'CALÇAS JEANS',
          'BERMUDAS ELASTANO', 'BERMUDAS TECTEL', 'CAMISAS LISTRDAS', 'CAMISAS DE SURF', 'CAMISAS POLO ALEATORY',
          'CAMISAS DE TIME', 'POLOS VARIADAS', 'CAMISAS DA TOMMY', 'GATILHOS', 'TÊNIS 4 MOLA', 'TÊNIS FLEK', 'TÊNIS MODOC',
          'TÊNIS FILA']
tot = fun = valor = acm = valorpago = tottenis = tot2 = s = vl = 0
valor = float(input(f'VALOR TOTAL DAS VENDAS: R$'))
vl = valor
resp = str(input('VENDEU ROUPAS OU OUTROS TIPOS DE ACESSÓRIOS [S/N]? ')).upper().strip()[0]
if resp == 'S':
    for c in range(0, 20):
        quanti = int(input(f'QUANTIDADE DE VENDAS DE {am}{vendas[c]}{p}: '))
        if quanti >= 1:
            tot = cont.total(c, quanti, valor)
            acm = tot
            valor = tot
            if c <= 15:
                fun += quanti
        if c >= 16 and quanti >= 1:
            tot2 += quanti
            s += quanti
    tot2 = tot2 * 5
elif resp == 'N' and valor > 1:
    acm = valor
print('-='*25)
while True:
    resp = str(input('VENDEU MAIS ALGUM PRODUTO POR FORA [S/N]? ')).upper().strip()[0]
    if resp == 'N':
        print('OK...')
        print('-=' * 25)
        break
    else:
        valorpago = int(input(f'{am}DIGITE O VALOR QUE VOCÊ PAGOU PELO PRODUTO{p}: '))
        acm = acm - valorpago
        tenis = str(input('FOI UM TÊNIS [S/N]? ')).strip().upper()[0]
        if tenis == 'S':
            q = int(input('QUANTOS ?'))
            tottenis = tottenis + q * 5
print('=============== FUNCIONÁRIOS =================')
print(f'TOTAL DE TÊNIS VENDIDOS: {s} COMISSÃO R${tot2}')
print(f'TOTAL DOS OUTROS PRODUTOS VENDIDOS : {fun} COMISSÃO R${fun*0.50}')
print(f'COMISSÃO DE TÊNIS ENCOMENDADO: R${tottenis}')
fun = fun * 0.50 + 20 + tottenis
fun += tot2
if vl >= 500:
    print('COMISSÃO DE META: R$5.00')
    fun = fun + 5
print(f'GANHO TOTAL R${fun}')
print('-='*25)
acm = acm - 2 * fun
print(f'VALOR TOTAL DAS VENDAS: {vl}')
print(f'{am}SEU LUCRO{p}: R${acm}')