# recursos.py
class Recursos:
    def __init__(self, comida=5, ouro=5, ciencia=5, fe=5, cultura=5):
        """
        Inicializa os recursos com valores padrão ou personalizados.
        """
        self.comida = comida
        self.ouro = ouro
        self.ciencia = ciencia
        self.fe = fe
        self.cultura = cultura

    def adicionar_recursos(self, comida=0, ouro=0, ciencia=0, fe=0, cultura=0):
        """
        Adiciona valores aos recursos.
        """
        self.comida += comida
        self.ouro += ouro
        self.ciencia += ciencia
        self.fe += fe
        self.cultura += cultura

    def remover_recursos(self, comida=0, ouro=0, ciencia=0, fe=0, cultura=0):
        """
        Remove valores dos recursos.
        Verifica se há recursos suficientes antes de remover.
        Retorna True se a remoção for bem-sucedida, False caso contrário.
        """
        if (self.comida >= comida and
            self.ouro >= ouro and
            self.ciencia >= ciencia and
            self.fe >= fe and
            self.cultura >= cultura):
            self.comida -= comida
            self.ouro -= ouro
            self.ciencia -= ciencia
            self.fe -= fe
            self.cultura -= cultura
            return True
        else:
            print("Recursos insuficientes!")
            return False

    def exibir_recursos(self):
        """
        Exibe os recursos atuais.
        """
        return (f"Comida: {self.comida}\n"
                f"Ouro: {self.ouro}\n"
                f"Ciência: {self.ciencia}\n"
                f"Fé: {self.fe}\n"
                f"Cultura: {self.cultura}")

    def __str__(self):
        """
        Retorna uma representação simplificada dos recursos.
        """
        return f"Comida: {self.comida}, Ouro: {self.ouro}, Ciência: {self.ciencia}, Fé: {self.fe}, Cultura: {self.cultura}"
    
# Definindo uma classe base para as cartas de recursos
class CartaRecurso:
    def __init__(self, nome, tipo_recurso, quantidade):
        self.nome = nome
        self.tipo_recurso = tipo_recurso
        self.quantidade = quantidade

    def exibir_info(self):
        return f"{self.nome} - Quantidade: {self.quantidade} {self.tipo_recurso.capitalize()}"

# Modificando as classes de recursos para herdar de CartaRecurso
class CartaComida(CartaRecurso):
    def __init__(self):
        super().__init__("Carta de Comida", "Comida", 1)

class CartaOuro(CartaRecurso):
    def __init__(self):
        super().__init__("Carta de Ouro", "Ouro", 1)

class CartaCiencia(CartaRecurso):
    def __init__(self):
        super().__init__("Carta de Ciência", "Ciência", 1)

class CartaFe(CartaRecurso):
    def __init__(self):
        super().__init__("Carta de Fé", "Fé", 1)

class CartaCultura(CartaRecurso):
    def __init__(self):
        super().__init__("Carta de Cultura", "Cultura", 1)
