# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 11:36:05 2022

@author: alumno
"""

from modulos.carta import Carta
from modulos.mazo import Mazo

class JuegoGuerra:
    
    valores = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    palos = ['♠', '♥', '♦', '♣']


    
    def __init__(self):
        self.mazoPrincipal = Mazo()
        self.mazoJ1 = Mazo()
        self.mazoJ2 = Mazo()



    def crearMazo(self):
        for palo in self.palos:
            for valor in self.valores:
                carta = Carta(valor, palo)
                self.mazoPrincipal.agregarArriba(carta)
        
        self.mazoPrincipal.mezclar()

    
    
    def repartirCartas(self):  
        bandera = True
        for i in range(52):
            if bandera == True:
                self.mazoJ1.agregarArriba(self.mazoPrincipal.darCarta())
                bandera=False
            
            elif bandera == False:
                self.mazoJ2.agregarArriba(self.mazoPrincipal.darCarta())
                bandera=True
            

            
    # def iniciar_juego(self):
    #     turno = 0
    #     print("jugador1:")
    #     self.mazoJ1.mostrarCartas()
    #     self.mazoJ1.mostrarCarta() 
    #     self.mazoJ2.mostrarCarta()
    #     print("jugador2:")
    #     self.mazoJ2.mostrarCartas()
    #     if 
        
        
        
            
            
            
        
            
            
            
                
            
           
        

juego1 = JuegoGuerra()

juego1.crearMazo()

juego1.repartirCartas()

# juego1.mazoJ1.mostrarCarta()
# juego1.mazoJ1.mostrarCartas()
