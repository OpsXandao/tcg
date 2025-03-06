# campo_de_batalha.py
class CampoDeBatalha:
    def __init__(self):
        """
        Inicializa o campo de batalha com 3 linhas e 4 colunas.
        Cada posição é inicializada como None (vazia).
        """
        self.tabuleiro = [
            [None, None, None, None],  # Linha de Defesa
            [None, None, None, None],  # Linha Central
            [None, None, None, None]   # Linha Avançada
        ]

    def posicionar_unidade(self, linha, coluna, unidade):
        """
        Posiciona uma unidade no campo de batalha.
        :param linha: 0 (Defesa), 1 (Central), 2 (Avançada)
        :param coluna: 0 a 3
        :param unidade: Objeto da unidade a ser posicionada
        """
        if 0 <= linha < 3 and 0 <= coluna < 4:
            if self.tabuleiro[linha][coluna] is None:
                self.tabuleiro[linha][coluna] = unidade
                print(f"Unidade {unidade.nome} posicionada na linha {linha}, coluna {coluna}.")
            else:
                print("Posição já ocupada!")
        else:
            print("Posição inválida!")

    def exibir_campo(self):
        """
        Exibe o campo de batalha no console.
        """
        print("\nCampo de Batalha:")
        for i, linha in enumerate(self.tabuleiro):
            print(f"Linha {i}: ", end="")
            for posicao in linha:
                if posicao is None:
                    print("[ Vazio ]", end=" ")
                else:
                    print(f"[ {posicao.nome} ]", end=" ")
            print()  # Nova linha