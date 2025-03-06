# main.py
from cidade import Atenas, Esparta, Corinto
from lider import AlexandreGrande, RamesesII
from jogador import Jogador
from campoDeBatalha import CampoDeBatalha
from unidade import *
from estrutura import *
from deck import Deck
from recursos import CartaComida, CartaOuro, CartaCiencia, CartaFe, CartaCultura, CartaRecurso
import random

def escolher_cidade():
    cidades_disponiveis = [Atenas(), Esparta(), Corinto()]
    print("Bem-vindo ao jogo!")
    print("Escolha sua cidade:")
    for i, cidade in enumerate(cidades_disponiveis, start=1):
        print(f"{i}. {cidade.exibir_info()}")
    while True:
        try:
            escolha = int(input("Digite o número da cidade que deseja escolher: "))
            if 1 <= escolha <= len(cidades_disponiveis):
                return cidades_disponiveis[escolha - 1]
        except ValueError:
            pass
        print("Escolha inválida! Tente novamente.")

def escolher_lider():
    lideres_disponiveis = [AlexandreGrande(), RamesesII()]
    print("\nAgora, escolha seu líder:")
    for i, lider in enumerate(lideres_disponiveis, start=1):
        print(f"{i}. {lider.exibir_info()}")
    while True:
        try:
            escolha = int(input("Digite o número do líder que deseja escolher: "))
            if 1 <= escolha <= len(lideres_disponiveis):
                return lideres_disponiveis[escolha - 1]
        except ValueError:
            pass
        print("Escolha inválida! Tente novamente.")

def montar_deck_maquina():
    # Função para montar o deck da máquina com 20 unidades, 20 estruturas e 20 recursos.
    cartas_unidade = [
        SoldadoComum(), Arqueiro(), CavalariaLeve(), Lanceiro(),
        Catapulta(), SoldadoDeElite(), EngenheiroDeBatalha(),
        CarroDeCombateEgipcio(), GuardiaoDoNilo(), ArqueiroDoDeserto(),
        HoplitaGrego(), FalcataGrega(), ArqueiroDeDourado()
    ]
    
    cartas_estrutura = [
        HortaComunitaria(), FazendaDeGraos(), PlantacaoDeOlivas(),
        MercadoLocal(), FeiraComercial(), PortoMercantil(),
        EscolaDeSabios(), Biblioteca(), AcademiaDeFilosofia(),
        TeatroAoArLivre(), SalaDeArtefatos(), Anfiteatro(),
        AltarDosDeuses(), TemploMenor(), GrandeTemplo()
    ]
    
    cartas_recurso = [
        CartaComida(), CartaOuro(), CartaCiencia(), CartaFe(), CartaCultura()
    ]
    
    deck_maquina = Deck()  # Cria um objeto Deck
    
    # Adicionar 20 unidades aleatórias (ou o máximo possível)
    for carta in random.sample(cartas_unidade, min(20, len(cartas_unidade))):
        deck_maquina.adicionar_carta(carta)
    
    # Adicionar 20 estruturas aleatórias (ou o máximo possível)
    for carta in random.sample(cartas_estrutura, min(20, len(cartas_estrutura))):
        deck_maquina.adicionar_carta(carta)
    
    # Adicionar 20 recursos aleatórios (ou o máximo possível)
    for carta in random.sample(cartas_recurso, min(20, len(cartas_recurso))):
        deck_maquina.adicionar_carta(carta)
    
    random.shuffle(deck_maquina.cartas)  # Embaralha o deck da máquina
    
    return deck_maquina

def montar_deck(jogador):
    deck = Deck()
    cartas_disponiveis = [
        SoldadoComum(), Arqueiro(), CavalariaLeve(), Lanceiro(),
        Catapulta(), SoldadoDeElite(), EngenheiroDeBatalha(),
        CarroDeCombateEgipcio(), GuardiaoDoNilo(), ArqueiroDoDeserto(),
        HoplitaGrego(), FalcataGrega(), ArqueiroDeDourado(),
        HortaComunitaria(), FazendaDeGraos(), PlantacaoDeOlivas(),
        MercadoLocal(), FeiraComercial(), PortoMercantil(),
        EscolaDeSabios(), Biblioteca(), AcademiaDeFilosofia(),
        TeatroAoArLivre(), SalaDeArtefatos(), Anfiteatro(),
        AltarDosDeuses(), TemploMenor(), GrandeTemplo(),
        CartaComida(), CartaOuro(), CartaCiencia(), CartaFe(), CartaCultura()
    ]
    
    while len(deck.cartas) < 60:
        print(f"\nCartas no deck: {len(deck.cartas)}/60")
        print("Cartas já adicionadas:")
        for nome, quantidade in deck.contar_cartas().items():
            print(f"{nome}: {quantidade}")

        print("\nEscolha uma categoria de cartas para adicionar ao seu deck:")
        print("1. Cartas de Unidade")
        print("2. Cartas de Estrutura")
        print("3. Cartas de Recurso")
        print("4. Voltar para o menu anterior")
        
        try:
            categoria_escolhida = int(input("Digite o número da categoria que deseja ver: "))
            
            if categoria_escolhida == 4:
                print("Voltando ao menu anterior...")
                continue  # Retorna ao início da iteração para permitir nova escolha de categoria

            if categoria_escolhida == 1:
                print("\n>>> CARTAS DE UNIDADE <<<")
                cartas_unidade = [carta for carta in cartas_disponiveis if isinstance(carta, Unidade)]
                for i, carta in enumerate(cartas_unidade, start=1):
                    recursos_usados = []
                    if carta.custo_comida > 0:
                        recursos_usados.append(f"{carta.custo_comida} Comida")
                    if carta.custo_ouro > 0:
                        recursos_usados.append(f"{carta.custo_ouro} Ouro")
                    if carta.custo_ciencia > 0:
                        recursos_usados.append(f"{carta.custo_ciencia} Ciência")
                    if carta.custo_fe > 0:
                        recursos_usados.append(f"{carta.custo_fe} Fé")
                    if carta.custo_cultura > 0:
                        recursos_usados.append(f"{carta.custo_cultura} Cultura")
                
                    recursos_str = ", ".join(recursos_usados)
                    print(f"{i}. {carta.nome} (Custo: {recursos_str})")
                
                cartas_escolhidas = cartas_unidade  # Atualizado para categoria correta
                
            elif categoria_escolhida == 2:
                print("\n>>> CARTAS DE ESTRUTURA <<<")
                cartas_estrutura = [carta for carta in cartas_disponiveis if isinstance(carta, Estrutura)]
                for i, carta in enumerate(cartas_estrutura, start=1):
                    recursos_usados = []
                    if carta.custo_comida > 0:
                        recursos_usados.append(f"{carta.custo_comida} Comida")
                    if carta.custo_ouro > 0:
                        recursos_usados.append(f"{carta.custo_ouro} Ouro")
                    if carta.custo_ciencia > 0:
                        recursos_usados.append(f"{carta.custo_ciencia} Ciência")
                    if carta.custo_fe > 0:
                        recursos_usados.append(f"{carta.custo_fe} Fé")
                    if carta.custo_cultura > 0:
                        recursos_usados.append(f"{carta.custo_cultura} Cultura")
                
                    recursos_str = ", ".join(recursos_usados)
                    print(f"{i}. {carta.nome} (Custo: {recursos_str})")
                
                cartas_escolhidas = cartas_estrutura  # Atualizado para categoria correta
                
            elif categoria_escolhida == 3:
                print("\n>>> CARTAS DE RECURSO <<<")
                cartas_recurso = [carta for carta in cartas_disponiveis if isinstance(carta, CartaRecurso)]
                for i, carta in enumerate(cartas_recurso, start=1):
                    print(f"{i}. {carta.exibir_info()}")
                
                cartas_escolhidas = cartas_recurso  # Atualizado para categoria correta
                
            else:
                print("Opção inválida! Tente novamente.")
                continue
            
            try:
                escolha = int(input("Digite o número da carta que deseja adicionar ao deck: "))
                if 1 <= escolha <= len(cartas_escolhidas):  # Usar a lista correta de cartas
                    carta_escolhida = cartas_escolhidas[escolha - 1]
                    
                    # Pergunta a quantidade de cartas a serem adicionadas
                    quantidade = int(input(f"Quantas cartas de {carta_escolhida.nome} você deseja adicionar ao deck? "))
                    
                    # Adiciona a quantidade escolhida de cartas
                    for _ in range(quantidade):
                        deck.adicionar_carta(carta_escolhida)
                    
                    print(f"{quantidade} carta(s) de {carta_escolhida.nome} adicionada(s) ao deck.")
                else:
                    print("Escolha inválida! Tente novamente.")
            except ValueError:
                print("Entrada inválida! Digite um número.")
        
        except ValueError:
            print("Entrada inválida! Digite um número.")
    
    print("\nDeck completo!")
    return deck

def turno(jogador, maquina, campo, deck_jogador, deck_maquina):
    # Começa o turno com compra de 2 cartas para o jogador e a máquina
    print("\nInício do Turno")
    
    jogador.comprar_cartas(2, deck_jogador)  # Passando o deck_jogador como argumento
    maquina.comprar_cartas(2, deck_maquina)  # Passando o deck_maquina como argumento
    
    # Verifica se ambos têm no máximo 9 cartas na mão
    jogador.verificar_mao()
    maquina.verificar_mao()
    
    # Exibe os recursos, cartas na mão e o campo de batalha após compra
    print(f"Recursos de {jogador.cidade.nome}: {jogador.exibir_recursos()}")
    print(f"Cartas na mão do jogador:\n{jogador.exibir_cartas()}")
    print(f"\nRecursos de {maquina.cidade.nome}: {maquina.exibir_recursos()}")
    print(f"Cartas na mão da máquina:\n{maquina.exibir_cartas()}")
    
    campo.exibir_campo()
    
    # Continue com o turno (ações do jogador e da máquina)
    print("\nO jogador pode realizar suas ações agora.")
    # Adicione a lógica do jogo para o turno aqui
    
def main():
    print("===== Início do Jogo =====")
    
    # Escolha das cidades e líderes
    cidade_jogador = escolher_cidade()
    lider_jogador = escolher_lider()
    cidade_maquina = random.choice([Atenas(), Esparta(), Corinto()])
    lider_maquina = random.choice([AlexandreGrande(), RamesesII()])
    
    jogador = Jogador(cidade_jogador, lider_jogador)
    maquina = Jogador(cidade_maquina, lider_maquina)
    
    print(f"\nVocê escolheu {cidade_jogador.nome} e {lider_jogador.nome}")
    print(f"A máquina escolheu {cidade_maquina.nome} e {lider_maquina.nome}")
    
    # Montando os decks
    print("\nMontando o deck do jogador...")
    deck_jogador = montar_deck(jogador)
    deck_jogador.exibir_deck()
    
    print("\nMontando o deck da máquina...")
    deck_maquina = montar_deck_maquina()
    
    # Embaralhando os decks
    print("\nEmbaralhando os decks...")
    random.shuffle(deck_jogador.cartas)
    random.shuffle(deck_maquina.cartas)
    
    # Comprando 5 cartas iniciais para o jogador e a máquina
    print("\nComprando cartas iniciais...")
    jogador.comprar_cartas(5, deck_jogador)  # Passando o deck_jogador como argumento
    maquina.comprar_cartas(5, deck_maquina)  # Passando o deck_maquina como argumento
    
    print(f"Cartas iniciais do jogador: {jogador.exibir_cartas()}")
    print(f"Cartas iniciais da máquina: {maquina.exibir_cartas()}")
    
    # Inicializando o campo de batalha
    campo = CampoDeBatalha()
    campo.exibir_campo()
    
    # Iniciando o turno
    turno(jogador, maquina, campo, deck_jogador, deck_maquina)

if __name__ == "__main__":
    main()