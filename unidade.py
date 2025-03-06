class Unidade:
    def __init__(self, nome, ataque, defesa, custo_comida=0, custo_ouro=0, custo_ciencia=0, custo_cultura=0, custo_fe=0, habilidade=None):
        """
        Inicializa uma unidade com nome, ataque, defesa, custos e habilidade.
        """
        self.nome = nome
        self.ataque = ataque
        self.defesa = defesa
        self.custo_comida = custo_comida
        self.custo_ouro = custo_ouro
        self.custo_ciencia = custo_ciencia
        self.custo_cultura = custo_cultura
        self.custo_fe = custo_fe
        self.habilidade = habilidade

    def __str__(self):
        """
        Retorna uma representação simplificada da unidade.
        """
        return f"{self.nome} (Ataque: {self.ataque}, Defesa: {self.defesa}, Habilidade: {self.habilidade})"
    
    def exibir_info(self):
        """
        Retorna informações detalhadas da unidade.
        """
        return (f"Nome: {self.nome}\n"
                f"Ataque: {self.ataque}\n"
                f"Defesa: {self.defesa}\n"
                f"Custo - Comida: {self.custo_comida}, Ouro: {self.custo_ouro}, Ciência: {self.custo_ciencia}, Cultura: {self.custo_cultura}, Fé: {self.custo_fe}\n"
                f"Habilidade: {self.habilidade}")


# Unidades Genéricas
class SoldadoComum(Unidade):
    def __init__(self):
        super().__init__(
            nome="Soldado Comum",
            ataque=2,
            defesa=2,
            custo_comida=1,
            custo_ouro=0,
            habilidade="Nenhuma"
        )


class Arqueiro(Unidade):
    def __init__(self):
        super().__init__(
            nome="Arqueiro",
            ataque=3,
            defesa=1,
            custo_comida=1,
            custo_ouro=1,
            habilidade="Ataque à Distância"
        )


class CavalariaLeve(Unidade):
    def __init__(self):
        super().__init__(
            nome="Cavalaria Leve",
            ataque=3,
            defesa=1,
            custo_comida=1,
            custo_ouro=3,
            habilidade="Movimento Rápido"
        )


class Lanceiro(Unidade):
    def __init__(self):
        super().__init__(
            nome="Lanceiro",
            ataque=3,
            defesa=4,
            custo_comida=2,
            custo_ouro=2,
            habilidade="Nenhuma"
        )


class Catapulta(Unidade):
    def __init__(self):
        super().__init__(
            nome="Catapulta",
            ataque=5,
            defesa=2,
            custo_comida=4,
            custo_ouro=4,
            habilidade="Ataque à Distância"
        )


class SoldadoDeElite(Unidade):
    def __init__(self):
        super().__init__(
            nome="Soldado de Elite",
            ataque=4,
            defesa=4,
            custo_comida=4,
            custo_ouro=0,
            habilidade="Nenhuma"
        )


class EngenheiroDeBatalha(Unidade):
    def __init__(self):
        super().__init__(
            nome="Engenheiro de Batalha",
            ataque=0,
            defesa=3,
            custo_comida=2,
            custo_ouro=1,
            habilidade="Fortificação"
        )


# Unidades Específicas - Egito
class CarroDeCombateEgipcio(Unidade):
    def __init__(self):
        super().__init__(
            nome="Carro de Combate Egípcio",
            ataque=4,
            defesa=3,
            custo_comida=0,
            custo_ouro=4,
            habilidade="Movimento Rápido"
        )


class GuardiaoDoNilo(Unidade):
    def __init__(self):
        super().__init__(
            nome="Guardião do Nilo",
            ataque=3,
            defesa=4,
            custo_comida=0,
            custo_ouro=2,
            custo_fe=2,  # Agora a classe Unidade aceita esse parâmetro
            habilidade="Nenhuma"
        )


class ArqueiroDoDeserto(Unidade):
    def __init__(self):
        super().__init__(
            nome="Arqueiro do Deserto",
            ataque=2,
            defesa=3,
            custo_comida=3,
            custo_ouro=0,
            habilidade="Tiro de Areia"
        )


# Unidades Específicas - Grécia
class HoplitaGrego(Unidade):
    def __init__(self):
        super().__init__(
            nome="Hoplita Grego",
            ataque=3,
            defesa=5,
            custo_comida=3,
            custo_ouro=1,
            habilidade="Formação de Defesa"
        )


class FalcataGrega(Unidade):
    def __init__(self):
        super().__init__(
            nome="Falcata Grega",
            ataque=5,
            defesa=3,
            custo_comida=4,
            custo_ouro=0,
            habilidade="Ataque Poderoso"
        )


class ArqueiroDeDourado(Unidade):
    def __init__(self):
        super().__init__(
            nome="Arqueiro de Dourado",
            ataque=3,
            defesa=2,
            custo_comida=3,
            custo_ouro=2,
            habilidade="Tiro Longo"
        )
