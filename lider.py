# lider.py
class Lider:
    def __init__(self, nome, efeito, descricao):
        self.nome = nome
        self.efeito = efeito
        self.descricao = descricao

    def exibir_info(self):
        """
        Exibe as informações do líder (nome, efeito e descrição).
        """
        return f"{self.nome}\nEfeito: {self.efeito}\nDescrição: {self.descricao}"

    def __str__(self):
        """
        Retorna uma representação simplificada do líder.
        """
        return f"{self.nome}"

class AlexandreGrande(Lider):
    def __init__(self):
        super().__init__(
            nome="Alexandre, o Grande",
            efeito="Quando uma unidade derrota outra em combate, você pode comprar uma carta. Além disso, todas as unidades de cavalaria ganham +1 de ataque.",
            descricao="Com um exército disciplinado e estratégias inovadoras, Alexandre expandiu seu império a um ritmo implacável, levando a cultura helenística a terras distantes."
        )


class RamesesII(Lider):
    def __init__(self):
        super().__init__(
            nome="Ramsés IIs",
            efeito="Estruturas geram +1 recurso do tipo que produzem.",
            descricao="O grande faraó de inúmeras construções monumentais e vitórias militares, Ramsés II consolidou o Egito como uma potência inabalável."
        )