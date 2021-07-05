### Parte 1 do desafio

investimento = input('Digite o valor a ser investido R$: ')
investimento = float(investimento)

investimento *= 30
qtdclick = investimento * .12
compartilhamento = qtdclick * .15
visualizacao = compartilhamento * 40

print(f'Aproximadamente {investimento + visualizacao:.0f} pessoas visualizarao o anuncio.')


### Parte 2 do desafio

import datetime
def lin():
    print ('-'*40)
dados = {}


def cadastro(cliente, vi, vm, qtdm, cm):
    dados.update({"Cliente": cliente, "Valor total investido R$": vi, "Visualizações máximas": vm,
                  "Cliques máximos": qtdm, "Compartilhamentos máximos": cm})
v = 1
opcao = 0
while v != 0 and opcao != 3:

    print('1  Cadastrar anúncio.')
    lin()
    print('2 Ver relatorio de anuncio cadastrado.')
    lin()
    print('3 Sair do programa.')
    lin()

    opcao = int(input('Digite a opcao desejada :'))
    if opcao == 1:
        nome_do_anuncio = str(input('Digite o nome do anúncio:'))
        cliente = str(input('Digite o nome do cliente:'))
        diai = int(input('Digite o dia de ínicio no formato dd/ / :'))
        mesi = int(input('Digite o mês no formato /mm/ :'))
        anoi = int(input('Digite o ano no formato / /aaaa :'))

        diaf = int(input('Digite o dia de término dd/ / :'))
        mesf = int(input('Digite o mes de termino /mm/ :'))
        anof = int(input('Digite o ano de termino / /aaaa :'))

        investimento_por_dia = float(input('Digite o valor a ser investido: R$'))
        print('Cadastro realizado')
        v = int(input('Digite 1 para voltar ao menu:'))


        datai = datetime.datetime(year=anoi, month=mesi, day=diai)
        dataf = datetime.datetime(year=anof, month=mesf, day=diaf)

        dif = dataf - datai

        days = dif.days
        years, days = days // 365, days % 365
        months, days = days // 30, days % 30

        total_invest = dif.days * investimento_por_dia
        a4 = total_invest * 30
        qtdclick = a4 * .12
        compartilhamento = qtdclick * .15
        visualizacao = compartilhamento * 40

        max_visualizacao = a4.__ceil__() + visualizacao.__ceil__()
        max_qtdclick = qtdclick.__ceil__()
        max_compartilhamento = .15 * qtdclick.__ceil__()
        a5 = max_compartilhamento.__ceil__()
        cadastro(cliente, total_invest, max_visualizacao, max_qtdclick, a5)


    elif opcao == 2:
        resp = str(input('Digite o nome do cliente'))
        for n, v in dados.items():
            if resp == dados['Cliente']:
                print(n, v)
            else:
                lin()

                print('O usuario nao esta cadastrado por favor verifique novamente')
                lin()

                break
