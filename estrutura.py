# estrutura.py
class Estrutura:
    def __init__(self, nome, custo, efeito, descricao):
        self.nome = nome
        self.custo = custo  # Dicionário com os custos (ex: {"Comida": 1, "Ouro": 1})
        self.efeito = efeito
        self.descricao = descricao
    
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

    def gerar_recursos(self, recursos):
        """
        Adiciona recursos ao jogador de acordo com o efeito da estrutura.
        :param recursos: Objeto da classe Recursos do jogador.
        """
        if "+1 Comida" in self.efeito:
            recursos.adicionar_recursos(comida=1)
        elif "+2 Comida" in self.efeito:
            recursos.adicionar_recursos(comida=2)
        elif "+3 Comida" in self.efeito:
            recursos.adicionar_recursos(comida=3)

        if "+1 Ouro" in self.efeito:
            recursos.adicionar_recursos(ouro=1)
        elif "+2 Ouro" in self.efeito:
            recursos.adicionar_recursos(ouro=2)
        elif "+3 Ouro" in self.efeito:
            recursos.adicionar_recursos(ouro=3)

        if "+1 Ciência" in self.efeito:
            recursos.adicionar_recursos(ciencia=1)
        elif "+2 Ciência" in self.efeito:
            recursos.adicionar_recursos(ciencia=2)
        elif "+3 Ciência" in self.efeito:
            recursos.adicionar_recursos(ciencia=3)

        if "+1 Fé" in self.efeito:
            recursos.adicionar_recursos(fe=1)
        elif "+2 Fé" in self.efeito:
            recursos.adicionar_recursos(fe=2)
        elif "+3 Fé" in self.efeito:
            recursos.adicionar_recursos(fe=3)

        if "+1 Cultura" in self.efeito:
            recursos.adicionar_recursos(cultura=1)
        elif "+2 Cultura" in self.efeito:
            recursos.adicionar_recursos(cultura=2)
        elif "+3 Cultura" in self.efeito:
            recursos.adicionar_recursos(cultura=3)

    def __str__(self):
        return f"{self.nome} - Custo: {self.custo} - Efeito: {self.efeito} - {self.descricao}"
# Estruturas de Comida (🌽)
class HortaComunitaria(Estrutura):
    def __init__(self):
        super().__init__("Horta Comunitária", {"Comida": 1, "Ouro": 1}, "Gera +1 Comida por turno", "Uma pequena horta que sustenta a população local.")

class FazendaDeGraos(Estrutura):
    def __init__(self):
        super().__init__("Fazenda de Grãos", {"Comida": 2, "Ouro": 2}, "Gera +2 Comida por turno", "Campos de trigo e cevada que alimentam toda a região.")

class PlantacaoDeOlivas(Estrutura):
    def __init__(self):
        super().__init__("Plantação de Olivas", {"Comida": 3, "Ouro": 3}, "Gera +3 Comida por turno", "Oliveiras que produzem azeite e azeitonas, essenciais para a dieta.")

# Estruturas de Ouro (💰)
class MercadoLocal(Estrutura):
    def __init__(self):
        super().__init__("Mercado Local", {"Ouro": 1, "Comida": 1}, "Gera +1 Ouro por turno", "Um pequeno mercado onde os comerciantes trocam bens e serviços.")

class FeiraComercial(Estrutura):
    def __init__(self):
        super().__init__("Feira Comercial", {"Ouro": 2, "Comida": 2}, "Gera +2 Ouro por turno", "Uma feira movimentada que atrai comerciantes de longe.")

class PortoMercantil(Estrutura):
    def __init__(self):
        super().__init__("Porto Mercantil", {"Ouro": 3, "Comida": 3}, "Gera +3 Ouro por turno", "Um porto movimentado que facilita o comércio marítimo.")

# Estruturas de Ciência (🔬)
class EscolaDeSabios(Estrutura):
    def __init__(self):
        super().__init__("Escola de Sábios", {"Ciencia": 1, "Ouro": 1}, "Gera +1 Ciência por turno", "Um local onde os sábios compartilham conhecimentos.")

class Biblioteca(Estrutura):
    def __init__(self):
        super().__init__("Biblioteca", {"Ciencia": 2, "Ouro": 2}, "Gera +2 Ciência por turno", "Um observatório para estudar as estrelas e prever eventos.")

class AcademiaDeFilosofia(Estrutura):
    def __init__(self):
        super().__init__("Academia de Filosofia", {"Ciencia": 3, "Ouro": 3}, "Gera +3 Ciência por turno", "Um centro de aprendizado onde grandes mentes se reúnem.")

# Estruturas de Cultura (🎭)
class TeatroAoArLivre(Estrutura):
    def __init__(self):
        super().__init__("Teatro ao Ar Livre", {"Cultura": 1, "Ouro": 1}, "Gera +1 Cultura por turno", "Um local onde artistas encenam peças e contam histórias.")

class SalaDeArtefatos(Estrutura):
    def __init__(self):
        super().__init__("Sala de Artefatos", {"Cultura": 2, "Ouro": 2}, "Gera +2 Cultura por turno", "Um repositório de conhecimento e histórias antigas.")

class Anfiteatro(Estrutura):
    def __init__(self):
        super().__init__("Anfiteatro", {"Cultura": 3, "Ouro": 3}, "Gera +3 Cultura por turno", "Um grande local para espetáculos e celebrações culturais.")

# Estruturas de Fé (🙏)
class AltarDosDeuses(Estrutura):
    def __init__(self):
        super().__init__("Altar dos Deuses", {"Fe": 1, "Ouro": 1}, "Gera +1 Fé por turno", "Um local sagrado para orações e oferendas.")

class TemploMenor(Estrutura):
    def __init__(self):
        super().__init__("Templo Menor", {"Fe": 2, "Ouro": 2}, "Gera +2 Fé por turno", "Um templo dedicado aos deuses locais.")

class GrandeTemplo(Estrutura):
    def __init__(self):
        super().__init__("Grande Templo", {"Fe": 3, "Ouro": 3}, "Gera +3 Fé por turno", "Um imponente templo que atrai peregrinos de toda a região.")

# Estruturas Únicas para a Grécia
class ColegioDeArquiteto(Estrutura):
    def __init__(self):
        super().__init__("Colégio de Arquiteto", {"Cultura": 2, "Ouro": 1}, "Unidades de corpo a corpo ganham +1 de defesa.", "O Colégio de Arquiteto fortalece a defesa das unidades.")

class TemploDeAtena(Estrutura):
    def __init__(self):
        super().__init__("Templo de Atena", {"Cultura": 3, "Ouro": 2}, "Gera +2 Cultura por turno.", "Dedicado à deusa Atena, fortalece a cultura da região.")

class AcademiaMilitar(Estrutura):
    def __init__(self):
        super().__init__("Academia Militar", {"Comida": 2, "Ouro": 2}, "Unidades de corpo a corpo ganham +1 de ataque.", "A academia treina generais e soldados para aprimorar combate.")

# Estruturas Únicas para o Egito
class ObeliscoSolar(Estrutura):
    def __init__(self):
        super().__init__("Obelisco Solar", {"Fe": 2, "Ouro": 1}, "Gera +1 Fé por turno e +1 ataque para unidades de corpo a corpo.", "Obeliscos honram o deus Sol e fortalecem as tropas.")

class PlantacaoDoNilo(Estrutura):
    def __init__(self):
        super().__init__("Plantação do Nilo", {"Comida": 3, "Ouro": 2}, "Gera +3 Comida por turno.", "Usando tecnologias antigas, o Egito produz grande quantidade de alimento.")

class BibliotecaDeAlexandria(Estrutura):
    def __init__(self):
        super().__init__("Biblioteca de Alexandria", {"Ciencia": 3, "Ouro": 2}, "Gera +2 Ciência por turno e permite comprar 1 carta adicional de tecnologia por turno.", "A maior biblioteca do mundo antigo, promovendo inovações.")