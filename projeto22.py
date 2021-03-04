def linha():
    print('='*50)

def espaco ():
    print ('')

linha ()
print ('Bem vindo!!Neste jogo você se tornara o investigador e salvará o carnaval!')
linha()

print ('Onde está o ChameGIT?')
print('O cantor Promp Pyano escreveu um forró eletrônico que irá estourar no carnaval pós pandemia.\n\
Porém na sua ida ao estúdio para gravar Promp dá falta do hit e se desespera. \n\
Ajude Promp a saber onde e com quem está o hit "ChameGIT" e salve o carnaval.')
espaco()


nome = input('Digite seu nome e codinome: ')
idade = input('Agora digite sua idade: ')

espaco()
print('Agora que você já se identificou e entendeu o caso \n\
    escolha entre três opções de cenário para começar sua investigação.')
espaco()

print('1.Cenário: Procurar no Estúdio de Promp Pyano.')
espaco()
print('2.Cenário: Procurar na casa de Promp Pyano')
espaco()
print('3.Cenário: Conversar com seus sócios para obter informações.')
espaco()

escolha_cena = int(input('Escolha o número do cenário que deseja investigar: '))
espaco()

if escolha_cena == 1:
   
    print('1.Perguntar Ifgênio empresário de Promp. \n\
    2.Perguntar aos funcionários do estúdio.')
    
    pergunt_1 = int(input(":"))   
    
    if pergunt_1 == 1:
        print('Infelizmente não está aqui. Fim de Jogo! Você não conseguiu achar o GITHIT.')
   
    elif pergunt_1 == 2:
        print('Os funcionários dizem que não tem idéia de onde esteja. Fim de Jogo!')
        espaco() 

elif escolha_cena == 2:
    
    print('A esposa de Promp te recebe em casa, e pela conversa você percebe que ela está nervosa.Após a conversa você pode: \n\
    1.Segui-lá e encontra-lá vendendo um papel sugestivo para o irmão de Promp.\n\
    2.Resolve deixar passar por achar que ela está abalada com a situação.')
    
    pergunt_2 = int(input(":"))
    
    if pergunt_2 == 1:
        
        print('Parabéns!! Sua desconfiança te levou a vitória.O GIThit está com a esposa de Promp que o vendeu para seu cunhado.')
    
    elif pergunt_2 == 2:
       
        print('Você foi tapeado!! Fim da linha de investigação para você.')

if escolha_cena == 3:
   
    print('Promp possui dois sócios, seu irmão gêmeo Elif e seu cunhado Elsemar. \n\
    1.Se você escolher o cunhado Elsemar você irá descobrir que:\n\
    2.Se você escolher o irmão de Promp,Elif você irá descobrir que:')
    
    pergunt_3 = int(input(":"))
   
    if pergunt_3 == 1:
        print('Seu faro para apuração te trouxe ao fim do jogo. Continue tentando.')
    
    if pergunt_3 == 2:
        print('Parabéns você salvou o carnaval de Promp!!\n\
    O hit foi pego por Elif para se passar por seu irmão Promp e ganhar a fama que o hit "ChameGIT" trará.')
    