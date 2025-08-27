import random

class DistribuidorAtributos:

    def rolar_3d6(self):
        return sum(random.randint(1, 6) for _ in range(3)) 

    def rolar_4d6_descartar_menor(self):
        dados = [random.randint(1, 6) for _ in range(4)]
        dados.remove(min(dados))
        return sum(dados)

    def dado_classico(self):
        return [self.rolar_3d6() for _ in range(6)]

    def dado_heroico(self):
        return [self.rolar_4d6_descartar_menor() for _ in range(6)]

    def escolher_atributos(self, estilo):
        if estilo == "aventureiro":
            dados = self.dado_classico()
        elif estilo == "heroico":
            dados = self.dado_heroico()
        else:
            print("Estilo desconhecido, usando estilo clássico por padrão.")
            dados = self.dado_classico()

        while True:
           
                escolha_atributos = input(
                    f"\nVocê tirou os dados: {dados}\n"
                    f"Ordem: [FORÇA, DESTREZA, CONSTITUIÇÃO, INTELIGÊNCIA, SABEDORIA, CARISMA]\n"
                    f"Agora determine onde vai colocar os pontos (separe por vírgula): "
                )
                valores = [int(x.strip()) for x in escolha_atributos.split(",") if x.strip() != '']
                
