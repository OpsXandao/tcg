class Cidade:
    def __init__(self, id, nome, vida, bonus, descricao):
        self.id = id
        self.nome = nome
        self.vida = vida
        self.bonus = bonus
        self.descricao = descricao

    def tomar_dano(self, dano):
        self.vida -= dano
        if self.vida < 0:
            self.vida = 0

    def esta_viva(self):
        return self.vida > 0

    def exibir_info(self):
        return f"{self.nome} (Vida: {self.vida})\nBônus: {self.bonus}\nDescrição: {self.descricao}"

    def __str__(self):
        return f"{self.nome} (Vida: {self.vida})"


class Atenas(Cidade):
    def __init__(self):
        super().__init__(
            id=1,
            nome="Atenas",
            vida=20,
            bonus="Cultura",
            descricao="O berço da filosofia, da democracia e das artes, Atenas se destaca como um farol de conhecimento e cultura no mundo antigo."
        )


class Esparta(Cidade):
    def __init__(self):
        super().__init__(
            id=2,
            nome="Esparta",
            vida=25,
            bonus="Combate",
            descricao="Forjada na disciplina e no combate, Esparta molda guerreiros imbatíveis, prontos para enfrentar qualquer desafio no campo de batalha."
        )


class Corinto(Cidade):
    def __init__(self):
        super().__init__(
            id=3,
            nome="Corinto",
            vida=30,
            bonus="Comércio",
            descricao="Uma cidade próspera e estrategicamente posicionada, Corinto é um centro comercial essencial para o mundo grego."
        )