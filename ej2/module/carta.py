# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 14:46:15 2022

@author: alumno
"""

class Carta:
    def __init__(self, numero, palo):
        self.numero = numero
        self.palo = palo
        self.cara = "boca abajo"
        
    @property   
    def numero(self):
        return self._numero
    @property
    def palo(self):
        return self._palo
    @property
    def cara(self):
        return self._cara
    
    def voltear(self):
        if self.cara == "boca abajo":
            self.cara = "boca arriba"
        else:
            self.cara = "boca abajo"
    

    
    def __iter__(self):
         nodo = self.cabeza
         while nodo :
             yield nodo
             nodo = nodo.siguiente


