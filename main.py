import json
import random as rd # Usado para determinar músicas e filtros aleatórios, enquanto ainda nao temos integração externa com api

# Nesse código existe conteúdos que fazem parte da sprint 4, sendo eles: json e try/except, 
# Além disso, sobre o conteúdo que não foi dado em aula, foi utilizado upper() e manipulações de strings com cor, slicing e alinhamento para prints

def print_invalido(): # Função para printar que a entrada é inválida
    print('\nEntrada inválida!! ')
    print('Tente novamente!! \n\n')

def permissoes_aplicativo(): # Função para o usuário permitir o acesso a outros aplicativos
    while True:
        print("Pra começar, precisamos  de algumas permissões:\n")
        print("O Synesthesia precisa acessar sua câmera e galeria.")
        print("Usamos isso para aplicar filtros inteligentes com base no seu ambiente.")
        print("\n🔒 Fique tranquilo: todo o processamento é feito direto no seu celular!")
        
        print('\nDigite:')
        print('1 - Permitir tudo')
        print("2 - Não permitir\n")

        permissao = input()

        match permissao:
            case '1':
                return

            case '2':
                print('\n\nPara usar nosso sistema, você precisa permitir tudo!! ')
                print('Tente novamente!\n')

            case _:
                print_invalido() 

def permissoes_dados(): # Função para permitir uso de dados
    while True:
        print("\n" + "="*40)
        print("          🛡️ PRIVACIDADE DE DADOS")
        print("="*40)
        print("Sua privacidade é nossa prioridade.")
        print("Para melhorar a sua experiência, o Synesthesia")
        print("precisa coletar dados anônimos de uso:")
        print("\n* Uso de Filtros: Para sabermos quais você mais gosta!")
        print("* Erros do App: Para corrigirmos bugs rapidamente!")
        print("* Metadados: músicas escolhidas, para melhores recomendações!")
        print("\n⚠️  Nenhuma foto ou informação pessoal sai do seu celular!")
        
        print('\nDigite:')
        print('1 - Aceito compartilhar dados de melhoria')
        print("2 - Prefiro não compartilhar meus dados")
        
        try: # Usado para verificação de entrada
            escolha = int(input("\nSua escolha: "))
            
            if escolha == 1:
                print("\n✅ Obrigado! Você está ajudando o Synesthesia a evoluir.")
                return 'ACEITO'
            
            elif escolha == 2:
                print("\nSua experiência será afetada! Caso mude de ideia, poderá aceitar no futuro! ")
                return 'RECUSADO'
            
            else:
                print("\nOpção inválida! Escolha 1 ou 2.")
        
        except ValueError:
            print("\nPor favor, digite apenas o número 1 ou 2.")

def print_camera(visu,filtros_formatados): #Função para mostrar o visor da câmera em tempo real
    print(f'''
        _________________________________________
        | 📱                                      |
        |  [ 8:08 ]            📡   📶   🔋 100%  |
        |_________________________________________|
        |                                         |
        |                              [  ⚙️   ]   |
        |_________________________________________|
        |                                         |
        |                                         |
        |                                         |
        |                                         |
        |                                         |
        |                                         |
        |                   {visu}                    |
        |                                         |
        |                                         |
        |                                         |
        |                                         |
        |                                         |
        |_________________________________________|
        |                                         |
        |  Filtros disponíveis:                   |
        |  {filtros_formatados[0]:<10}      {filtros_formatados[1]:<10}      {filtros_formatados[2]:<10} |
        |  {filtros_formatados[3]:<10}      {filtros_formatados[4]:<10}      {filtros_formatados[5]:<12} |
        |  {filtros_formatados[6]:<38} |
        |                                         |
        |                                         |  
        |    🖼️             ⚪             🔄      |
        |                                         |
        |          _______________________        |
        |_________[_______________________]_______|
    ''')

def print_foto(visu,filtro,musica,descricao_musica,num1,num2): # Função para mostrar o visor da foto no seu editor 
    print(f'''
        _________________________________________
        | 📱                                      |
        |  [ 8:08 ]            📡   📶   🔋 100%  |
        |_________________________________________|
        |                                         |
        |                                         |
        |_________________________________________|
        |                                         |
        |                                         |
        |                                         |
        |                                         |
        |                                         |
        |                                         |
        |                   {visu}                    |
        |                                         |
        |                                         |
        |                                         |
        |                                         |
        |                                         |
        |_________________________________________|
        |                                         |
        |  Filtro aplicado: {filtro[:21]:<21}  |
        |                                         |
        |  Música aplicada: {musica:<22} |
        |  Descrição música: {descricao_musica:<10} |
        |  Trecho: 00:{num1:02} até 00:{num2:02} = {num2-num1:02} segundos  |
        |                                         |
        |                                         |
        |    ⬇️             ▶️             🔗       |
        |                                         |
        |          _______________________        |
        |_________[_______________________]_______|
    ''')

def escolha_filtros(nomes_filtros,filtro_atual): # Função para o usuário dizer qual filtro deseja escolher
    while True:
        print('\nEscreva o nome do filtro desejado (sem o emoji). ')
        print('Caso queira voltar ao menu principal digite SAIR: ')
        filtro_desejado = input('').upper() # Usado upper() para verificação de entrada

        if filtro_desejado == 'SAIR':
            return filtro_atual
    
        elif filtro_desejado in nomes_filtros:
            if filtro_desejado == filtro_atual:
                print('\nEsse filtro já está selecionado, digite outro! \n ')

            else:
                return filtro_desejado    

        else:
            print('\nEsse filtro não foi encontrado! ')
            print('Tente novamente\n')

def menu_de_edicao_da_foto(id,nomes_filtros,filtros): # Função para mostrar o menu de edição de foto

    # Recebe as fotos da galeria.json atualizada

    with open('galeria.json', 'r', encoding='utf-8') as g: 
        dados_fotos = json.load(g)["fotos"]
    
    foto_escolhida = dados_fotos[id] # Recebe os dados de determinada foto
    
    # Abaixo vão ser armazenadas em variáveis cada dado da foto
    visu = foto_escolhida["visu"]
    filtro_atual = foto_escolhida["filtro"]
    filtro_formatado = foto_escolhida["filtro_formatado"]
    musicas_sorteadas = foto_escolhida["musicas"]
    musica_escolhida = foto_escolhida["musica"]
    musica_formatada = foto_escolhida["musica_formatada"]
    descricao_musica = foto_escolhida["descricao_musica"]
    num1 = foto_escolhida["num1"]
    num2 = foto_escolhida["num2"]
    
    while True:  
        nomes_musicas = [] # Lista usada para armazenar os nomes das 4 músicas determinadas para a foto, que será usada para verificações de entrada

        for i in range(5):
            nomes_musicas.append(musicas_sorteadas[i]['nome'])

        # Laço de repetição para atualizar a música formatada e sua descrição para serem printadas e caso usuário queira, salvar as informações atualizados 
        for m in musicas_sorteadas: 
            if m['nome'] == musica_escolhida:
                musica_formatada = m['formatada']
                descricao_musica = m['descricao']

        print_foto(visu,filtro_formatado,musica_formatada,descricao_musica,num1,num2) # Imagem do visor de edição da foto

        print('\nDigite a opção desejada:')                  
        print('1 - Trocar música') # Troca a música aplicada na foto por outra uma das outras 3 que nosso sistema determinou para a foto               
        print('2 - Ajustar tempo da música') # Ajusta o tempo da música aplicada para o trecho que mais agrada o usuário
        print('3 - Tocar a música') # Por enquanto só printa que a música está tocando sem interatividade
        print('4 - Alterar filtro') # Altera o filtro da foto 
        print('5 - Salvar mudanças e compartilhar foto') # Salva as mudanças feitas pelo usuário e compartilha a foto com algum aplicativo 
        print('6 - Apagar foto e retornar para a galeria') # Apaga a foto e retorna para a galeria   
        print('7 - Salvar mudanças e voltar para a câmera') # Salva as mudanças feitas e volta para câmera
        print('8 - Voltar para a câmera sem salvar mudanças\n') # Volta para câmera sem salvar a foto

        menu_foto = input('')

        match menu_foto:
            case '1':
                while True:
                    print('Encontrei essas músicas para sua foto: ')

                    # Laço de repetição para printar as músicas que não estão aplicadas na foto
                    for m in musicas_sorteadas: 
                        texto = m['formatada']
                        if m['nome'] != musica_escolhida:
                            print()
                            print(texto)
                            print(m['descricao'])

                    print('\nDigite o nome da música desejada (ou "Sem som") para continuar: ')
                    musica_desejada = input('Caso queira voltar ao menu principal digite SAIR: ').upper()

                    if musica_desejada in nomes_musicas:
                        if musica_desejada == musica_escolhida:
                            print('\nEssa música já está selecionada, digite outra! \n ')

                        else:
                            musica_escolhida = musica_desejada
                            # Caso o usuário trocar de música, o tempo da música retornará para o padrão de 30 segundos
                            num1 = 0
                            num2 = 30
                            break

                    elif musica_desejada == 'SAIR':
                        break

                    else:
                        print('\nEssa música não foi encontrada! ')
                        print('Tente novamente\n')

            case '2':   
                if musica_escolhida != 'SEM SOM':
                    print('\nEscolha o intervalo da música que você quer tocar (máximo de 30 segundos).')
                    print('\nPara cancelar e voltar ao menu de edição, digite 00 \n')
                    
                    while True:
                        try: # Usado para verificação de entrada
                            numero1 = int(input('Digite o segundo inicial da música: ')) 
                            numero2 = int(input('Digite o segundo final da música: '))                      
                
                            if (0 <= numero1 <= 30) and (0 <= numero2 <= 30):
                                if numero1 == 0 and numero2 == 0:
                                    break

                                elif numero1 > numero2:
                                    print('\nEscolha um tempo de término maior que o de início. ')
                                    print('Tente novamente! \n')

                                elif (numero1 == numero2) or ((numero2 - numero1) == 1):
                                    print('\nA música precisa ter no mínimo 2 segundos. ')
                                    print('Tente novamente! \n')

                                else:
                                    num1 = numero1
                                    num2 = numero2
                                    print(f'\nVocê selecionou a música entre o intervalo {num1} e {num2}\n')
                                    break

                            else:
                                print("\nPor favor, digite dois números entre 0 e 30! ")

                        except ValueError:
                            print("\nEntrada inválida! Digite dois números entre 0 e 30.\n")   
                else:
                    print('\nVocê precisa aplicar uma música para utilizar essa função.')

            case '3':
                if musica_escolhida != 'SEM SOM':
                    print(f"\n\nTocando {num2-num1} segundos da seguinte música: {musica_formatada}\n")
                
                else:
                    print('\nVocê precisa aplicar uma música para utilizar essa função.')

            case '4':
                print('\nAs opções de filtros disponíveis são: ')

                # Laço de repetição usado para printar os filtros não aplicados na foto
                for f in filtros: 
                    if filtro_atual != f['nome']:
                        print(f['formatado'])                    

                filtro_atual = escolha_filtros(nomes_filtros,filtro_atual) # Função para o usuário escolher novo filtro

                filtros_formatados = [] # Lista com os filtros formatados com emojis e o filtro aplicado em destaque

                for f in filtros:
                    texto = f['formatado']                     
                    filtros_formatados.append(f"\033[31m【 {texto} 】\033[0m" if f['nome'] == filtro_atual else texto)

                    if filtro_atual == f['nome']:
                        filtro_formatado = texto
            
            case '5':
                # Opções de compartilhamento do nosso aplicativo
                opcoes_compartilhamento = ['Instagram','TikTok','Whatsapp','Twitter','Linkedin']

                print('\n\nEscolha uma rede para compartilhar: \n')
                print('1 - Instagram')
                print('2 - TikTok')
                print('3 - WhatsApp')
                print('4 - Twitter (X)')
                print('5 - Linkedin')
                print('6 - Voltar ao menu de edição')

                while True:
                    try: # Usado para verificação de entrada
                        rede_social = int(input(''))

                        if not (1 <= rede_social <= 6):
                            print('\nNão existe essa opção. ')
                            print('Tente novamente!\n')

                        elif rede_social == 6:
                            break
                        
                        else:       
                            # Caso o usuário compartilhe com alguma rede social, antes disso o sistema salvará a foto e depois, enviará para o aplicativo desejado
                            foto_editada = {
                                "id": id+1,
                                "visu": visu, 
                                "filtro": filtro_atual,
                                "filtro_formatado": filtro_formatado,
                                "musicas": musicas_sorteadas,
                                "musica": musica_escolhida,
                                "musica_formatada": musica_formatada,
                                "descricao_musica": descricao_musica,
                                "num1": num1,
                                "num2": num2
                            }

                            dados_fotos[id] = foto_editada 
                            conteudo_para_salvar = {"fotos": dados_fotos}

                            with open('galeria.json', 'w', encoding='utf-8') as g: 
                                json.dump(conteudo_para_salvar, g, indent=4, ensure_ascii=False) 

                            print(f'\n\nFoto salva e compartilhada com sucesso para a rede {opcoes_compartilhamento[rede_social-1]}!\n')
                            break

                    except ValueError:
                        print_invalido()
        
            case '6':
                # Apaga da lista de fotos a foto que está sendo utilizada no editor no momento
                dados_fotos.pop(id)

                # Laço de repetição para reajustar os IDs de todas as fotos que sobraram, caso o usuário apague alguma do meio 
                if id != len(dados_fotos) - 2: 
                    for i, foto in enumerate(dados_fotos):
                        foto['id'] = i + 1

                conteudo_para_salvar = {"fotos": dados_fotos}

                # Atualiza galeria.json sem a foto, e corrigindo possíveis erros de numeração
                with open('galeria.json', 'w', encoding='utf-8') as g: 
                    json.dump(conteudo_para_salvar, g, indent=4, ensure_ascii=False) 

                break

            case '7':
                # Cria um dicionário com os novos dados da foto
                foto_editada = {
                    "id": id+1,
                    "visu": visu,
                    "filtro": filtro_atual,
                    "filtro_formatado": filtro_formatado,
                    "musicas": musicas_sorteadas,
                    "musica": musica_escolhida,
                    "musica_formatada": musica_formatada,
                    "descricao_musica": descricao_musica,
                    "num1": num1,
                    "num2": num2
                }

                dados_fotos[id] = foto_editada 
                conteudo_para_salvar = {"fotos": dados_fotos}

                # Atualiza a foto no galeria.json
                with open('galeria.json', 'w', encoding='utf-8') as g: 
                    json.dump(conteudo_para_salvar, g, indent=4, ensure_ascii=False) 

                break
            
            case '8':
                break

            case _:
                print_invalido()

def main(uso_dados): # Função principal para mostrar o visor da câmera

    # As variáveis abaixo servem para setar as configurações padrões da câmera, sendo possível alterá-las pelo usuário
    filtro_automatico = 'ATIVADO'
    grade_de_composicao = 'DESATIVADO'
    sugestao_automatica = 'ATIVADO'

    traseira = True # Variável para saber se o usuário está vendo a câmera traseira ou frontal
    visu = '🌄' # Imagem do visor da câmera

    # Recebe o filtros.json do nosso sistema
    with open('filtros.json', 'r', encoding='utf-8') as f:
        dados_filtros = json.load(f) 

    filtros = dados_filtros['filtros'] # Aqui ficará armazenado a lista de dados dos filtros para ser usado em verificações

    filtro_determinado = rd.randint(0,6) # Esse número vai determinar o filtro julgado pelo nosso sistema como o filtro da 'Vibe' da imagem no leitor da câmera em tempo real. Entretanto, como não temos integração ainda, ele terá um filtro aleatório setado como inicial

    filtro_atual = filtros[filtro_determinado]['nome'] # Aqui vai ser armazenado o nome do filtro selecionado para ser usado em verificações

    filtro_formatado = filtros[filtro_determinado]['formatado'] # Aqui vai ser armazenado o filtro selecionado formatado com emoji para ser usado no menu de edição

    while True:        
        filtros_formatados = [] # Lista dos filtros formatados com os emojis e o filtro aplicado em destaque
        nomes_filtros = [] # Aqui ficará armazenado os nomes dos filtros puros para verificações de entrada

        for f in filtros:
            texto = f['formatado'] # Recebe o nome do filtro formatado com o emoji
            nomes_filtros.append(f['nome'])

            # Adiciona na lista com destaque se for o filtro atual, senão adiciona somente o filtro com emoji
            filtros_formatados.append(f"\033[31m【 {texto} 】\033[0m" if f['nome'] == filtro_atual else texto)
            
            # Atualiza a variável 'filtro' caso o usuário tiver selecionado outro filtro
            if f['nome'] == filtro_atual: 
                filtro_formatado = texto

        print_camera(visu, filtros_formatados)

        print('\nDigite a opção desejada:')     
        print('1 - Tirar Foto') # Tira a foto com as informações que o usuário estiver vendo no momento
        print('2 - Entrar na galeria') # Acessa a galeria do nosso sistema, podendo editar fotos já tiradas 
        print('3 - Ajustes') # Configurações padrões da câmera 
        print('4 - Alterar filtro em tempo real') # Altera o filtro em tempo real 
        print('5 - Virar câmera') # Vira a câmera do celular 
        print('6 - Sair do aplicativo\n') # Fecha o aplicativo

        menu_inicial = input()

        match menu_inicial:
            case '1':
                # Aqui o sistema determinará quais são as 3 músicas que mais combinam com a foto, mas no momento ela só vai escolher 3 músicas aleatórias
                with open('musicas.json', 'r', encoding='utf-8') as m:
                    dados_musicas = json.load(m) 

                musicas = dados_musicas['musicas'] 
                    
                musicas_sorteadas = rd.sample(musicas, k=4) # Aqui estão armazenadas as músicas que o nosso sistema sorteou 

                sem_som = {"nome": "SEM SOM", "descricao": "A foto fala por si só", "formatada": "Sem Som"} # Cria a possibilidade da foto ficar sem som
                musicas_sorteadas.append(sem_som)
                
                # Com nossa API grátis, por enquanto só conseguimos 30 segundos de cada música
                # Como ainda não temos integração com essa API, o tempo da música é figurativo e só serve para mostrar ao usuário o tempo da música e dar a opção de editá-lo 

                num1 = 0 # Variável para mostrar o segundo que a música começa

                if sugestao_automatica == 'ATIVADO': # Se essa configuração estiver ligada
                    musica_escolhida = musicas_sorteadas[0]['nome'] # Nome da música escolhida pela IA para verificações de entrada
                    descricao_musica = musicas_sorteadas[0]['descricao'] # Descrição da música escolhida pela IA
                    musica = musicas_sorteadas[0]['formatada'] # Música escolhida formatada com o artista

                    num2 = 30 # Variável para mostrar o segundo que a música termina

                else: # Se a configuração estiver desligada, não terá música aplicada na foto, até o usuário aplicar alguma
                    musica_escolhida = musicas_sorteadas[4]['nome'] # Nome da música escolhida pela IA para verificações de entrada
                    descricao_musica = musicas_sorteadas[4]['descricao'] # Descrição da música escolhida pela IA
                    musica = musicas_sorteadas[4]['formatada'] 

                    num2 = 0

                # Todas as músicas, por enquanto tem por padrão 30 segundos, mas ao usuário salvar a foto, ela pode ter menos tempo de duração 

                # Nosso sistema recebe todas as fotos da galeria.json para criar um novo índice ao adicionar a foto recém tirada
                with open('galeria.json', 'r', encoding='utf-8') as g: 
                    dados_fotos = json.load(g)['fotos']

                    novo_id = len(dados_fotos) + 1 

                    nova_foto = { # Cria um dicionário com os dados da foto tirada
                        "id": novo_id,
                        "visu": visu,
                        "filtro": filtro_atual,
                        "filtro_formatado": filtro_formatado,
                        "musicas": musicas_sorteadas,
                        "musica": musica_escolhida,
                        "musica_formatada": musica,
                        "descricao_musica": descricao_musica,
                        "num1": num1,
                        "num2": num2
                    }

                    dados_fotos.append(nova_foto) # Adiciona essa foto ao conjunto de fotos
                    conteudo_para_salvar = {"fotos": dados_fotos} # Salva esse conjunto no dicionário

                    # Atualiza galeria.json com a nova foto
                    with open('galeria.json', 'w', encoding='utf-8') as g: 
                        json.dump(conteudo_para_salvar, g, indent=4, ensure_ascii=False) 

                # Entra no menu de edição de foto
                menu_de_edicao_da_foto(novo_id - 1,nomes_filtros,filtros) 

                # Ao voltar para câmera o sistema recalculará o filtro adequado de acordo com o que aparecer no visor
                # Novamente será determinado um filtro aleatório

                filtro_atual = filtros[rd.randint(0,6)]['nome'] 
        
            case '2':
                while True:
                    print("\nBem vindo à Galeria")
                    print('Fotos do Synesthesia: ')

                    # Recebe todas as fotos da galeria
                    with open('galeria.json', 'r', encoding='utf-8') as g:
                        dados_fotos = json.load(g)['fotos']

                    galeria = dados_fotos

                    # Mostra todas as fotos salvas na galeria
                    for i in galeria:
                        print(f"\nA {i['id']}º foto possui o filtro {i['filtro_formatado']}")
                        print(f"E a seguinte música: {i['musica_formatada']}")

                    voltar = False # Variável usada para saber se o usuário deseja voltar para câmera

                    while True:
                        try: # Usado para validação de entrada
                            print('\nDigite o número da foto desejada para editá-la:')
                            print('Caso deseje voltar para câmera, digite 0')
                            opcao_foto = int(input(''))

                            if opcao_foto == 0:
                                voltar = True
                                break

                            elif 0 < opcao_foto <= len(galeria):
                                menu_de_edicao_da_foto((opcao_foto-1),nomes_filtros,filtros) # Com alguma foto existente escolhida pelo usuário, ele irá entrar no menu de edição para editá-la
                                break
                            else:
                                print('\nEssa foto não existe!')
                                print('Tente novamente!\n')

                        except ValueError:
                            print_invalido()
                    
                    if voltar == True:
                        break
                    
            case '3':
                # Menu de edição dos ajustes da câmera
                while True:
                    print('\n\nAjustes — Digite o número para alterar:')
                    print()
                    print('📸 Câmera e Composição:')
                    print(f'1. Filtro Automático: [{filtro_automatico}]')
                    print('Aplica o filtro ideal com base no ambiente.')
                    print()                    
                    print(f'2. Grade de composição: [{grade_de_composicao}]')
                    print('Ativa a regra dos terços no visor.')
                    print()
                    print('🎵 Música e Áudio')
                    print(f'3. Sugestão Inteligente: [{sugestao_automatica}]')
                    print('O Gemini escolhe a trilha sonora após a captura.')
                    print()
                    print('🔒 Privacidade')
                    print(f'4. Uso de Dados: ({uso_dados})') # Por enquanto não temos a coleta de dados para melhores recomendações, mas o usuário poderá rever e mudar sua decisão
                    print('Toque para rever suas permissões.')
                    print()
                    print('5. Voltar para a câmera ')

                    menu_ajustes = input('\n\nDigite a opção desejada: ')

                    match menu_ajustes:
                        case '1':
                            if filtro_automatico == "ATIVADO":
                                filtro_automatico = 'DESATIVADO'

                                # Caso o filtro automático seja desligado, o visor da câmera ficará sem filtro, até o usuário colocar algum
                                filtro_atual = "SEM FILTRO"

                            else:
                                filtro_automatico = 'ATIVADO'

                                # Caso seja ligado novamente, será determinado novamente um filtro aleatório adequado para o visor
                                filtro_atual = filtros[rd.randint(0,6)]['nome'] 

                        case '2':
                            if grade_de_composicao == "ATIVADO":
                                grade_de_composicao = 'DESATIVADO'

                            else:
                                grade_de_composicao = 'ATIVADO'

                        case '3':
                            if sugestao_automatica == "ATIVADO":
                                sugestao_automatica = 'DESATIVADO'

                            else:
                                sugestao_automatica = 'ATIVADO'

                        case '4':
                            uso_dados = permissoes_dados()

                        case '5':
                            break

                        case _:
                            print_invalido()
                        
            case '4':
                filtro_atual = escolha_filtros(nomes_filtros,filtro_atual) # Função para o usuário mostrar qual filtro deseja aplicar na imagem em tempo real
                
            case '5':
                traseira = not traseira
                # Determina novamente um filtro aleatório de acordo com a imagem no visor da câmera 
                filtro_atual = filtros[rd.randint(0,6)]['nome'] 

                print('\n\nAo virar a câmera, o sistema recalcula em tempo real o filtro adequado! ') 

                if traseira == True:
                    visu = '🌄'

                else:
                    visu = '👦'

            case '6':
                print('\n\nObrigado por usar nosso aplicativo!! ')
                print("Volte sempre!! ")
                break

            case _:
                print_invalido()

if __name__ == "__main__":  # Começo do código
    print('\nBem vindo ao modo Synesthesia !!!\n')

    permissoes_aplicativo()
    dados_permitidos = permissoes_dados()

    main(dados_permitidos)