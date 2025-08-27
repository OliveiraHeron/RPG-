from models.classes.Guerreiro import Guerreiro
from models.classes.Clerigo import Clerigo  
from models.classes.Ladrao import ladrao    

def classe_escolha(escolha: str):
        if escolha == "1":
            return Guerreiro()
        elif escolha == "2":
            return Clerigo()
        elif escolha == "3":
            return ladrao()
        else:
            print("Numero sem classe definida, escolhendo guerreiro por padrão")
            return Guerreiro()