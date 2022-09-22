# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 15:41:36 2022

@author: alumno

"""
from modulos.cola_doble import ColaDoble

class Mazo:
    def __init__(self):
        self.mazo = ColaDoble()
        
    def mostrarCarta(self):  
        carta = self.mazo.devolverFinal()  #no tendria que devolver frente?
        return print(carta.numero + carta.palo) 
        
    def compararCarta(self):
        carta = self.mazo.devolverFinal()
        return carta
    
    def darCarta(self):
        carta = self.mazo.devolverFinal()
        self.mazo.removerFinal()
        return carta
    
    def agregarArriba(self, Carta):
        self.mazo.agregarFinal(Carta)
        
    def agregarAbajo(self, Carta):
        self.mazo.agregarFrente(Carta)
    
    def cantidadCartas(self):
        return self.mazo.tamano()
    
    def mostrarCartas(self):
        aux=[]
        for i in range(self.cantidadCartas()):
            aux.append('X')
        return print(aux)
    
    def mezclar(self):
        self.mazo.mezclar()


# mazo=Mazo()
# mazo2=Mazo()
# mazo.agregarAbajo(Carta('8','♥'))

# mazo2.agregarAbajo(mazo.darCarta())
# mazo2.cantidadCartas()
# mazo.cantidadCartas()