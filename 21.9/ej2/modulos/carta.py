# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 14:46:15 2022

@author: alumno
"""

class Carta:
    def __init__(self,num,pal):
        self._numero = num
        self._palo = pal
        self._cara = "boca abajo"
        
    @property   
    def numero(self):
        return self._numero
    
    # @numero.setter
    # def numero(self, valor):
    #     self._numero = valor
   
    @property
    def palo(self):
        return self._palo
    
    # @palo.setter
    # def palo(self, valor):
    #     self._palo = valor
    
    @property
    def cara(self):
        return self._cara
    
    # @cara.setter
    # def cara(self, valor):
    #     self._cara = valor
    
    def voltear(self):
        if self.cara == "boca abajo":
            self.cara = "boca arriba"
        else:
            self.cara = "boca abajo"
    
    def __lt__(self):
        pass


