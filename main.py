# main.py
from cidade import Atenas, Esparta, Corinto
from lider import AlexandreGrande, RamesesII
from jogador import Jogador
import random

def escolher_cidade():
    """
    Exibe um menu para o jogador escolher sua cidade.
    Retorna um objeto Cidade com base na escolha.
    """
    cidades_disponiveis = [Atenas(), Esparta(), Corinto()]

    print("Bem-vindo ao jogo!")
    print("Escolha sua cidade:")

    for i, cidade in enumerate(cidades_disponiveis, start=1):
        print(f"{i}. {cidade.exibir_info()}")

    escolha = input("Digite o número da cidade que deseja escolher: ")

    try:
        escolha = int(escolha)
        if 1 <= escolha <= len(cidades_disponiveis):
            return cidades_disponiveis[escolha - 1]
        else:
            print("Escolha inválida! Tente novamente.")
            return escolher_cidade()
    except ValueError:
        print("Entrada inválida! Digite um número.")
        return escolher_cidade()

def escolher_lider():
    """
    Exibe um menu para o jogador escolher seu líder.
    Retorna um objeto Lider com base na escolha.
    """
    lideres_disponiveis = [AlexandreGrande(), RamesesII()]

    print("\nAgora, escolha seu líder:")

    for i, lider in enumerate(lideres_disponiveis, start=1):
        print(f"{i}. {lider.exibir_info()}")

    escolha = input("Digite o número do líder que deseja escolher: ")

    try:
        escolha = int(escolha)
        if 1 <= escolha <= len(lideres_disponiveis):
            return lideres_disponiveis[escolha - 1]
        else:
            print("Escolha inválida! Tente novamente.")
            return escolher_lider()
    except ValueError:
        print("Entrada inválida! Digite um número.")
        return escolher_lider()

def escolher_cidade_aleatoria():
    """
    Escolhe uma cidade aleatória para a máquina.
    Retorna um objeto Cidade.
    """
    cidades_disponiveis = [Atenas(), Esparta(), Corinto()]
    cidade_escolhida = random.choice(cidades_disponiveis)
    return cidade_escolhida

def escolher_lider_aleatorio():
    """
    Escolhe um líder aleatório para a máquina.
    Retorna um objeto Lider.
    """
    lideres_disponiveis = [AlexandreGrande(), RamesesII()]
    lider_escolhido = random.choice(lideres_disponiveis)
    return lider_escolhido

def main():
    """
    Função principal do jogo.
    """
    print("===== Início do Jogo =====")
    
    # Jogador escolhe sua cidade
    cidade_jogador = escolher_cidade()
    print(f"\nVocê escolheu a {cidade_jogador}!")

    # Jogador escolhe seu líder
    lider_jogador = escolher_lider()
    print(f"\nVocê escolheu o líder {lider_jogador}!")

    # Máquina escolhe uma cidade aleatória
    cidade_maquina = escolher_cidade_aleatoria()

    # Máquina escolhe um líder aleatório
    lider_maquina = escolher_lider_aleatorio()

    # Exibe as escolhas do jogador e da máquina
    print(f"\n>>> Você escolheu {cidade_jogador.nome} e {lider_jogador.nome} <<<")
    print(f"\n>>> A máquina escolheu {cidade_maquina.nome} e {lider_maquina.nome} <<<")

    # Cria o jogador
    jogador = Jogador(cidade_jogador, lider_jogador)

    # Aqui você pode continuar com a lógica do jogo, como criar o jogador, o inimigo, etc.
    print("\nO jogo está começando...")
    print(f"\n{jogador}")

if __name__ == "__main__":
    main()