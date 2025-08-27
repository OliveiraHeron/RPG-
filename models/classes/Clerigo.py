from models.classes.ClasseBase import Classe

class Clerigo(Classe):
    def __init__(self):
        super().__init__(
            nome= "Clerigo",
            dado_dv= 4, 
            equipamento= ["APENAS armas impactantes", "Podem usar todas as armaduras", "Clerigo é capaz de usar todos os tipos de itens mágicos desde que sejam ordeiros"],
            habilidades= ["Magias Divinas", "Afastar Mortos-Vivos", "Cura Milagrosa"]
        )   