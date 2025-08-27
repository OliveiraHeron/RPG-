from models.racas.Humano import Humano
from models.racas.Elfo import Elfo
from models.racas.Anao import Anao
from models.racas.Gnomo import Gnomo
from models.racas.Halfling import Halfling
from models.racas.MeioElfo import MeioElfo

def raca_escolha(escolha: str):
    racas = {
        "1": Humano,
        "2": Elfo,
        "3": Halfling,
        "4": Anao,
        "5": Gnomo,
        "6": MeioElfo
    }

    raca_classe = racas.get(escolha)
    if raca_classe:
        return raca_classe()
    else:
        print("Número sem raça definida, escolhendo Humano por padrão.")
        return Humano()
