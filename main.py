# main.py
from cidade import Atenas, Esparta, Corinto
from lider import AlexandreGrande, RamesesII
from jogador import Jogador
from campoDeBatalha import CampoDeBatalha
from unidade import *
from estrutura import *
from deck import Deck
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
        AltarDosDeuses(), TemploMenor(), GrandeTemplo()
    ]
    
    while len(deck.cartas) < 60:
        print("\nCartas disponíveis para adicionar ao deck:")
        for i, carta in enumerate(cartas_disponiveis, start=1):
            print(f"{i}. {carta.nome} (Custo: {carta.custo_comida} Comida, {carta.custo_ouro} Ouro)")
        print(f"\nCartas no deck: {len(deck.cartas)}/60")
        print("Cartas já adicionadas:")
        for nome, quantidade in deck.contar_cartas().items():
            print(f"{nome}: {quantidade}")
        
        try:
            escolha = int(input("Digite o número da carta que deseja adicionar ao deck: "))
            if 1 <= escolha <= len(cartas_disponiveis):
                carta_escolhida = cartas_disponiveis[escolha - 1]
                deck.adicionar_carta(carta_escolhida)
            else:
                print("Escolha inválida! Tente novamente.")
        except ValueError:
            print("Entrada inválida! Digite um número.")
    
    print("\nDeck completo!")
    return deck

def main():
    print("===== Início do Jogo =====")
    cidade_jogador = escolher_cidade()
    lider_jogador = escolher_lider()
    jogador = Jogador(cidade_jogador, lider_jogador)
    print(f"\nVocê escolheu {cidade_jogador.nome} e {lider_jogador.nome}")
    
    print("\nMontando seu deck...")
    deck_jogador = montar_deck(jogador)
    deck_jogador.exibir_deck()
    
    print("\nO jogo está começando...")
    print(f"\n{jogador}")

if __name__ == "__main__":
    main()
