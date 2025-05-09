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
        self.mao = []  # Lista para armazenar as cartas na mão do jogador
        self.estruturas = []  # Lista para armazenar as estruturas do jogador

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

    def adicionar_estrutura(self, estrutura):
        """
        Adiciona uma estrutura ao jogador.
        """
        self.estruturas.append(estrutura)

    def gerar_recursos_estruturas(self):
        """
        Aciona o efeito de geração de recursos de todas as estruturas do jogador.
        """
        for estrutura in self.estruturas:
            estrutura.gerar_recursos(self.recursos)

    def comprar_cartas(self, quantidade, deck):
        """
        Compra uma quantidade específica de cartas do deck e adiciona à mão do jogador.
        """
        for _ in range(quantidade):
            if len(deck.cartas) > 0:
                carta_comprada = deck.comprar_carta()
                self.mao.append(carta_comprada)
            else:
                print("O deck está vazio! Não é possível comprar mais cartas.")
                break

    def exibir_cartas(self):
        """
        Exibe as cartas na mão do jogador.
        """
        return "\n".join([carta.exibir_info() for carta in self.mao])

    def verificar_mao(self):
        """
        Verifica se o jogador tem mais de 9 cartas na mão e ajusta para no máximo 9 cartas.
        """
        if len(self.mao) > 9:
            print(f"Você tem mais de 9 cartas na mão, removendo as excedentes...")
            self.mao = self.mao[:9]  # Mantém apenas as 9 primeiras cartas, descartando as outras
        print(f"Cartas na mão após verificação: {len(self.mao)} cartas.")
    
    def __str__(self):
        """
        Retorna uma representação simplificada do jogador.
        Inclui a vida da cidade.
        """
        return (f"Jogador: {self.cidade.nome} (Vida: {self.cidade.vida}), "
                f"Líder: {self.lider.nome}\nRecursos: {self.recursos}")
