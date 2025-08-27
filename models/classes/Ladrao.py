from models.classes.ClasseBase import Classe

class ladrao(Classe):
    def __init__(self):
        super().__init__(
            nome= "Ladrao",
            dado_dv= 6, 
            equipamento= ["Apenas pequenas ou médias", "APENAS armaduras leves", "Não pode usar Cajados, Varinhas e Pergaminhos"],
            habilidades= ["Ataque Furtivo", "Ouvir Ruídos", "Talentos de Ladrao"]
        )