

from abc import ABC, abstractmethod

class Personagem:
    def __init__(self, nome, classe, vida, forca):
        self.nome=nome
        self.classe=classe
        self.vida=vida
        self.forca=forca            

heroi= Personagem("Heron","mago",100,50)        


print(heroi.nome)
print(heroi.classe)
print(heroi.vida)
print(heroi.forca)


    