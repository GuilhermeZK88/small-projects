this_data = 'Altair Silva\tPP dep.altairsilva@alesc.sc.gov.br 303 (48) 3221-2729 Ana Campagnolo\tPL ana@alesc.sc.gov.br 008 (48) 3221-2686 Antídio Lunelli\tMDB depantidiolunelli@alesc.sc.gov.br 027 (48) 3221-2695 Camilo Martins\tPODEMOS camilo@camilomartins.com.br 010 (48) 3221-2677 Carlos Humberto\tPL deputado@carloshumberto.sc 036 (48) 3221-2653 Delegado Egidio\tPTB deputadoegidio@alesc.sc.gov.br 102 (48) 3221-2638 Dr. Vicente Caropreso\tPSDB dr.vicente@alesc.sc.gov.br 118 (48) 3221-2640 Emerson Stein *\tMDB deputadoemerson@alesc.sc.gov.br 037 (48) 3221-2683 Fabiano da Luz\tPT fabiano@fabianodaluz.com.br 305 (48) 3221-2628 Fernando Krelling\tMDB fernandokrelling@alesc.sc.gov.br 206 (48) 3221-2650 Ivan Naatz\tPL ivannaatz@alesc.sc.gov.br 115 (48) 3221-2801 Jair Miotto\tUNIÃO BRASIL jairmiotto@alesc.sc.gov.br 117 (48) 3221-2748 Jessé Lopes\tPL dep.jesselopes@alesc.sc.gov.br 116 (48) 3221-2698 José Milton Scheffer\tPP josemilton@alesc.sc.gov.br 025 (48) 3221-2671 Julio Garcia\tPSD juliogarcia@alesc.sc.gov.br 107 (48) 3221-2667 Lucas Neves\tPODEMOS lucasneves@alesc.sc.gov.br 09 (48) 3221-2807 Luciane Carminatti\tPT lucianecarminatti13@gmail.com 304 (48) 3221-2998 Marcius Machado\tPL marcius.machado@alesc.sc.gov.br 204 (48) 3221-2717 Marcos da Rosa\tUNIÃO BRASIL depmarcosdarosa@alesc.sc.gov.br 104 (48) 3221-2577 Marcos Vieira\tPSDB marcosvieira@alesc.sc.gov.br 302 (48) 3221-2707 Mário Motta\tPSD depmariomotta@alesc.sc.gov.br 110 (48) 3221-2839 Marquito\tPSOL marquitopsol@gmail.com 026 (48) 3221-2662 Massocco\tPL deputadomassocco@alesc.sc.gov.br 111 (48) 3221-2723 Matheus Cadorin\tNOVO contato@matheuscadorin.com.br 105 (48) 3221-2732 Maurício Eskudlark\tPL eskudlark@alesc.sc.gov.br 101 (48) 3221-2874 Maurício Peixer *\tPL depmauriciopeixer@gmail.com 106 (48) 3221-2689 Mauro de Nadal\tMDB maurodenadal@alesc.sc.gov.br 103 (48) 3221-2702 Napoleão Bernardes\tPSD gabinete@napoleaobernardes.com.br 035 (48) 3221-2715 Neodi Saretta\tPT gabinetesaretta@alesc.sc.gov.br 033 (48) 3221-2665 Nilso Berlanda\tPL deputadoberlanda@alesc.sc.gov.br 109 (48) 3221-2645 Oscar Gutz\tPL gabineteoscargutz@alesc.sc.gov.br 207 (48) 3221-2953 Padre Pedro Baldissera\tPT padrepedro@alesc.sc.gov.br 113 (48) 3221-2726 Paulinha\tPODEMOS gabinetepaulinha@gmail.com 203 (48) 3221-2734 Pepê Collaço\tPP pepe.collaco@alesc.sc.gov.br 034 (48) 3221-2644 Repórter Sérgio Guimarães\tUNIÃO BRASIL sergioguimaraes@alesc.sc.gov.br 108 (48) 3221-2980 Rodrigo Minotto\tPDT rodrigominotto@alesc.sc.gov.br 114 (48) 3221-2656 Sargento Lima\tPL dep.sargentolima@alesc.sc.gov.br 023 (48) 3221-2966 Sergio Motta\tREPUBLICANOS depsergiomotta@alesc.sc.gov.br 028 (48) 3221-2737 Tiago Zilli\tMDB deptiagozilli@alesc.sc.gov.br 205 (48) 3221-2795 Volnei Weber\tMDB volneiweber@alesc.sc.gov.br 112 (48) 3221-2720'

def Processing_this_data(string):
    pos_nome = False
    letter_counter = 0
    output = ''
    deputado_counter = 1
    #'ciclar letras'
    for letter in this_data:
        #se "\t", trocar por espaço " "
        if letter == '\t':
            letter = ','
            #se fim de subdado, colocar vírgula
            #se espaço do nome, manter espaço
            pos_nome = True
        #se espaço e depois do nome (aka: não é espaço entre nome)
        elif letter == ' ' and pos_nome:
            #se espaço, então "\n" se fim, "," se meio, " " se depois do prefixo do telefone
            
            #checando se um cada dos últimos 4 char são número, preceded continuará true
            precededby4numb = True
            for i in [1,2,3,4]:
                if this_data[letter_counter - i].isnumeric():
                    pass
                else:
                    precededby4numb = False
                    
                    #se depois de um ')', é no meio do telefone
                    if this_data[letter_counter - i] == ')':
                        letter = ''
                        break
                    #se antecede uma palavra em caps, então partido com 2 nomes
                    elif this_data[letter_counter + 2].isupper():
                        letter = ' '
                        break

                    #se não precedido por ')' ou 4 numb, não é o fim
                    letter = ','
                    precededby4numb = False
                    break
            #estamos depois de 4 numb? fim do deputado
            if precededby4numb:
                letter = '\n'
                pos_nome = False
                deputado_counter += 1
                
        letter_counter += 1
        output += letter
    print(f'Os {deputado_counter} deputados são:')
    return output

print( Processing_this_data(this_data) )
