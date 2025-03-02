# jogador.py
from recursos import Recursos

class Jogador:
    def __init__(self, cidade, lider):
        """
        Inicializa o jogador com uma cidade, um líder e recursos.
        Cada jogador começa com 5 de cada recurso.
        """
        self.cidade = cidade
        self.lider = lider
        self.recursos = Recursos()  # Inicializa com 5 de cada recurso

    def adicionar_recursos(self, comida=0, ouro=0, ciencia=0, fe=0, cultura=0):
        """
        Adiciona recursos ao jogador.
        """
        self.recursos.adicionar_recursos(comida, ouro, ciencia, fe, cultura)

    def remover_recursos(self, comida=0, ouro=0, ciencia=0, fe=0, cultura=0):
        """
        Remove recursos do jogador.
        Retorna True se a remoção for bem-sucedida, False caso contrário.
        """
        return self.recursos.remover_recursos(comida, ouro, ciencia, fe, cultura)

    def exibir_recursos(self):
        """
        Exibe os recursos do jogador.
        """
        return self.recursos.exibir_recursos()

    def __str__(self):
        """
        Retorna uma representação simplificada do jogador.
        Inclui a vida da cidade.
        """
        return (f"Jogador: {self.cidade.nome} (Vida: {self.cidade.vida}), "
                f"Líder: {self.lider.nome}\nRecursos: {self.recursos}")