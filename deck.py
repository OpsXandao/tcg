# deck.py
class Deck:
    def __init__(self):
        self.cartas = []

    def adicionar_carta(self, carta):
        self.cartas.append(carta)
        print(f"Carta {carta.nome} adicionada ao deck.")

    def remover_carta(self, carta):
        if carta in self.cartas:
            self.cartas.remove(carta)
            print(f"Carta {carta.nome} removida do deck.")
        else:
            print("Carta não encontrada no deck.")

    def comprar_carta(self):
        """
        Remove e retorna a carta do topo do deck.
        Se o deck estiver vazio, retorna None.
        """
        if len(self.cartas) > 0:
            return self.cartas.pop()  # Remove e retorna a última carta do deck
        else:
            print("O deck está vazio! Não é possível comprar mais cartas.")
            return None

    def exibir_deck(self):
        if not self.cartas:
            print("O deck está vazio.")
        else:
            print("\nCartas no deck:")
            for i, carta in enumerate(self.cartas, start=1):
                print(f"{i}. {carta.nome}")

    def contar_cartas(self):
        """
        Retorna um dicionário com a contagem de cada carta no deck.
        """
        contagem = {}
        for carta in self.cartas:
            if carta.nome in contagem:
                contagem[carta.nome] += 1
            else:
                contagem[carta.nome] = 1
        return contagem  # Retorna um dicionário com {nome_da_carta: quantidade}

    def __str__(self):
        return f"Deck com {len(self.cartas)} cartas."