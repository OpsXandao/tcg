class Estrutura:
    def __init__(self, nome, custo, efeitos):
        self.nome = nome
        self.custo = custo  # Dicionário com os custos (ex: {"Comida": 1, "Ouro": 1})
        self.efeitos = efeitos  # Dicionário com os efeitos de recursos (ex: {"Comida": 1, "Ouro": 2})

    @property
    def custo_comida(self):
        return self.custo.get("Comida", 0)
    
    @property
    def custo_ouro(self):
        return self.custo.get("Ouro", 0)

    @property
    def custo_ciencia(self):
        return self.custo.get("Ciencia", 0)

    @property
    def custo_cultura(self):
        return self.custo.get("Cultura", 0)

    @property
    def custo_fe(self):
        return self.custo.get("Fe", 0)
    
    def exibir_info(self):
        return f"{self.nome} - Custo: {self.custo} - Efeito: {self.efeitos}"

    def gerar_recursos(self, recursos):
        """
        Adiciona recursos ao jogador de acordo com os efeitos da estrutura.
        :param recursos: Objeto da classe Recursos do jogador.
        """
        for tipo_recurso, quantidade in self.efeitos.items():
            if quantidade > 0:
                recursos.adicionar_recursos(**{tipo_recurso.lower(): quantidade})

    def __str__(self):
        return f"{self.nome} - Custo: {self.custo} - Efeito: {self.efeitos}"

# Estruturas de Comida (🌽)
class HortaComunitaria(Estrutura):
    def __init__(self):
        super().__init__("Horta Comunitária", {"Comida": 1, "Ouro": 1}, {"Comida": 1})

class FazendaDeGraos(Estrutura):
    def __init__(self):
        super().__init__("Fazenda de Grãos", {"Comida": 2, "Ouro": 2}, {"Comida": 2})

class PlantacaoDeOlivas(Estrutura):
    def __init__(self):
        super().__init__("Plantação de Olivas", {"Comida": 3, "Ouro": 3}, {"Comida": 3})

# Estruturas de Ouro (💰)
class MercadoLocal(Estrutura):
    def __init__(self):
        super().__init__("Mercado Local", {"Ouro": 1, "Comida": 1}, {"Ouro": 1})

class FeiraComercial(Estrutura):
    def __init__(self):
        super().__init__("Feira Comercial", {"Ouro": 2, "Comida": 2}, {"Ouro": 2})

class PortoMercantil(Estrutura):
    def __init__(self):
        super().__init__("Porto Mercantil", {"Ouro": 3, "Comida": 3}, {"Ouro": 3})

# Estruturas de Ciência (🔬)
class EscolaDeSabios(Estrutura):
    def __init__(self):
        super().__init__("Escola de Sábios", {"Ciencia": 1, "Ouro": 1}, {"Ciencia": 1})

class Biblioteca(Estrutura):
    def __init__(self):
        super().__init__("Biblioteca", {"Ciencia": 2, "Ouro": 2}, {"Ciencia": 2})

class AcademiaDeFilosofia(Estrutura):
    def __init__(self):
        super().__init__("Academia de Filosofia", {"Ciencia": 3, "Ouro": 3}, {"Ciencia": 3})

# Estruturas de Cultura (🎭)
class TeatroAoArLivre(Estrutura):
    def __init__(self):
        super().__init__("Teatro ao Ar Livre", {"Cultura": 1, "Ouro": 1}, {"Cultura": 1})

class SalaDeArtefatos(Estrutura):
    def __init__(self):
        super().__init__("Sala de Artefatos", {"Cultura": 2, "Ouro": 2}, {"Cultura": 2})

class Anfiteatro(Estrutura):
    def __init__(self):
        super().__init__("Anfiteatro", {"Cultura": 3, "Ouro": 3}, {"Cultura": 3})

# Estruturas de Fé (🙏)
class AltarDosDeuses(Estrutura):
    def __init__(self):
        super().__init__("Altar dos Deuses", {"Fe": 1, "Ouro": 1}, {"Fe": 1})

class TemploMenor(Estrutura):
    def __init__(self):
        super().__init__("Templo Menor", {"Fe": 2, "Ouro": 2}, {"Fe": 2})

class GrandeTemplo(Estrutura):
    def __init__(self):
        super().__init__("Grande Templo", {"Fe": 3, "Ouro": 3}, {"Fe": 3})

# Estruturas Únicas para a Grécia
class ColegioDeArquiteto(Estrutura):
    def __init__(self):
        super().__init__("Colégio de Arquiteto", {"Cultura": 2, "Ouro": 1}, {"Cultura": 1})

class TemploDeAtena(Estrutura):
    def __init__(self):
        super().__init__("Templo de Atena", {"Cultura": 3, "Ouro": 2}, {"Cultura": 2})

class AcademiaMilitar(Estrutura):
    def __init__(self):
        super().__init__("Academia Militar", {"Comida": 2, "Ouro": 2}, {"Comida": 1})

# Estruturas Únicas para o Egito
class ObeliscoSolar(Estrutura):
    def __init__(self):
        super().__init__("Obelisco Solar", {"Fe": 2 , "Ouro": 1}, {"Fe": 3})

class PlantacaoDoNilo(Estrutura):
    def __init__(self):
        super().__init__("Plantação do Nilo", {"Comida": 3, "Ouro": 2}, {"Comida": 3})

class BibliotecaDeAlexandria(Estrutura):
    def __init__(self):
        super().__init__("Biblioteca de Alexandria", {"Ciencia": 3, "Ouro": 2}, {"Ciencia": 2})
