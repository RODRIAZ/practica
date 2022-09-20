# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 14:42:31 2022

@author: alumno
"""
from module.LDE import ListaDobleEnlazada
class ColaDoble:
    def __init__(self):
        self.items = ListaDobleEnlazada()

    def estaVacia(self):
        return self.items.estaVacia()

    def agregarFrente(self, item):
        self.items.agregar(item)

    def agregarFinal(self, item): 
        self.items.anexar(item)

    def removerFrente(self):        #no los elimina de la cola
        return self.items.extraer(0)

    def removerFinal(self):
        return self.items.extraer()

    def tamano(self):
        return self.items.tamanio
    
    def mostrarFrente(self):
        return print(self.items.cabeza.dato)
    
    
    def mostrarFinal(self):
        return print(self.items.cola.dato) 
